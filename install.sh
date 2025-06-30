#!/bin/bash
set -e

cat << "EOF"
   ____         __       ____     __  _         
  /  _/__  ___ / /____ _/ / /__ _/ /_(_)__  ___ 
 _/ // _ \(_-</ __/ _ `/ / / _ `/ __/ / _ \/ _ \
/___/_//_/___/\__/\_,_/_/_/\_,_/\__/_/\___/_//_/
EOF

echo "Preparing to install ipquery..."

# Detect package manager
echo "Detecting package manager..."

if command -v pacman &> /dev/null; then
  PM="pacman"
  INSTALL="sudo pacman -S --noconfirm --needed python3 python-pip"
elif command -v apt &> /dev/null; then
  PM="apt"
  INSTALL="sudo apt install -y python3 python3-pip"
elif command -v dnf &> /dev/null; then
  PM="dnf"
  INSTALL="sudo dnf install -y python3 python3-pip"
elif command -v zypper &> /dev/null; then
  PM="zypper"
  INSTALL="sudo zypper install -y python3 python3-pip"
else
  echo "Unsupported or unknown package manager."
  exit 1
fi

echo "Using package manager: $PM"
echo "Ensuring Python 3 and pip are installed..."
$INSTALL

echo "Installing required Python packages..."
pip3 install --user requests

# Copy script and make executable
echo "Setting up ipquery..."

if [ ! -f "script.py" ]; then
  echo "Error: script.py not found in the current directory."
  exit 1
fi

chmod +x script.py
sudo cp script.py /bin/ipquery

echo "Installed 'ipquery' to /bin/ipquery"

# Usage Info
cat <<EOL

Usage:
  ipquery <IP_ADDRESS>       # Provide IP to query
  ipquery -a                 # Use the -a flag (if implemented)

Dependencies installed:
  - Python 3
  - requests (via pip)

You can now run:
  ipquery 1.1.1.1

EOL

echo "DONE."
