from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())
price_span = soup.find(class_="a-offscreen").getText()
price_witout_dollar= price_span.split("$")[1]
price_as_float= float(price_witout_dollar)
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
print(title)
BUY_PRICE = 100
if BUY_PRICE>price_as_float:
    message=f"{title}is now cheap"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result= connection.login("samrath163@gmail.com", "oxfc hfeh thnb ubdn")
        connection.sendmail(
            from_addr="samrath163@gmail.com",
            to_addrs="vartikabajpai9650@gmail.com",
            msg=f"subject:Amazon price alert!!\n\n{message}\n{url}".encode("utf-8")
        )



