# python-scripts

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![boto3](https://img.shields.io/badge/boto3-aws--sdk-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Small Python utilities + AWS boto3 practice scripts.  
All scripts are **safe by default** (DryRun or read-only), making this repository portfolio-ready.

---

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip -r requirements.txt
    aws configure   # set AWS access key, secret, region (e.g., us-east-1)

---

## Notes

- Requires configured AWS credentials.  
- ⚠️ Safe by default — destructive actions use DryRun unless `--apply` is passed.

---

## License

MIT

