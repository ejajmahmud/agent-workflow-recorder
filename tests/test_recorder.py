"""Unit tests for WorkflowRecorder."""
import unittest
from agent_workflow_recorder.recorder import WorkflowRecorder

class TestWorkflowRecorder(unittest.TestCase):
    def test_record_and_replay(self):
        rec = WorkflowRecorder("s1")
        rec.record_step("prompt", "hi")
        rec.record_step("response", "hello")

        exported = rec.export_recording()
        events = WorkflowRecorder.replay(exported)
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["payload"], "hi")

if __name__ == "__main__":
    unittest.main()
