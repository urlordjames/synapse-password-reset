import requests

token = input("auth token:\n")

user = input("matrix user id:\n")
password = input("password:\n")

headers = {"Authorization": "Bearer " + token}

url = f"https://jamesvps.tk/_synapse/admin/v1/reset_password/{user}"

params = {
	"new_password": password,
	"logout_device": True
}

r = requests.post(url, json=params, headers=headers)

print(r.status_code)
print(r.text)
