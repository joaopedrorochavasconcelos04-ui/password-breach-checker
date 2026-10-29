import hashlib
import json
import os
import time
import urllib.error
import urllib.request


def check_password_api(password):
    password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    url = f"https://api.pwnedpasswords.com/range/{password_hash[:5]}"
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        return {"status": "error", "error_code": error.code}

    for line in response_text.split():
        suffix, count = line.split(":")
        if suffix == password_hash[5:]:
            return {"status": "success", "breach_count": int(count)}

    return {"status": "success", "breach_count": 0}


# --- MAIN MENU ---
print("=========================================")
print("Password Breach Checker:")
print("1 - Batch check (TXT file)")
print("2 - Single password check")
print("=========================================")

option = input("Choose an option (1 or 2): ").strip()

# Guard clause: invalid menu choice
if option not in ("1", "2"):
    print(json.dumps({"error": "Invalid menu choice"}, indent=4))
    exit()

# --- FLOW 1: BATCH CHECK ---
if option == "1":
    filename = input("Enter the file name (e.g. sample_passwords.txt): ").strip()

    # Guard clauses
    if not filename:
        print(json.dumps({"error": "The file name cannot be empty"}, indent=4))
        exit()

    if not os.path.exists(filename):
        print(json.dumps({"error": f"File '{filename}' was not found"}, indent=4))
        exit()

    # Store the results that will be serialized as JSON
    final_result = {
        "verification_type": "batch",
        "source_file": filename,
        "results": {}
    }

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            password = line.strip()
            if not password:
                continue

            result = check_password_api(password)

            # Use each password as the key in the results object
            if result["status"] == "success":
                final_result["results"][password] = {
                    "exposed": result["breach_count"] > 0,
                    "count": result["breach_count"]
                }
            else:
                final_result["results"][password] = {
                    "error": f"API request failed (status {result['error_code']})"
                }

            time.sleep(0.5)

    # Serialize and print the final result as formatted JSON
    json_output = json.dumps(final_result, indent=4)
    print("\n--- OUTPUT JSON ---")
    print(json_output)

# --- FLOW 2: SINGLE PASSWORD CHECK ---
elif option == "2":
    password = input("Enter the password to check: ")

    # Guard clause
    if not password:
        print(json.dumps({"error": "No password was entered"}, indent=4))
        exit()

    result = check_password_api(password)

    single_result = {
        "verification_type": "single",
        "password_checked": password,
        "exposed": result.get("breach_count", 0) > 0 if result["status"] == "success" else "error",
        "count": result.get("breach_count", 0) if result["status"] == "success" else 0
    }

    print("\n--- OUTPUT JSON ---")
    print(json.dumps(single_result, indent=4))
