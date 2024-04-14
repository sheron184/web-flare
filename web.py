# Sample App
# Import app class
from system.app import app
# Create app obj with hostname and port
myapp = app('localhost', 7200)
# Serve app
myapp.serve()

# access app on http://localhost:7200