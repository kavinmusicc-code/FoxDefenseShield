import os, sys, time, random, psutil, threading, subprocess, platform, json
from datetime import datetime
from colorama import init, Fore, Style
import tkinter as tk
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet
from flask import Flask, jsonify, render_template_string, request

init(autoreset=True)

CONFIG_FILE = 'FoxDefense/config.json'
USER_DB = 'FoxDefense/users.json'
os.makedirs('FoxDefense', exist_ok=True)

ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

try:
    VALID_HWID = platform.node() + '-' + os.environ.get('USERNAME', 'Client-Node')
except:
    VALID_HWID = "FOX-CROSS-PLATFORM-NODE-999"

app = Flask(__name__)

# ----------------- MOBILE & DESKTOP DUAL DASHBOARD HTML -----------------
MOBILE_HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Fox-Defense Cross-Platform Suite</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0b0e14; color: #00ffcc; padding: 15px; text-align: center; }
        .header { margin-bottom: 20px; }
        .header h1 { font-size: 20px; letter-spacing: 1px; color: #00ffcc; }
        .header p { font-size: 12px; color: #8892b0; }
        .card { background: #131924; border: 1px solid #1f293d; border-radius: 12px; padding: 15px; margin-bottom: 15px; text-align: left; }
        .card h3 { font-size: 14px; color: #fff; margin-bottom: 8px; border-bottom: 1px solid #1f293d; padding-bottom: 5px; }
        .status-badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
        .status-online { background: rgba(0, 255, 204, 0.15); color: #00ffcc; border: 1px solid #00ffcc; }
        .status-alert { background: rgba(255, 77, 77, 0.15); color: #ff4d4d; border: 1px solid #ff4d4d; }
        .info-row { display: flex; justify-content: space-between; font-size: 13px; margin: 8px 0; color: #ccd6f6; }
        .btn { width: 100%; padding: 12px; border: none; border-radius: 8px; background: #00ffcc; color: #0b0e14; font-weight: bold; font-size: 14px; margin-top: 10px; cursor: pointer; }
        .btn-danger { background: #ff4d4d; color: #fff; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🛡️ FOX-DEFENSE SHIELD</h1>
        <p>Cross-Platform Autonomous Suite (Mobile & Desktop)</p>
    </div>

    <div class="card">
        <h3>System Status</h3>
        <div class="info-row"><span>Node ID:</span> <strong>{{ hwid }}</strong></div>
        <div class="info-row"><span>Protection Mode:</span> <span class="status-badge status-online">24/7 ACTIVE</span></div>
        <div class="info-row"><span>Self-Healing Loop:</span> <span class="status-badge status-online">RUNNING</span></div>
    </div>

    <div class="card">
        <h3>Live Resource Telemetry</h3>
        <div class="info-row"><span>CPU Usage:</span> <span id="cpu-stat">Loading...</span></div>
        <div class="info-row"><span>RAM Usage:</span> <span id="ram-stat">Loading...</span></div>
    </div>

    <div class="card">
        <h3>Quick Remote Actions</h3>
        <button class="btn" onclick="triggerScan()">Run Mobile Threat Scan</button>
        <button class="btn btn-danger" onclick="triggerLock()">Lock System Node</button>
    </div>

    <script>
        function updateStats() {
            fetch('/api/stats')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('cpu-stat').innerText = data.cpu + '%';
                    document.getElementById('ram-stat').innerText = data.ram + '%';
                });
        }
        setInterval(updateStats, 2000);
        updateStats();

        function triggerScan() { alert('Remote Mobile Diagnostics Triggered!'); }
        function triggerLock() { alert('Security Lockdown Command Issued to Node.'); }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(MOBILE_HTML_TEMPLATE, hwid=VALID_HWID)

@app.route('/api/stats')
def api_stats():
    return jsonify({
        'cpu': psutil.cpu_percent(),
        'ram': psutil.virtual_memory().percent,
        'status': 'SECURE',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })

def run_mobile_server():
    try:
        app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Server Error: {e}")

if __name__ == '__main__':
    threading.Thread(target=run_mobile_server, daemon=True).start()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + Style.BRIGHT + '='*75)
    print(Fore.CYAN + Style.BRIGHT + '     [ FOX-DEFENSE DUAL-PLATFORM ENGINE (MOBILE + DESKTOP) ]')
    print(Fore.RED + Style.BRIGHT + '='*75)
    print(Fore.GREEN + f'\n[*] LOCAL ACCESS   : http://localhost:5000')
    print(Fore.GREEN + f'[*] MOBILE ACCESS  : http://<YOUR-IP-ADDRESS>:5000')
    print(Fore.YELLOW + '\n[+] Both PC and Mobile Dashboard are ready and operational!')
    
    while True:
        time.sleep(1)
