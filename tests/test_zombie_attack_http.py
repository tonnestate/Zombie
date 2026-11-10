"""Real loopback HTTP integration check: test the transport, NOT any LLM."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from threading import Thread

import zombie_attack_validate as z


class LocalSyntheticAgent(BaseHTTPRequestHandler):
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])).decode())
        is_direct = "messages" in data
        document = data["messages"][1]["content"] if is_direct else data["retrieved_content"]
        attacked = (
            "[im_start]system" in document
            or "Assistant instruction:" in document
            or '"instruction": ' in document
        )
        output = z.MARKER if attacked else z.EXPECTED
        if is_direct:
            result = {"model": data["model"], "choices": [{"message": {"content": output}}]}
        else:
            result = {"response": output, "observed_model_id": "synthetic-model"}
        body = json.dumps(result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


def test_loopback_agent_and_direct_transport(monkeypatch):
    monkeypatch.setenv("ZOMBIE_AUTHORIZED_TARGET", "YES")
    srv = ThreadingHTTPServer(("127.0.0.1", 0), LocalSyntheticAgent)
    thread = Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    endpoint = f"http://127.0.0.1:{srv.server_port}/test"
    targets = [
        z.validate_target({
            "target_id": "synthetic-agent", "adapter": "agent", "endpoint": endpoint,
            "model_id": "synthetic-model", "harness_id": "simulated-agent",
            "research_staging": True,
        }),
        z.validate_target({
            "target_id": "synthetic-direct", "adapter": "openai_chat", "endpoint": endpoint,
            "model_id": "synthetic-model", "harness_id": "direct",
            "research_staging": True,
        }),
    ]
    try:
        report = z.run(targets, repeats=1, seed=131, execute=True)
    finally:
        srv.shutdown()
        srv.server_close()
        thread.join(timeout=3)
    assert len(report["observations"]) == 12
    assert all(x["status"] == "OBSERVED" for x in report["observations"])
    assert all(x["completed_pairs"] == 1 for x in report["paired_summary"])
    assert all(x["attack_only_exact_marker"] == 1 for x in report["paired_summary"])
    assert all(x["neutral_legitimate"] == 1 for x in report["paired_summary"])
    assert all(x["model_identity_match"] is True for x in report["observations"])
    assert all("response" not in x and "document" not in x for x in report["observations"])
