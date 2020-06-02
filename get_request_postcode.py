import requests

path = 'http://api.postcodes.io/postcodes/'
argument = 'wd79lb'
target_url = path + argument

print(target_url)

response = requests.get(target_url)

print(response)
print(type(response))

print(response.json())

response_dict = response.json()
print(type(response_dict))


result_dict = response_dict['result']
print(result_dict)

for key in result_dict.keys():
    print(key.title(), '- the value inside this key is:', result_dict[key])