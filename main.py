import os

LINE = "At 2am the fridge light clicks on like a courtroom lamp, and the leftover pizza testifies: 'Same guy, same crime, third night running.'"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
