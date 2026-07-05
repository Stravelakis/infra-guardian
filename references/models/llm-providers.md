# LLM Providers — Free-Tier Cheat Sheet

Only the providers this stack uses, with a focus on their free/no-cost paths.
⚠️ Free-tier limits change often. Always confirm current quotas on the
provider's own pricing/limits page before relying on them.

| Provider   | Free path (how you get in)                          | Typically good for            | Notes |
|------------|-----------------------------------------------------|-------------------------------|-------|
| Groq       | Free API key, generous rate-limited free tier       | Very fast inference, testing  | Watch per-minute token/request caps. |
| Gemini     | Free key via Google AI Studio                       | General reasoning, long context | AI Studio tier is separate from paid Vertex. |
| Mistral    | Free "La Plateforme" experimental tier              | Cheap general use             | Some models free, some paid-only. |
| Cerebras   | Free tier via Cerebras Inference                    | High-speed responses          | Rate-limited; check daily caps. |
| NVIDIA     | Free credits via build.nvidia.com (NIM)             | Trying hosted open models     | Credit-based, not unlimited. |
| OpenRouter | Free tier; some models tagged ":free"               | One key, many models          | Free models are rate-limited and can rotate. |

## OpenRouter specifics
OpenRouter offers a free tier and exposes certain models with a `:free`
suffix that route to no-cost endpoints [[1]]. Because it's OpenAI-API
compatible, you can point most tools at it with a single key.

## Practical guidance for free usage
- **Never assume "free" = "unlimited."** Every provider above rate-limits.
- **Keep one key per provider in `.env`**, never in these reference files.
- **Free tiers are for dev/testing.** For anything user-facing or scheduled,
  expect to hit limits and plan a paid fallback.
- **Model availability on free tiers rotates** — a `:free` model today may be
  paid or gone next month. Don't hard-code names in scripts without a fallback.
