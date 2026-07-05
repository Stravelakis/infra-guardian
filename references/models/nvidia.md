# NVIDIA NIM (build.nvidia.com)

## In plain English
NVIDIA's hosted model endpoints (NIM microservices), OpenAI-compatible.

## What it's used for
Access to a broad model catalogue; can also self-host NIM containers later.

## Where settings live
- API base: https://integrate.api.nvidia.com/v1
- Key: NVIDIA_API_KEY (.env, placeholder)
- guardian.config.yaml → model_providers.nvidia

## Safe-change checklist
- [ ] If self-hosting NIM: backup + checksum image tag before pull.
- [ ] Confirm GPU/driver reqs before any local NIM (doctor.py check).

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 401 | key/tier issue | check .env + account access |
| Model gated | preview access | request access, don't hardcode ID |

## New terms → glossary
- NIM (NVIDIA Inference Microservice)
