import requests, json, sys, argparse
# running via time command on linux gave
# me results somewhat fast on average
# real	0m0.426s
# user	0m0.068s
# sys	  0m0.020s

# cat:119, 226, 209 infotxt:140, 213, 124 dits:99,206,232 Core:165, 166, 179

banner = """    \x1b[0;38;2;0;102;204m▘  ▄▖        
    \x1b[0;38;2;30;122;214m▌▛▌▌▌▌▌█▌▛▘▌▌
    \x1b[0;38;2;60;142;224m▌▙▌█▌▙▌▙▖▌ ▙▌
    \x1b[0;38;2;90;162;234m ▌  ▘      ▄▌
    \x1b[0;38;2;120;182;244m
    \x1b[0m"""

headers = {
    "Host": "ipinfo.io",
    "Connection": "keep-alive",
    "DNT": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Referer": "https://ipinfo.io/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

def iplookup(response):
    if response.status_code == 200:
        data = response.json()

        ip = data["data"].get("ip", "N/A")
        hostname = data["data"].get("hostname", "N/A")
        city = data["data"].get("city", "N/A")
        region = data["data"].get("region", "N/A")
        country = data["data"].get("country", "N/A")
        loc = data["data"].get("loc", "N/A")
        org = data["data"].get("org", "N/A")
        postal = data["data"].get("postal", "N/A")
        timezone = data["data"].get("timezone", "N/A")

        asn = data["data"].get("asn", {})
        company = data["data"].get("company", {})
        privacy = data["data"].get("privacy", {})
        abuse = data["data"].get("abuse", {})

        print("   \x1b[0;38;2;165;166;179mInfo")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mIP             \x1b[0;38;2;140;213;124m", ip)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mHostname       \x1b[0;38;2;140;213;124m", hostname)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mCity           \x1b[0;38;2;140;213;124m", city)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mRegion         \x1b[0;38;2;140;213;124m", region)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mCountry        \x1b[0;38;2;140;213;124m", country)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mLocation       \x1b[0;38;2;140;213;124m", loc)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mOrganization   \x1b[0;38;2;140;213;124m", org)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mPostal Code    \x1b[0;38;2;140;213;124m", postal)
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mTimezone       \x1b[0;38;2;140;213;124m", timezone)
        print("   \x1b[0;38;2;165;166;179mASN")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mASN Number     \x1b[0;38;2;140;213;124m", asn.get("asn", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mASN Name       \x1b[0;38;2;140;213;124m", asn.get("name", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mASN Domain     \x1b[0;38;2;140;213;124m", asn.get("domain", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mASN Route      \x1b[0;38;2;140;213;124m", asn.get("route", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mASN Type       \x1b[0;38;2;140;213;124m", asn.get("type", "N/A"))
        print("   \x1b[0;38;2;165;166;179mCompany")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mCompany Name   \x1b[0;38;2;140;213;124m", company.get("name", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mCompany Domain \x1b[0;38;2;140;213;124m", company.get("domain", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mCompany Type   \x1b[0;38;2;140;213;124m", company.get("type", "N/A"))
        print("   \x1b[0;38;2;165;166;179mServices")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mVPN            \x1b[0;38;2;140;213;124m", privacy.get("vpn", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mProxy          \x1b[0;38;2;140;213;124m", privacy.get("proxy", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mTor            \x1b[0;38;2;140;213;124m", privacy.get("tor", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mRelay          \x1b[0;38;2;140;213;124m", privacy.get("relay", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mHosting        \x1b[0;38;2;140;213;124m", privacy.get("hosting", "N/A"))
        print("   \x1b[0;38;2;165;166;179mAbuse Report")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Address  \x1b[0;38;2;140;213;124m", abuse.get("address", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Country  \x1b[0;38;2;140;213;124m", abuse.get("country", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Email    \x1b[0;38;2;140;213;124m", abuse.get("email", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Name     \x1b[0;38;2;140;213;124m", abuse.get("name", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Network  \x1b[0;38;2;140;213;124m", abuse.get("network", "N/A"))
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mAbuse Phone    \x1b[0;38;2;140;213;124m", abuse.get("phone", "N/A"))
    else:
        print("   \x1b[0;38;2;165;166;179mError!")
        print("    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209mPlease enter a valid IP address.")

def main():
  if len(sys.argv) != 2:
      print(f"➥ \x1b[0;38;2;128;128;128mUsage    {sys.argv[0]} <ip>") # support for ipv6 soon
      sys.exit(1)
  
  ip_address = sys.argv[1]
  ipinfo_url = f"https://ipinfo.io/widget/demo/{ip_address}"

  try:
      response = requests.get(ipinfo_url, headers=headers)
      print(banner)
      iplookup(response)
  except requests.RequestException as e:
      print(" \x1b[0;38;2;255;255;255m➡ Network Error")
      print(f"    \x1b[0;38;2;255;255;255m ➥ \x1b[0;38;2;119;226;209m\x1b[0;38;2;119;226;209m{e}")

if __name__ == "__main__":
    main()
