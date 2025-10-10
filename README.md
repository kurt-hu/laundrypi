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

```
# Local development (initialize venv directory first if not present)
/home/pi/laundrypi/venv/bin/python3 /home/pi/laundrypi/app.py

# Production (restarts automatically): see /etc/systemd/system/laundrypiflask.service
sudo systemctl enable laundrypiflask.service
sudo systemctl start laundrypiflask.service
sudo systemctl status laundrypiflask.service
```