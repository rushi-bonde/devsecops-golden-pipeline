# 📖 DevSecOps Operations Runbook

### Handling Security Scan Failures:
1. **GitLeaks Alert:** Immediately revoke and rotate any leaked credential. Do not just `git rebase` or delete the commit; assume compromised once pushed.
2. **Checkov Failure:** Review the violating line in the PR. If a business exemption is required, follow the formal Policy Exemption Process with ticket ID.