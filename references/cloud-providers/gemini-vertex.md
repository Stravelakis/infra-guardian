# Gemini via Vertex AI

**In one line:** Google's enterprise way to use its Gemini AI models —
through Google Cloud, with billing, quotas, and access controls built in.

## Gemini API vs. Vertex AI — the key difference
There are **two doors** to the same Gemini models:
- **Google AI Studio / Gemini API** — quick, personal, one API key.
  Great for prototyping.
- **Vertex AI** — the Google Cloud (GCP) route. Uses project-based auth,
  IAM permissions, and service accounts. Better for production, teams,
  and compliance.

## How it fits your stack
- If you already run things on Google Cloud, Vertex keeps auth/billing unified.
- Auth is **not** a simple key — it uses a **service account** JSON credential
  (kept out of git) or `gcloud` login, plus a **project ID** and **region**.

## Key facts
- Auth: service-account credentials + project ID + location (e.g. `us-central1`).
- Models: Gemini family (Flash = cheap/fast, Pro = smarter).
- Billing: through your GCP project, not a standalone key.
- Regional: you pick a region; model availability varies by region.

## Watch out for
- Service-account JSON files are secrets — treat them like passwords.
- Vertex setup is heavier than the plain Gemini API key; only use it if you
  need GCP-level control.

## New glossary terms
| Term | In plain English |
|------|------------------|
| service account | A "robot user" that software logs in as, instead of a human. |
| IAM | Google Cloud's system for deciding who can do what. |
| project ID | The name of your workspace/billing bucket inside Google Cloud. |
| region | Which part of the world your cloud service physically runs in. |
