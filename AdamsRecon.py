#!/usr/bin/env python3
import os
import json
import re
import subprocess
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def display_banner():
    banner = """
 █████╗ ██████╗  █████╗ ███╗   ███╗███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
███████║██║  ██║███████║██╔████╔██║███████╗    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══██║██║  ██║██╔══██║██║╚██╔╝██║╚════██║    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║  ██║██████╔╝██║  ██║██║ ╚═╝ ██║███████║    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                               Version 1.0
    """
    print(banner)
    print("Coded By Shivam Sharma - @hehacksdark")
# Call this function to display the banner
display_banner()


# Colors for visibility
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
END = "\033[0m"

TOOLS = {
    "1": {"name": "Sublist3r", "command": "sublist3r -d {target} -o subdomains/sublist3r.txt"},
    "2": {"name": "Subfinder", "command": "subfinder -d {target} -silent"},
    "3": {"name": "crt.sh", "command": "custom"},
    "4": {"name": "Amass", "command": "amass enum -passive -d {target}"},
    "5": {"name": "Findomain", "command": "findomain -t {target} -q"},
    "6": {"name": "TheHarvester", "command": "custom"}
}

THE_HARVESTER_APIS = {
    "1": {"name": "Bing", "env": "BING_API_KEY"},
    "2": {"name": "GitHub", "env": "GITHUB_API_KEY"},
    "3": {"name": "Shodan", "env": "SHODAN_API_KEY"},
    "4": {"name": "Censys", "envs": ["CENSYS_API_ID", "CENSYS_API_SECRET"]},
    "5": {"name": "SecurityTrails", "env": "SECURITYTRAILS_API_KEY"},
    "6": {"name": "VirusTotal", "env": "VIRUSTOTAL_API_KEY"},
    "7": {"name": "Hunter.io", "env": "HUNTER_API_KEY"},
    "8": {"name": "Intelx", "env": "INTELX_API_KEY"},
    "9": {"name": "Netlas", "env": "NETLAS_API_KEY"},
    "10": {"name": "AlienVault OTX", "env": "OTX_API_KEY"},
    "11": {"name": "Urlscan", "env": "URLSCAN_API_KEY"},
    "12": {"name": "ZoomEye", "env": "ZOOMEYE_API_KEY"},
    "13": {"name": "Certspotter", "env": "CERTSPOTTER_API_KEY"},
    "14": {"name": "Spyse", "env": "SPYSE_API_KEY"}
}

def is_valid_subdomain(domain, target):
    """Check if domain is a valid subdomain of target"""
    domain = domain.lower().strip()
    target = target.lower().strip()
    pattern = r'^([a-z0-9-]+\.)*' + re.escape(target) + r'$'
    return re.match(pattern, domain) is not None

def run_crtsh(target):
    """Query crt.sh with proper domain filtering"""
    subs = set()
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://crt.sh/?q=%25.{target}&output=json"
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            try:
                data = response.json()
                for entry in data:
                    for name in entry["name_value"].split('\n'):
                        cleaned = name.strip().lower()
                        if is_valid_subdomain(cleaned, target):
                            subs.add(cleaned)
            except json.JSONDecodeError:
                return ""
    except Exception as e:
        return ""
    return "\n".join(sorted(subs))

def parse_theharvester_output(target):
    """Parse TheHarvester output into separate files"""
    output_file = Path(f"subdomains/theharvester.txt")
    if not output_file.exists():
        return

    sections = {
        "subdomains": [],
        "ips": [],
        "emails": [],
        "asns": [],
        "hosts": [],
        "others": []
    }
    
    current_section = None
    with open(output_file, "r") as f:
        for line in f:
            line = line.strip()
            
            # Detect section headers
            if line.startswith("[*] Hosts found:"):
                current_section = "subdomains"
            elif line.startswith("[*] IPs found:"):
                current_section = "ips"
            elif line.startswith("[*] Emails found:"):
                current_section = "emails"
            elif line.startswith("[*] ASNs found:"):
                current_section = "asns"
            elif line.startswith("[*] Tweets found:") or line.startswith("[*] Interesting URLs found:"):
                current_section = "others"
            elif line and current_section:
                # Clean and validate data
                cleaned = line.split(':', 1)[-1].strip() if ':' in line else line
                if current_section == "subdomains" and is_valid_subdomain(cleaned, target):
                    sections["subdomains"].append(cleaned)
                elif current_section == "ips" and re.match(r"^\d+\.\d+\.\d+\.\d+$", cleaned):
                    sections["ips"].append(cleaned)
                elif current_section == "emails" and '@' in cleaned:
                    sections["emails"].append(cleaned)
                elif current_section == "asns" and cleaned.startswith("AS"):
                    sections["asns"].append(cleaned)
    
    # Save to separate files
    for category, data in sections.items():
        if data:
            with open(f"subdomains/theharvester_{category}.txt", "w") as f:
                f.write("\n".join(sorted(set(data))))

