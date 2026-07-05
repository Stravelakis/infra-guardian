# Camoufox

## In plain English
Camoufox is a stealth/anti-detect build of Firefox aimed at automation and
scraping — patched to reduce browser fingerprinting.

## What it's used for
Bot-resistant browsing/automation (often driven via Playwright), fingerprint
and geolocation spoofing.

## Where settings live
- Launch options / config passed by your automation script.
- Any self-hosted service wrapping it → its own container env.

## Safe-change checklist
- [ ] Understand the legality/ToS of your target sites before use.
- [ ] Isolate in its own container/network.
- [ ] Change one fingerprint option at a time and verify.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Still detected | Fingerprint mismatch | Align UA/locale/timezone |
| Crashes on launch | Missing deps/headless setup | Check runtime deps |
| Slow/blocked | Proxy/rate issues | Verify proxy config |

## New terms → glossary
fingerprinting, anti-detect, headless browser
