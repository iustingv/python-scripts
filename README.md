### ec2_toggle_by_tag.py (read-only by design)

Demonstrates how to **find EC2 instances by tag** and run a **start/stop action** safely.

- Performs a **DryRun** by default (no changes made).
- If `--apply` is used but the IAM user has no permissions, it exits gracefully with:  
  *“ℹ️ Read-only mode: no permissions to start/stop. Matched instances shown above; no action taken.”*
- This makes it safe for demo/portfolio use — it shows AWS error-handling and IAM awareness without requiring destructive permissions.

**Required IAM permissions (read-only):**
- `ec2:DescribeInstances`
- (optional) `sts:GetCallerIdentity` to show which profile/region is being used

**Usage examples**
```bash
# DryRun only — lists instances and confirms permission check
python ec2_toggle_by_tag.py stop Name=Linux2-Training

# Attempt real apply — if no permissions, exits gracefully in read-only mode
python ec2_toggle_by_tag.py stop Name=Linux2-Training --apply

