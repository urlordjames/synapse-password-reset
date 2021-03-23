import requests

def reset_passwd(hostname, token, user, password):
	headers = {"Authorization": "Bearer " + token}
	
	url = f"https://{hostname}/_synapse/admin/v1/reset_password/{user}"
	
	params = {
		"new_password": password,
		"logout_device": True
	}
	
	r = requests.post(url, json=params, headers=headers)
	return r

if __name__ == "__main__":
	hostname = input("hostname:\n")
	token = input("auth token:\n")
	uname = input("username to reset password of:\n")
	user = f"@{uname}:{hostname}"
	password = input("password:\n")

	r = reset_passwd(hostname, token, user, password)
	
	print(r.status_code)
	print(r.text)
