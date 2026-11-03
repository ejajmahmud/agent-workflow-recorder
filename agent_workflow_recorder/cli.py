"""Command-line interface for Agent Workflow Recorder."""
import argparse
from .recorder import WorkflowRecorder

def main():
    parser = argparse.ArgumentParser(description="Agent Workflow Recorder CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate session recording and offline replay")
    args = parser.parse_args()

    rec = WorkflowRecorder("sess_prod_42")
    rec.record_step("user_input", "Please fix database schema")
    rec.record_step("tool_call", {"tool": "db_query", "query": "SELECT *"})
    rec.record_step("tool_result", {"rows": 42})

    saved = rec.export_recording()
    print("Exported Session Recording snippet:")
    print(saved[:150] + "\n...")

    replayed = WorkflowRecorder.replay(saved)
    print(f"Replayed {len(replayed)} deterministic steps offline.")

if __name__ == "__main__":
    main()
