import requests

# Have this deployed on pythonanywhere 
request = requests.get('https://thisisfortestingpurposes.pythonanywhere.com/')
data = request.join()

print(data)