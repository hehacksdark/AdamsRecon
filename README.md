# AdamsRecon
**A Comprehensive Subdomain Enumeration Script** - *Inspired by Heath Adams (TCM Security) and the PJPT course*

AdamsScan is an automated subdomain enumeration script that utilizes multiple popular tools and APIs like Sublist3r, Amass, Subfinder, Findomain, crt.sh and TheHarvester. It helps security researchers discover subdomains, gather valuable information, and streamline passive reconnaissance for security assessments. Designed during TCM Security's PJPT training, this tool streamlines early-stage penetration testing workflows.  

Note: Before using AdamsRecon, ensure that you have the latest versions of all required tools installed. Keeping these tools up to date ensures optimal performance and compatibility with the script.  

# ✨ Features

![image](https://github.com/user-attachments/assets/a4da7c55-e804-4ba4-ad0f-f17d2003e459)

## Integrated Tool Suite: 
- Combines 6+ reconnaissance tools  
- Smart Validation: Auto-filter subdomains belonging to target  
- Multi-Data Extraction: IPs, Emails, ASNs, and more  
- API Integration: Supports 14+ TheHarvester data sources  
- Live Subdomain Verification: Powered by httpx  
- Color-Coded Workflow: Easy-to-read terminal output  
- Custom Parsing: Organized output structure  

## Usage
```sh
cd AdamsRecon
```
```sh
chmod +x adamsrecon.py
```
```sh
./AdamsRecon.py
```

## Prerequisites & Required System Tools:
AdamsRecon requires Python **3.6 or higher** to run.  

# 🛠 Installation
Run the following command to install the latest version:
```sh
git clone https://github.com/hehacksdark/AdamsRecon.git
```
## Install dependencies
```sh
sudo apt install python3-pip git
```
## Install required tools
```sh
pip3 install sublist3r theHarvester httpx findomain amass
```
```sh
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Workflow
1. Enter target domain (e.g., example.com)
2. Select tools (comma-separated numbers)
3. Configure API keys if using TheHarvester
4. Review results in /subdomains directory

## Output Files
- combined_subdomains.txt: All validated subdomains
- live_subdomains.txt: Verified active domains
- TheHarvester Data:  
                    - theharvester_emails.txt  
                    - theharvester_ips.txt  
                    - theharvester_asns.txt

# 🔧 Configuration
## API Keys (Optional)

Set environment variables for TheHarvester integrations:

![image](https://github.com/user-attachments/assets/dcbaf7d4-0b98-4f7b-8d92-49bee522a334)

```sh
# Example for Shodan
export SHODAN_API_KEY="your_key_here"
```
See full list in [Configuration Guide](Configuration.md)

## 📂 Output Structure
📦 results/  
├── 📄 combined_subdomains.txt  
├── 📄 live_subdomains.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 subdomains/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 amass.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 sublist3r.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 subfinder.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 findomain.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 theharvester_*.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── 📄 crtsh.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    └── 📄 cleaned.txt  

## 🤝 Contributing  
1. Fork the repository  
2. Push branch (git push origin feature/improvement)  
3. Open Pull Request  

## ⚠️ Disclaimer
**Use Responsibly!** This tool is for:  

- Authorized penetration testing  
- Educational purposes  
- Security research  
- Developers assume no liability for unauthorized/malicious use.  

## 📜 License  
GNU General Public License v1.0

# What’s next? 🚀
I’m already working on AdamsRecon Version 1.1, which will include:

- **New Tools:** WaybackURL and a tool to capture screenshots of subdomain pages.  
- **Interactive Features:** Customizable commands and options for each selected tool.
- **Even more structured output:** Better data categorization for deeper insights 

Stay tuned for the update! It's coming soon, and I can't wait to share it with you. 🛠️

# 🙏 Acknowledgments
- Heath Adams/TCM Security for inspiration
- Open-source tool maintainers:
   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Sublist3r by @aboul3la.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subfinder by ProjectDiscovery.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - TheHarvester   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Amass by OWASP  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Findomain by @Edu4rdSHL.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - httpx by ProjectDiscovery.  
