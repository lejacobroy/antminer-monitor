import urllib.request
import re
import gzip

f = urllib.request.urlopen("http://10.66.10.63:8081/metrics")
res = gzip.decompress(f.read())

result = re.search('model="(.*)",os_version',res.decode('utf-8'))
print(result.group(1))