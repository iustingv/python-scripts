import argparse, requests
p = argparse.ArgumentParser()
p.add_argument("url")
a = p.parse_args()
r = requests.get(a.url, timeout=10)
print("Status:", r.status_code)
print(r.text[:400])
