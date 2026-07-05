# OpenClaw

## In plain English
OpenClaw is an open-source AI agent framework (openclaw.ai) for building
autonomous, tool-using agents. NOTE: fast-moving project with limited stable
public docs — verify specifics against its own site. [[2]] [[8]]

## What it's used for
Running multi-step agentic tasks with tool/gateway integrations; considered a
predecessor/peer to Hermes Agent. [[4]]

## Where settings live
- Its config/env (model provider, gateway, tools).
- Provider keys as secrets.

## Safe-change checklist
- [ ] Sandbox it — agents can run commands / hit external APIs.
- [ ] Confirm gateway stability before trusting long tasks (a known pain point). [[4]]
- [ ] One tool integration at a time.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Task loops/stalls | Gateway instability | Check gateway/model conn [[4]] |
| No memory across runs | No persistence layer | Add/verify storage [[4]] |
| Tool call fails | Misconfigured integration | Test that tool alone |

## New terms → glossary
agent framework, gateway, tool call
