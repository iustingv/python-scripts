# python-scripts

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![boto3](https://img.shields.io/badge/boto3-aws--sdk-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Small Python utilities and AWS **boto3** practice scripts.  
All scripts are **safe by default** (DryRun or read-only) unless noted.

---

## Prerequisites
- Python 3.9+
- (For AWS scripts) An AWS account with credentials configured:
  - Run `aws configure`  
  - Or export environment variables:  
    `AWS_PROFILE`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`

---

## Setup

**Linux/macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip -r requirements.txt

# Configure AWS once:
aws configure

# Or use environment variables instead:
# export AWS_PROFILE=default
# export AWS_DEFAULT_REGION=us-east-1

---

## Scripts

- **list_ec2.py** — List EC2 instances (ID, name, state, type, region).  
- **ec2_toggle_by_tag.py** — Start/stop EC2 instances by tag (DryRun by default; use `--apply` to execute).  
- **ec2_usage_tracker.py** — Track EC2 uptime and export results to `ec2_report.csv`.  
- **list_buckets.py** — Show all S3 buckets.  
- **wordcount.py** — Print the top 10 most common words in a file.  
- **fetch_http.py** — Fetch a URL and show status code + snippet.  
- **hello.py / basics.py** — Simple Python CLI and file-handling practice.

---

## Notes
- AWS actions are non-destructive by default. Use `--apply` for real changes.  
- Repo ignores virtualenvs, caches, and generated files (`.gitignore`).  
- License: MIT.  
- Developed as part of a **Cloud / DevOps learning roadmap**.

