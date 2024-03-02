from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(selector=".titleline > a:first-child")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)

print(article_texts[max_index])
print(article_links[max_index])
print(max_upvote)
# print(article_upvotes)
#based on the Hacker News page of ycombinator on 03rd March 2024


import smtplib
import time

#Enter your email address and password
MY_EMAIL = ""
MY_PASSWORD = ""

while True:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject: Top Voted On Hacker News!!!\n\n{article_texts[max_index]}\n\n{article_links[max_index]}"
        )
    time.sleep(3600)