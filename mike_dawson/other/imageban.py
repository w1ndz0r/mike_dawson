import requests, base64

with open("velosiped.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

client_key = "pQP0y1XUyfBcNzQ7Or8G"
secret_key = "5rt7rEV2PZn1QkoO2QiYlOpFmhJ2uX5qfpn"
api_url = 'https://api.imageban.ru/v1'
#image_url = 'https://2ch.pm/mo/src/171410/14885707382530.jpg'
header = {'Authorization: TOKEN': client_key}

#data = {'secret_key': secret_key, 'url': image_url}
data = {'secret_key': secret_key, 'image': encoded_image}

r = requests.post(api_url, headers=header, data=data)


short_link = r.json().get('data').get('short_link')

print(short_link)