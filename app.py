import os
from voila.app import Voila

# Create Voila instance
voila_app = Voila()

# Set Voila configuration options
voila_app.root_dir = os.getcwd()  # Set root directory
voila_app.launch_instance(argv=["--no-browser", "--port=8866", "--strip_sources=False", "main.ipynb"])
