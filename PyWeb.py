# pip install requests
#pip install beautifulsoup4
#pip install lxml
##<span class="table-ip4-home">  178.141.232.207     </span>
#ipinfo--location
import requests
import bs4

URL="https://www.iplocation.net/"

response=requests.get(URL)
html_data=response.text

soup =bs4.BeautifulSoup(html_data, features="lxml")
span_tag = soup.find("span", class_ = "table-ip4-home")
ip_address = span_tag.text
ip_address = ip_address.strip()
print(f"{ip_address=}")

span_tag = soup.find("span", class_ = "ipinfo--location")
ipinfo_location = span_tag.text
ipinfo_location = ipinfo_location.strip()
i=0
for sim in ipinfo_location:
    i=i+1
    if sim ==")":
        ipinfo_location=ipinfo_location[0:i]
        break
print(f"{ipinfo_location=}")




















