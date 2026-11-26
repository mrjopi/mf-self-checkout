"""Entry for make.fun "The Self-Checkout Is Judging You" (u-motasimfuad-the-self-checkout-is-judging-you-b71130d6).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'Unexpected item in the bagging area: your dignity. Please remove it and try scanning your choices again.'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
