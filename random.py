
import urllib.request
x="12345"
y=""
for i in range(1):
    request_url = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={y}')
    x = str(request_url.read())
    y=x[len(x)-2:len(x)-7:-1]
print(y)