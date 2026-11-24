<p align="center">
  <img src="assets/logos/a_sleek_neon_tech_banner_identical_to_the_given_la.png" alt="NEXA project banner" width="100%">
</p>

<h1 align="center">NEXA-SLM — Semantic Intelligence Model</h1>
<p align="center"><strong>Specialized Programming Intent Reasoning</strong></p>
<p align="center">ONE INTENTION. MULTIPLE PROGRAMMING LANGUAGES.</p>

Part of the NextGenAI Infinity ecosystem.

## Overview

NEXA-SLM is a local-first hybrid semantic intelligence system designed to interpret developer intentions expressed in natural language, identify programming concepts and keywords, and provide technically compatible implementations across programming languages and technologies.

Its purpose is not merely to generate code, but to explain how and why each implementation works.

**Status: Project Foundation v0.1.0 — architecture and draft contracts, not yet runnable.**

## Architecture

Human intent → keywords → semantic interpretation → typed IR → compatibility → language adapters → validation → token-level explanations.

- Local small language model (SLM), combined with deterministic semantic rules and a versioned knowledge base.
- Comparative syntax dictionary, reserved words, operators, and programming concepts.
- Compatibility classification distinguishing native support, runtime APIs, libraries, frameworks, indirect implementations and unsupported or unknown operations.
- Syntax highlighting, copyable code examples and instruction-by-instruction explanations.
- Syntax, semantic and security validation; planned ScriptGuard integration.
- Offline installation and inference; no mandatory external AI API.
- Model selection, benchmarking, packaging and specialization are pending.

## Documentation

- [Architecture](docs/architecture/ARCHITECTURE.md)
- [Mandatory UX requirements](docs/ux/REQUIREMENTS.md)
- [Security](docs/security/THREAT_MODEL.md)
- [Local-first design decision](docs/decisions/0001-local-first.md)
- [Roadmap](docs/development/ROADMAP.md)

Never invent unsupported equivalents or execute generated code automatically. The model proposes; the deterministic engine validates; the human decides.

---

<p align="center"><em>AI assists. Human verifies. Human decides.</em></p>
<p align="center"><strong>THERE IS NO FINAL VERSION. THERE IS ONLY EVOLUTION.</strong></p>
