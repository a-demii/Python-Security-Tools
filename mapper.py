VULN_DB = {
    "OpenSSH_6.6.1p1": "HIGH - This version is old and has known security leaks!",
    "OpenSSH_7.2": "MEDIUM - Outdated, update recommended.",
    "Apache/2.4": "LOW - Standard version, but keep an eye on it."
}

def check_vulnerabilities():
    print("--- Starting Vulnerability Analysis ---\n")

    file = open("banners.txt", "r")

    for line in file:
        clean_line = line.strip()
        found_match = False

        for version in VULN_DB:
            if version in clean_line:
                print(f"[!] RISK DETECTED: {clean_line}")
                print(f"    SEVERITY: {VULN_DB[version]}\n")
                found_match = True

        if not found_match:
            print(f"[-] No known risks found for: {clean_line}\n")
        
    file.close()

check_vulnerabilities()
