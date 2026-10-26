# 🛡️ DevSecOps Pipeline Threat Model

**Methodology:** Supply Chain Levels for Software Artifacts (SLSA) & STRIDE

### Key Attack Vectors Mitigated:
1. **Secret Leakage:** GitLeaks prevents accidental credential commits directly at PR creation.
2. **IaC Misconfiguration:** Checkov halts pipelines if unencrypted storage, open SSH (port 22), or public S3/Blob containers are introduced.
3. **Budget Runaway:** Infracost Python gate prevents accidental provision of expensive GPU or compute tiers without explicit VP signoff.