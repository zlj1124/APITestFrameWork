import grequests

urls = [
    'http://192.168.3.21:18082',
    'http://192.168.3.19:18083',
    'http://192.168.3.21:18081',
   
]
rs = (grequests.get(u) for u in urls)
print grequests.map(rs)
