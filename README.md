# Python Security Toolkit: Automated Vulnerability Pipeline

A modular security tool designed to automate port scanning, service banner extraction, and vulnerability risk mapping.

## 🚀 Features
- **Network Scanning:** Identifies open ports on a target host.
- **Service Fingerprinting:** Grabs service banners to identify software versions.
- **Risk Mapping:** Matches banners against a custom vulnerability database.
- **Automated Reporting:** Generates a professional audit table.
- **Master Pipeline:** One-click execution using `run_all.py`.

## 🛠 File Overview
- `run_all.py`: The automation hub that runs the entire sequence.
- `scanner.py`: Performs port discovery.
- `grabber.py`: Handles banner extraction.
- `reporter.py`: Analyzes data and formats the final report.
- `banners.txt`: The data file where scan results are stored.

## 📈 How to Run
1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the master script:
   ```bash
   python run_all.py
