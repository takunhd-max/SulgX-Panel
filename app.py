import os
import runpy

if __name__ == "__main__":
    os.environ.setdefault("PORT", "5000")
    runpy.run_path("main.py", run_name="__main__")
