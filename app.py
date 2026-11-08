import os
import runpy

if __name__ == "__main__":
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("DOMAIN", "hedolllirpk.infrlo.com")
    runpy.run_path("main.py", run_name="__main__")
