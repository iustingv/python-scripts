import argparse
p = argparse.ArgumentParser()
p.add_argument("--name", default="world")
a = p.parse_args()
print(f"Hello, {a.name}!")
