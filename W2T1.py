import requests as req
r = req.get('https://www.youtube.com/watch?v=WQeoO7MI0Bs')
print(r.text)
