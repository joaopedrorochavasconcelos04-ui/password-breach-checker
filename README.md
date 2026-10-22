# 🔐 Password Breach Checker

> A fast, privacy-focused tool to check if a password has been exposed in data breaches without ever sending the full password over the internet.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Privacy First](https://img.shields.io/badge/privacy-k--anonymity-green)

---

![Demo GIF](https://via.placeholder.com/800x400.png?text=Demo+GIF+Placeholder) <!-- Replace with your actual GIF or image link -->

## 🛠️ How it works

Privacy comes first. This tool uses the **k-Anonymity** model provided by the Have I Been Pwned API to keep your real password safe during verification.

1. 🔒 **Local Hashing:** Your password is converted into a full SHA-1 hash locally.
2. ✂️ **Prefix Sharing:** Only the **first 5 characters** (prefix) of the hash are sent to the API.
3. 📦 **Suffix Fetching:** The API returns a list of matching hash suffixes along with how many times each hash appeared in known data breaches.
4. 💻 **Local Matching:** The script compares the full hash locally against the returned list to find a match. **Your plain password never leaves your machine.**

---

## 📊 What the number means (and doesn't)

- **What it means:** The count represents **historical exposure** in known data leaks.
- **What it doesn't mean:** It is **not** a measure of password strength or complexity. 
- ⚠️ **Important:** A count of **`0`** doesn't automatically mean your password is strong or unhackable—it simply means it has not been flagged in known data breaches yet.

---

## 🚀 Usage

### Prerequisites
- Python 3.8 or higher installed on your system.

### Quick Start

1. **Clone the repository and install dependencies:**
   ```bash
   pip install requests
   ```

2. **Run the checker:**
   ```bash
   python main.py
   ```

3. **Example Output:**
   ```text
   $ python main.py
   Enter password to check: **********

   ⚠️  WARNING: Password found! 
   This password has been exposed 4,210 times in known data breaches.
   Recommendation: Change this password immediately.
   ```

---

## 💡 What I learned

Building this project allowed me to deepen my understanding of practical cybersecurity principles:
- **k-Anonymity:** Learned how to query sensitive datasets safely without exposing client side identities or secrets.
- **Data Hashing:** Understood how standard hash functions like SHA-1 are used in cryptographic workflows.
- **REST APIs & Security:** Experienced consuming external APIs securely while handling edge cases and error responses cleanly.

---

## 🔮 Next steps

- [ ] Add a secure, customizable random password generator.
- [ ] Build a local brute-force demonstration tool (using harmless test passwords) to illustrate entropy and cracking speeds.
- [ ] Add support for checking passwords from a file in bulk (hashed locally).

---

Developed with 🔒 privacy in mind.
