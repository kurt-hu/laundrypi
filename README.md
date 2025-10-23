# LaundryPi - SvelteKit + Flask Application

A Raspberry Pi application that monitors laundry status with a web interface built using SvelteKit and Flask.

## Architecture

- **Frontend**: SvelteKit static site served by Flask
- **Backend**: Flask API with GPIO sensor integration
- **Deployment**: Tailscale tunnel for public HTTPS access

## Setup

### Prerequisites

- Python 3.x with pip
- Node.js and npm
- Raspberry Pi with GPIO access

### Installation

1. **Create Virtual Environment** (recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/macOS
# or
venv\Scripts\activate    # On Windows
```

2. **Python Dependencies**

```bash
pip install -r requirements.txt
```

3. **Frontend Dependencies**

```bash
cd web
npm install
```

4. **Build Frontend**

```bash
cd web
npm run build
```

### Development

1. **Start Flask Server**

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On Linux/macOS
# or
source venv\Scripts\activate    # On Windows (bash)

python app.py
```

2. **Frontend Development** (optional)

```bash
cd web
npm run dev
```

## API Endpoints

- `GET /` - SvelteKit frontend
- `GET /api/status` - Application status
- `GET /api/health` - Health check
- `GET /api/dryer` - Dryer sensor status

## Public HTTPS server

https://raspberrypi.pleco-pain.ts.net/

# How to connect

```
ssh pi@raspberrypi.local
ssh root@raspberrypi
```

# Deploying

### First time setup

This should only need to be run once. Docs: https://tailscale.com/kb/1311/tailscale-funnel#effects-of-rebooting-and-restarting

```
# Tunnel command, run in background
tailscale funnel --bg --https=443 8000

# See tunnel status
tailscale status

# To disable proxy
tailscale funnel --https=443 off
```

### Running server

```bash
# Local development
# Create and activate virtual environment if not already done
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py

# Production (restarts automatically): see /etc/systemd/system/laundrypiflask.service
sudo systemctl enable laundrypiflask.service
sudo systemctl start laundrypiflask.service
sudo systemctl status laundrypiflask.service
```
