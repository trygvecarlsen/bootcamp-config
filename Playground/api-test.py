import http.client

conn = http.client.HTTPSConnection("ice-cream-factory.inso-internal.cognite.ai")
payload = ''
headers = {}
conn.request("GET", "/site/all", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