def run_tool(tool, target):
    """Execute a subdomain enumeration tool"""
    print(f"{YELLOW}\n[*] Running {tool['name']}...{END}")
    try:
        if tool["name"] == "crt.sh":
            results = run_crtsh(target)
            with open("subdomains/crtsh.txt", "w") as f:
                f.write(results)
        
        elif tool["name"] == "TheHarvester":
            api_env = os.environ.copy()
            
            print(f"\n{CYAN}Available TheHarvester APIs:{END}")
            for num, api in THE_HARVESTER_APIS.items():
                print(f"  {num}. {api['name']}")
            
            selected_apis = input(f"{GREEN}[?] Select APIs to use or press enter (comma-separated, e.g., 1,3): {END}").strip().split(",")
            
            for num in selected_apis:
                if num in THE_HARVESTER_APIS:
                    api_info = THE_HARVESTER_APIS[num]
                    if "envs" in api_info:
                        for env_var in api_info["envs"]:
                            key = input(f"{GREEN}[?] Enter {api_info['name']} {env_var}: {END}").strip()
                            if key:
                                api_env[env_var] = key
                    else:
                        key = input(f"{GREEN}[?] Enter {api_info['name']} API key: {END}").strip()
                        if key:
                            api_env[api_info["env"]] = key
            
            # Run TheHarvester
            cmd = f"theHarvester -d {target} -b all -f subdomains/theharvester.txt"
            subprocess.run(
                cmd, 
                shell=True,
                env=api_env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Parse output
            parse_theharvester_output(target)
        
        else:
            cmd = tool["command"].format(target=target)
            output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
            with open(f"subdomains/{tool['name'].lower()}.txt", "w") as f:
                f.write(output)
    
    except Exception as e:
        print(f"{RED}[!] {tool['name']} failed: {str(e)}{END}")

def filter_and_clean(target):
    """Validate all subdomains and remove invalid entries"""
    valid_subs = set()
    output_dir = Path("subdomains")
    
    for tool_file in output_dir.glob("*.txt"):
        # Skip TheHarvester's parsed files except subdomains
        if "theharvester_" in tool_file.name and tool_file.name != "theharvester_subdomains.txt":
            continue
        with open(tool_file, "r") as f:
            for line in f:
                candidate = line.strip()
                if is_valid_subdomain(candidate, target):
                    valid_subs.add(candidate.lower())
    
    with open("subdomains/cleaned.txt", "w") as f:
        f.write("\n".join(sorted(valid_subs)))
    
    return len(valid_subs)

def main():
    target = input(f"{GREEN}[+] Enter target domain (e.g., example.com): {END}").strip()
    print(f"\n{CYAN}Available tools:{END}")
    for num, tool in TOOLS.items():
        print(f"  {num}. {tool['name']}")
    
    selected = input(f"\n{GREEN}[?] Select tools (comma-separated, e.g., 1,3,5): {END}").strip().split(",")
    
    # Setup directories
    output_dir = Path("subdomains")
    output_dir.mkdir(exist_ok=True)
    
    # Clear previous results
    for f in output_dir.glob("*.txt"):
        f.unlink()
    
    # Run selected tools
    for num in selected:
        if num in TOOLS:
            run_tool(TOOLS[num], target)
    
    # Filter and clean results
    print(f"{YELLOW}\n[*] Validating results...{END}")
    valid_count = filter_and_clean(target)
    
    # Combine results
    combined_path = Path("combined_subdomains.txt").resolve()
    live_path = Path("live_subdomains.txt").resolve()
    
    print(f"{YELLOW}[*] Combining results...{END}")
    os.system(f"cat subdomains/cleaned.txt | sort -u > {combined_path}")
    
    print(f"{YELLOW}[*] Checking live subdomains...{END}")
    os.system(f"httpx -l {combined_path} -status-code -title -silent -o {live_path}")
    
    print(f"\n{GREEN}[+] Results saved in:{END}")
    print(f"- {combined_path}")
    print(f"- {live_path}")
    print(f"{CYAN}Additional TheHarvester data in subdomains/:{END}")
    print("- theharvester_ips.txt")
    print("- theharvester_emails.txt")
    print("- theharvester_asns.txt")

if __name__ == "__main__":
    main()
