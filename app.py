import os
from voila.app import Voila

# Create Voila instance
voila_app = Voila()

# Set Voila configuration options
voila_app.root_dir = os.getcwd()  # Set root directory
voila_app.port = int(os.getenv("PORT", 8000))  # Use the port from environment variable

# Serve the notebook
voila_app.launch_instance(argv=["--strip_sources=False", "main.ipynb"])
