import requests
from bs4 import BeautifulSoup

def check_azure_status():
    url = "https://status.azure.com/en-us/status"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    services = soup.select(".status-banner .status-text")
    if not services:
        print("Could not retrieve service statuses.")
        return

    print("🔹 Azure Services Status:\n")
    for service in services:
        print(service.text.strip())

if __name__ == "__main__":
    check_azure_status()
