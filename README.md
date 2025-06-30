# ipQuery

**ipQuery** is a IP lookup tool that surpasses the limitations of IPInfo.io's official CLI. It provides extended information on IP addresses without requiring an API key making it good for developers, sysadmins, and network enthusiasts who need a quick lookup without the need to pay for an ipinfo apikey. You can also strip the print statements and use the json data for your own applications. 

## Features

* Retrieve detailed info about any IP address
* No API key required
* Faster and more informative than IPInfo.io's CLI
* Outputs include:

  * Location (city, region, country)
  * ISP/ASN
  * Coordinates
  * Reverse DNS (when available)
  * Etc.

## Installation

Clone the repo and make the script executable:

```bash
git clone https://github.com/deangelo-png/ipQuery && cd ipQuery && sudo bash install.sh
```

## Usage

Basic usage:

```bash
./ipQuery <ip-address>
```

Or, if you installed it globally:

```bash
ipquery <ip-address>
```

Example:

```bash
ipquery 8.8.8.8
```

You can also run it without an argument to get info about your own public IP:

```bash
ipquery
```

## Dependencies

* `curl`
* `jq` (for JSON parsing)

## API-Free

Unlike most IP lookup tools online, **ipQuery** leverages the old ipinfo demo widget api so you can use it as much as you like without worrying about rate limits.

## ✅ Example Output

```bash
    ▘  ▄▖        
    ▌▛▌▌▌▌▌█▌▛▘▌▌
    ▌▙▌█▌▙▌▙▖▌ ▙▌
     ▌  ▘      ▄▌
    
    
   Info
     ➥ IP              1.1.1.1
     ➥ Hostname        one.one.one.one
     ➥ City            Brisbane
     ➥ Region          Queensland
     ➥ Country         AU
     ➥ Location        -27.4816,153.0175
     ➥ Organization    AS13335 Cloudflare, Inc.
     ➥ Postal Code     4101
     ➥ Timezone        Australia/Brisbane
   ASN
     ➥ ASN Number      AS13335
     ➥ ASN Name        Cloudflare, Inc.
     ➥ ASN Domain      cloudflare.com
     ➥ ASN Route       1.1.1.0/24
     ➥ ASN Type        hosting
   Company
     ➥ Company Name    APNIC and Cloudflare DNS Resolver project
     ➥ Company Domain  cloudflare.com
     ➥ Company Type    hosting
   Services
     ➥ VPN             False
     ➥ Proxy           False
     ➥ Tor             False
     ➥ Relay           False
     ➥ Hosting         True
   Abuse Report
     ➥ Abuse Address   PO Box 3646, South Brisbane, QLD 4101, Australia
     ➥ Abuse Country   AU
     ➥ Abuse Email     helpdesk@apnic.net
     ➥ Abuse Name      ABUSE APNICRANDNETAU
     ➥ Abuse Network   1.1.1.0/24
     ➥ Abuse Phone     +000000000
```

## Contributing

Pull requests are welcome, If you have suggestions for improvements or additional features, open an issue or submit a PR.
