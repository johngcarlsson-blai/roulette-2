import os
from voila.app import Voila

# Create Voila instance
voila_app = Voila()

# Set Voila configuration options
voila_app.root_dir = os.getcwd()  # Set root directory
port = int(os.getenv("PORT", 8000))  # Get the port from the environment
host = "0.0.0.0"  # Bind to the external interface

# Launch Voila and bind to 0.0.0.0
voila_app.launch_instance(argv=[f"--port={port}", f"--ip={host}", "--strip_sources=False", "main.ipynb"])
