import os
import subprocess
import sys


def main():
    print("=" * 65)
    print("TgFlow PyPI Upload Tool")
    print("=" * 65)

    dist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dist"))
    if not os.path.isdir(dist_dir) or not os.listdir(dist_dir):
        print(f"Error: No distribution files found in {dist_dir}.")
        print("Run: python -m build")
        sys.exit(1)

    print("Distribution packages found:")
    for f in os.listdir(dist_dir):
        print(f"  - {f}")
    print("-" * 65)

    mode = input("Upload to TestPyPI first? (Y/n): ").strip().lower()
    use_test = not (mode == "n")

    cmd = [sys.executable, "-m", "twine", "upload"]
    if use_test:
        cmd += ["--repository", "testpypi"]
    cmd.append(os.path.join(dist_dir, "*"))

    print("\nExecuting command:")
    print(" ".join(cmd))
    print("=" * 65)
    print("Twine will prompt for your PyPI API token (__token__ / pypi-...).")
    print("=" * 65)

    try:
        subprocess.run(cmd, check=True)
        print("\n[SUCCESS] TgFlow uploaded to PyPI successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Upload exited with code {e.returncode}")
    except KeyboardInterrupt:
        print("\nUpload cancelled.")


if __name__ == "__main__":
    main()
