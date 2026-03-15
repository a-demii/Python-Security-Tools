VULN_DB = {
    "OpenSSH_6.6.1p1": "HIGH - This version is old and has known security leaks!",
    "OpenSSH_7.2": "MEDIUM - Outdated, update recommended.",
    "Apache/2.4": "LOW - Standard version, but keep an eye on it.",
    "vsFTPd 2.3.4": "CRITICAL - This version contains a famous backdoor (CVE-2011-2523)!",
    "Microsoft-IIS/7.5": "MEDIUM - Older Windows Server version. Check for MS15-034.",
    "SSH-2.0-OpenSSH_8.2": "LOW - Modern version. Just ensure it is patched.",
    "nginx/1.10.3": "MEDIUM - Outdated version of Nginx. Check for memory leak bugs."
}

def generate_report():
    print("\n" + "="*95)
    print(" " * 30 + "CYBER-PROJECT SECURITY REPORT")
    print("="*95)
    print(f"{'TARGET IP':<20} | {'SERVICE BANNER':<45} | {'RISK LEVEL'}")
    print("-" * 95)

    try:
        with open("banners.txt", "r") as file:
            for line in file:
                if ":" in line:
                    ip, banner = line.strip().split(":", 1)
                    ip = ip.strip()
                    banner = banner.strip()

                    risk = "CLEAN / UNKNOWN"
                    for key in VULN_DB:
                        if key in banner:
                            risk = VULN_DB[key]
                    
                    print(f"{ip:<15} | {banner:<15} | {risk}")
  
    except FileNotFoundError:
        print("Error: banner.txt not found. Run the grabber first!")

    print("="*50)
    print("End of Report\n")

if __name__ == "__main__":
    generate_report()