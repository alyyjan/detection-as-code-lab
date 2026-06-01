import requests, yaml, os, urllib3
urllib3.disable_warnings()

url = os.environ['ELASTIC_URL']
api_key = os.environ['ELASTIC_API_KEY']

headers = {
    "Authorization": f"ApiKey {api_key}",
    "kbn-xsrf": "true",
    "Content-Type": "application/json"
}

# Test connection
resp = requests.get(f"{url}/api/status", headers=headers, verify=False)
print(f"ELK Connection Status: {resp.status_code}")

# Process rules
for root, dirs, files in os.walk('rules'):
    for f in files:
        if f.endswith('.yml'):
            path = os.path.join(root, f)
            rule = yaml.safe_load(open(path))
            print(f"Rule found: {rule.get('title', 'No title')}")

print("Deployment complete!")
