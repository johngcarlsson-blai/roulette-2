import os
import subprocess

notebook_path = "main.ipynb"  # Update this to your notebook path if needed
port = os.getenv("PORT", 8000)

# Run Voila as a subprocess
subprocess.run(["voila", notebook_path, "--port", str(port), "--no-browser", "--strip_sources=False"])
