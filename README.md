# 🛡️ Enterprise DevSecOps Golden Pipeline

<div align="center">

[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Workflows-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Azure DevOps](https://img.shields.io/badge/Azure_Pipelines-YAML-0078D7?style=for-the-badge&logo=azure-devops&logoColor=white)](https://azure.microsoft.com/services/devops/pipelines/)
[![Security: GitLeaks](https://img.shields.io/badge/Secrets-GitLeaks_Active-red?style=for-the-badge&logo=github)](https://github.com/gitleaks/gitleaks)
[![Security: Checkov](https://img.shields.io/badge/IaC-Checkov_Enforced-brightgreen?style=for-the-badge&logo=bridgecrew)](https://www.checkov.io/)

**Standardized multi-cloud DevSecOps pipeline templates enforcing shift-left security (secrets, IaC compliance, container CVEs), FinOps cost caps, and dual-peer approval gates.**

[Threat Model](docs/threat-model.md) · [Operations Runbook](docs/operations-runbook.md) · [GitHub Actions](.github/workflows/golden-pipeline.yml) · [Azure DevOps YAML](azure-pipelines/azure-pipelines.yml)

</div>

---

## ⚡ Pipeline Stages & Flow

```mermaid
flowchart LR
    Commit["Commit / PR"] --> S1["1. GitLeaks Scan\n(Secret Hygiene)"]
    S1 --> S2["2. Checkov & Trivy\n(IaC & CVE Gate)"]
    S2 --> S3["3. FinOps Infracost\n(Delta Budget Guardrail)"]
    S3 --> S4["4. Dual-Peer Gate\n(Manual Sign-Off)"]
    S4 --> Deploy["5. Production Apply\n(Remote State Locked)"]
```

---

## 🚀 Quickstart & Usage

Include this pipeline in your microservice or IaC repositories by referencing the reusable workflow or copying `.github/workflows/golden-pipeline.yml`.

---

## 🤝 Maintained by
**Rushikesh Bonde** · Licensed under MIT.