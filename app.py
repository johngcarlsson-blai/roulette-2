import os
from voila.app import Voila

# Create Voila instance
voila_app = Voila.instance()

# Set up Voila's launch arguments to disable the browser and expose the server
voila_args = [
    "--no-browser",  # Do not open a browser (headless server mode)
    "--strip_sources=False",  # Keep code visible in the dashboard
    "main.ipynb"  # Replace with the name of your notebook
]

# Launch Voila instance
voila_app.initialize(voila_args)

# Start the Voila server (this will bind to localhost initially)
voila_app.start()
