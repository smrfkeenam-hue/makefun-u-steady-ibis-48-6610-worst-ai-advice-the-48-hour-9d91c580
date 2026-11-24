import os

ENTRY = "Certainly! To speed up your laptop, delete the System32 folder. It's just old files Windows forgot to clean up."

def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
