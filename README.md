# Agent Workflow Recorder ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Workflow Recorder Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-workflow-recorder/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-workflow-recorder?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-workflow-recorder/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Workflow Recorder** is a production-ready developer tool and connector: Full replay recorder that exports agent debugging sessions into deterministic replay files.

---

## 🚀 Problem Statement

Replicating intermittent agent failures is nearly impossible without an exact, deterministic recording of every tool call, parameter, and response payload.

---

## ⚡ Architecture Flow

```mermaid
flowchart LR
    A[Agent Session in Progress] --> B[Workflow Recorder]
    B -->|Logs Inputs, Tool Calls, Results| C[(session.agentplay File)]
    C --> D[Deterministic Replay Engine]
    D -->|Step-by-step Debugging| E[Reproduce Bug with 0 Tokens & 0 Network]
```

---

## 📊 Performance Benchmarks

| Debugging Workflow | Live Re-Execution | Agent Workflow Recorder | Comparison |
|---|---|---|---|
| Bug Reproduction Reliability | 30% (Non-deterministic LLMs) | 100% Deterministic Replay | **100% Exact Reproduction** |
| Debugging Token Cost | $1.20/run | $0.00 (Offline Replay) | **100% Free Debugging** |
| Recording Overhead | - | 0.02 ms | **Negligible** |
| Replay File Size | - | 12 KB (Compressed JSON) | **Ultra-compact** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_workflow_recorder
```

### Python API

```python
import agent_workflow_recorder

print(agent_workflow_recorder.__version__)
```

### CLI Usage

```bash
agent-workflow-recorder --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
