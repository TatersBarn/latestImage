#!/bin/bash

# Check if python3 command is available
if command -v python3 &>/dev/null; then
    python3 latest_image_server.py
else
    echo "Python 3 is required but not found. Please install Python 3."
    exit 1
fi

