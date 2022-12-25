import requests

def check_website_status(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return "Website is up and running"
    else:
      return "Website is down"
  except:
    return "Error checking website status"

num_websites = int(input("How many websites do you want to check? "))
websites = []

for i in range(num_websites):
  website = input(f"Enter the URL for website #{i+1}: ")
  websites.append(website)

for website in websites:
  print(f"Checking status of {website}:")
  status = check_website_status(website)
  print(status)
