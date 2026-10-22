<div align="center">
🔒 Password Breach Checker
A command-line tool that checks whether a password has appeared in known data breaches, using the Have I Been Pwned "Pwned Passwords" API.
The password itself is never sent: only the first 5 characters of its SHA-1 hash leave your machine.
</div>
---
🎬 Demo
(Add your GIF or screenshot here)
---
⚙️ How it works
The tool uses k-anonymity, a technique that lets you query the API without revealing what you are looking for.
Local hashing: the password is converted to a SHA-1 hash on your machine.
Prefix only: the first 5 characters of the hash (the prefix) are sent to the API.
Suffix list: the API returns every hash suffix that starts with that prefix, along with how many times each one appeared in breaches.
Local matching: the script compares the rest of your hash against that list locally. The password and the full hash are never sent.
---
📊 What the number means (and doesn't)
It is the number of times that exact password appeared in known data breaches. It measures historical exposure.
It does not measure strength or complexity. A long, complex password can show up in a breach if a service that stored it was compromised.
A count of 0 does not mean the password is safe. It only means it was not found in the breaches the API knows about.
Any count above 0 is a good reason to stop using that password.
---
🚀 Usage
Requires Python 3.x and the requests library.
```bash
git clone https://github.com/joaopedrorochavasconcelos04-ui/password-breach-checker.git
cd password-breach-checker
pip install requests
python main.py
```
The script asks for a password (the input is masked) and prints how many times it was found in known breaches. A result of 0 means it was not found.
While testing, use throwaway passwords such as `password123`, never a real one.
---
💡 What I learned
k-anonymity in practice: splitting the hash with `h[:5]` and `h[5:]` so the API never sees which password I am checking.
Small details matter: the API expects the hash in uppercase, so the `.upper()` call is required for the match to work.
Testing before coding: I called the API in Postman first to understand the response format before writing any Python.
Hashing with hashlib: a string has to be encoded to bytes before it can be hashed.
A note on SHA-1: it is considered weak for security today. Here it is used only because the API requires it, not as a security choice.
---
⚠️ Known limitations
Network errors and unexpected API responses are not handled yet.
It checks one password at a time.
---
📌 Next steps
[ ] Add a secure password generator.
[ ] Add a brute-force demonstration using only test passwords defined in the code, to show why length and variety matter.
[ ] Add error handling for network failures.
[ ] Check passwords from a file in bulk.
---
📝 Credits and disclaimer
Built with the free Pwned Passwords API from Have I Been Pwned. This is an educational project and does not replace a password maneger.
