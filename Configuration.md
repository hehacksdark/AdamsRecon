# AdamsRecon Configuration Guide ⚙️

## 📌 API Key Setup

To maximize AdamsRecon's capabilities with TheHarvester integration, configure these APIs:

---

### Table of Contents
1. [Bing](#-bing)
2. [GitHub](#-github)
3. [Shodan](#-shodan)
4. [Censys](#-censys)
5. [SecurityTrails](#-securitytrails)
6. [VirusTotal](#-virustotal)
7. [Hunter.io](#-hunterio)
8. [Intelx](#-intelx)
9. [Netlas](#-netlas)
10. [AlienVault OTX](#-alienvault-otx)
11. [Urlscan](#-urlscan)
12. [ZoomEye](#-zoomeye)
13. [Certspotter](#-certspotter)
14. [Spyse](#-spyse)

---

## 🔍 Bing
**Environment Variable:** `BING_API_KEY`
1. Create Microsoft Azure account
2. Create Cognitive Services resource
3. Get key from Azure Portal > Keys & Endpoint
```bash
export BING_API_KEY="your_azure_key"

```

---

## 🐙 GitHub
**Environment Variable:** `GITHUB_API_KEY`
1. Go to GitHub Settings > Developer Settings
2. Create Personal Access Token
3. Select `repo` and `read:org` scopes
```bash
export GITHUB_API_KEY="ghp_yourtokenhere"

```

---

## 👁️ Shodan
**Environment Variable:** `SHODAN_API_KEY`
1. Register at [shodan.io](https://www.shodan.io/)
2. Upgrade to paid account (free tier limited)
3. Find API key in Account Overview
```bash
export SHODAN_API_KEY="yourapikeyhere"

```

---

## 🔎 Censys
**Environment Variables:**
- `CENSYS_API_ID`
- `CENSYS_API_SECRET`
1. Create account at [censys.io](https://censys.io/)
2. Go to API Settings
3. Create new API credentials
```bash
export CENSYS_API_ID="your_id"
export CENSYS_API_SECRET="your_secret"

```

---

## 🛤️ SecurityTrails
**Environment Variable:** `SECURITYTRAILS_API_KEY`
1. Sign up at [securitytrails.com](https://securitytrails.com/)
2. Get API key from Dashboard
3. Free tier: 50 queries/month
```bash
export SECURITYTRAILS_API_KEY="yourapikey"

```

---

## 🦠 VirusTotal
**Environment Variable:** `VIRUSTOTAL_API_KEY`
1. Create account at [virustotal.com](https://www.virustotal.com/)
2. Get key from API tab
3. Free tier: 500 requests/day
```bash
export VIRUSTOTAL_API_KEY="yourkeyhere"

```

---

## 🎯 Hunter.io
**Environment Variable:** `HUNTER_API_KEY`
1. Register at [hunter.io](https://hunter.io/)
2. Get API key from Dashboard
3. Free tier: 50 searches/month
```bash
export HUNTER_API_KEY="hunterkey"

```

---

## 🕵️ Intelx
**Environment Variable:** `INTELX_API_KEY`
1. Create account at [intelx.io](https://intelx.io/)
2. Get API key from My Account
3. Free access limited
```bash
export INTELX_API_KEY="your_intelx_key"

```

---

## 🌐 Netlas
**Environment Variable:** `NETLAS_API_KEY`
1. Sign up at [netlas.io](https://netlas.io/)
2. Obtain API key from Profile
3. Free plan: 100 requests/day
```bash
export NETLAS_API_KEY="netlas_key"

```

---

## 👽 AlienVault OTX
**Environment Variable:** `OTX_API_KEY`
1. Register at [otx.alienvault.com](https://otx.alienvault.com/)
2. Get key from My Settings
3. Unlimited free access
```bash
export OTX_API_KEY="your_otx_key"

```

---

## 🔗 Urlscan
**Environment Variable:** `URLSCAN_API_KEY`
1. Create account at [urlscan.io](https://urlscan.io/)
2. Generate API key in Settings
3. Free tier: 100 scans/day
```bash
export URLSCAN_API_KEY="urlscan_key"

```

---

## 👁️ ZoomEye
**Environment Variable:** `ZOOMEYE_API_KEY`
1. Register at [zoomeye.org](https://www.zoomeye.org/)
2. Get API key from Profile
3. Free tier: 10,000 results/month
```bash
export ZOOMEYE_API_KEY="zoomeye_key"

```

---

## 📜 Certspotter
**Environment Variable:** `CERTSPOTTER_API_KEY`
1. Sign up at [sslmate.com](https://sslmate.com/)
2. Create API token
3. Free monitoring limited
```bash
export CERTSPOTTER_API_KEY="certspotter_key"

```

---

## 🕸️ Spyse
**Environment Variable:** `SPYSE_API_KEY`
1. Create account at [spyse.com](https://spyse.com/)
2. Get API key from Account
3. Free tier: 100 requests/month
```bash
export SPYSE_API_KEY="spyse_key"

```

---

## 🛡️ Security Best Practices
1. **Never commit API keys** to version control
2. Use environment variables temporarily:
```bash
# Temporary session-only usage
export API_KEY="yourkey" && ./adamsrecon.py
```
3. For permanent storage, add to shell config:
```bash
# ~/.bashrc or ~/.zshrc
export SPYSE_API_KEY="key"  # Add all your keys
```

---

## 🔧 Troubleshooting API Issues
- **Invalid Key Errors**: Verify key format and service subscription
- **Rate Limits**: Check service's API usage dashboard
- **No Results**: Confirm API-enabled data sources in TheHarvester selection
- **Connection Issues**: Verify firewall/proxy settings

*For detailed API documentation, refer to each service's official developer portal.*
