VULN_DB = {
    "OpenSSH_6.6.1p1": "HIGH - This version is old and has known security leaks!",
    "OpenSSH_7.2": "MEDIUM - Outdated, update recommended.",
    "Apache/2.4": "LOW - Standard version, but keep an eye on it.",
    "vsFTPd 2.3.4": "CRITICAL - This version contains a famous backdoor (CVE-2011-2523)!",
    "Microsoft-IIS/7.5": "MEDIUM - Older Windows Server version. Check for MS15-034.",
    "SSH-2.0-OpenSSH_8.2": "LOW - Modern version. Just ensure it is patched.",
    "nginx/1.10.3": "MEDIUM - Outdated version of Nginx. Check for memory leak bugs."
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
