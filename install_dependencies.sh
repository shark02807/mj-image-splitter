#!/bin/bash

# Install Python and pip (if not already installed)
if ! command -v python &>/dev/null; then
    echo "Python not found. Installing Python..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! command -v pip &>/dev/null; then
    echo "pip not found. Installing pip..."
    sudo apt-get install -y python3-pip
fi

# Install required Python packages
echo "Installing required Python packages..."
pip install requests Pillow

echo "Dependencies installation complete."
