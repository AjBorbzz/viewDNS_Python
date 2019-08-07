import requests
""" tools available: 
    reverse_dns, traceroute, port_scan, propagation, record,
"""

base_url = 'https://api.viewdns.info/'
apikey = '<your API KEY>'
tool = 'reversedns'
url2 = f"&apikey={apikey}&output=json"

def reverse_dns(ip):
	reversedns_url = f"{base_url}reversedns/?ip={ip}"
	query = f"{reversedns_url}{url2}"
	return query

def traceroute(domain):
	traceroute_url = f"{base_url}traceroute/?domain={domain}"
	query = f"{traceroute_url}{url2}"
	return query

def port_scan(host):
	portscan_url = f"{base_url}portscan/?host={host}"
	query = f"{portscan_url}{url2}"
	return query

def dns_propagation(domain):
	propagation = f"{base_url}propagation/?domain={domain}"
	query = f"{propagation}{url2}"
	return query

def dns_record(domain, record_type='A'):
	dnsrecord = f"{base_url}dnsrecord/?domain={domain}"
	query = f"{dnsrecord}&recordtype={record_type}{url2}"
	return query

def whois(domain):
	""" Access is restricted to paid API keys only """

	whois_url = f"{base_url}whois/?domain={domain}"
	query = f"{whois_url}{url2}"
	return query

response = requests.get(reverse_dns('199.59.148.10'))
print(response.json())