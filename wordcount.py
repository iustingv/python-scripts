import argparse, collections, pathlib, re
p = argparse.ArgumentParser()
p.add_argument("path")
a = p.parse_args()
text = pathlib.Path(a.path).read_text(encoding="utf-8").lower()
words = re.findall(r"\b[\w']+\b", text)
for w, c in collections.Counter(words).most_common(10):
    print(f"{w}: {c}")
