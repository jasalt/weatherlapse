#!/usr/bin/env python
# Run development server on local-machine
from app import app
print("Starting development server at localhost:5000")
app.run(port=5000, debug=True)  # host='0.0.0.0'
