import requests

url = "https://kaashiv.com"  # Corrected URL
try:
    page = requests.get(url)
    print(page.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
