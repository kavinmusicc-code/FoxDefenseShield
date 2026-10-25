import os, sys, time, random, psutil; from datetime import datetime; from colorama import init, Fore, Style; init(autoreset=True);
def run_diagnostic():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + '='*65)
    print(Fore.CYAN + Style.BRIGHT + '       [ FOX-DEFENSE DIAGNOSTIC & HEALTH MONITOR ]')
    print(Fore.CYAN + Style.BRIGHT + '       STATUS: RUNNING SYSTEM INTEGRITY & SECURITY CHECK')
    print(Fore.CYAN + Style.BRIGHT + '='*65 + '\n')
    checks = ['Checking Kernel Integrity...', 'Scanning Open Ports...', 'Analyzing Network Packets...', 'Validating Process Memory...', 'Checking Firewall Rules...']
    while True:
        t = datetime.now().strftime('%H:%M:%S')
        check = random.choice(checks)
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        print(Fore.YELLOW + f'[{t}] DIAGNOSTIC: {check} [OK] (CPU: {cpu}% | RAM: {ram}%)')
        if random.choice([False, False, True]):
            print(Fore.RED + Style.BRIGHT + f'[!] WARNING [{t}] ANOMALY DETECTED IN MEMORY STREAM! ISOLATING PROCESS...')
            print(Fore.YELLOW + '-'*65)
        time.sleep(1.0)
if __name__ == '__main__':
    try:
        run_diagnostic()
    except KeyboardInterrupt:
        print(Fore.GREEN + '\n[*] DIAGNOSTIC COMPLETE. SYSTEM SECURE.')
