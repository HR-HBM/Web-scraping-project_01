# from bs4 import BeautifulSoup
# import requests
#
#
# response = requests.get("https://news.ycombinator.com/news")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# articles = soup.select(selector=".titleline > a:first-child")
#
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# max_upvote = max(article_upvotes)
# max_index = article_upvotes.index(max_upvote)
#
# print(article_texts[max_index])
# print(article_links[max_index])
# print(max_upvote)
# # print(article_upvotes)
# #based on the Hacker News page of ycombinator on 03rd March 2024
#
#
# import smtplib
# import time
#
#
# MY_EMAIL = "humaihr469@gmail.com"
# MY_PASSWORD = "ffpymukxgqbmnkrh"
#
# while True:
#     connection = smtplib.SMTP("smtp.gmail.com", 587)
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=MY_EMAIL,
#         msg=f"Subject: Top Voted On Hacker News!!!\n\n{article_texts[max_index]}\n\n{article_links[max_index]}"
#         )
#     time.sleep(3600)

# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import time
#
# # ----------------------------------------
# # SCRAPE HACKER NEWS TOP 15
# # ----------------------------------------
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# # Select all articles
# articles = soup.select(".titleline > a:first-child")
# scores = soup.find_all("span", class_="score")
#
# article_texts = []
# article_links = []
# article_upvotes = []
#
# for i, article_tag in enumerate(articles):
#     if i >= 15:  # only top 15
#         break
#
#     title = article_tag.getText()
#     link = article_tag.get("href")
#
#     # Find upvotes
#     next_row = article_tag.parent.parent.find_next_sibling("tr")
#
#     if next_row:
#         score_tag = next_row.select_one(".score")
#         score = int(score_tag.getText().split()[0]) if score_tag else 0
#     else:
#         score = 0
#
#     article_texts.append(title)
#     article_links.append(link)
#     article_upvotes.append(score)
#
# # Format email body for all top 15
# email_body = "Top 15 Hacker News Posts:\n\n"
#
# for i in range(15):
#     email_body += f"{i+1}. {article_texts[i]}\n"
#     email_body += f"   {article_links[i]}\n"
#     email_body += f"   Upvotes: {article_upvotes[i]}\n\n"
#
# print(email_body)
#
# # ----------------------------------------
# # SEND EMAIL (use your APP PASSWORD here)
# # ----------------------------------------
#
# # MY_EMAIL = "xxxx@gmail.com"
# # MY_APP_PASSWORD = "your_16_char_app_password_here"  # NOT your real Gmail password
#
# MY_EMAIL = "humaihr469@gmail.com"
# MY_PASSWORD = "ffpymukxgqbmnkrh"
#
# from email.message import EmailMessage
#
# while True:
#     msg = EmailMessage()
#     msg["Subject"] = "Top 15 Hacker News Stories"
#     msg["From"] = MY_EMAIL
#     msg["To"] = MY_EMAIL   # sending to yourself
#     msg.set_content(email_body)   # UTF-8 safe
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.send_message(msg)
#
#     time.sleep(3600)











#
#
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import time
# from email.message import EmailMessage
#
# from dotenv import load_dotenv
# import os
#
# # ----------------------------------------------------
# # SCRAPE HACKER NEWS — TOP 15
# # ----------------------------------------------------
# def scrape_hacker_news():
#     response = requests.get("https://news.ycombinator.com/news")
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     articles = soup.select(".titleline > a:first-child")
#
#     article_texts = []
#     article_links = []
#     article_upvotes = []
#
#     for i, article_tag in enumerate(articles):
#         if i >= 15:
#             break
#
#         title = article_tag.getText()
#         link = article_tag.get("href")
#
#         next_row = article_tag.parent.parent.find_next_sibling("tr")
#
#         # if next_row:
#         #     score_tag = next_row.select_one(".score")
#         #     score = int(score_tag.getText().split()[0]) if score_tag else 0
#         # else:
#         #     score = 0
#
#         article_texts.append(title)
#         article_links.append(link)
#         # article_upvotes.append(score)
#
#     # Build formatted section
#     hn_body = "Top 15 Hacker News Posts:\n\n"
#     for i in range(15):
#         hn_body += f"{i+1}. {article_texts[i]}\n"
#         hn_body += f"   {article_links[i]}\n"
#         # hn_body += f"   Upvotes: {article_upvotes[i]}\n\n"
#
#     return hn_body
#
#
# # ----------------------------------------------------
# # SCRAPE FT SECTIONS
# # ----------------------------------------------------
# FT_PAGES = {
#     "FT Technology": "https://www.ft.com/technology",
#     "FT Markets": "https://www.ft.com/markets",
#     "FT World": "https://www.ft.com/world",
#     "FT Companies": "https://www.ft.com/companies",
# }
#
# def scrape_ft_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     results = []
#
#     ul = soup.find("ul", class_="o-teaser-collection__list")
#     if not ul:
#         return results
#
#     li_items = ul.find_all("li", class_="o-teaser-collection__item")
#
#     for li in li_items:
#
#         # Skip premium articles
#         if li.find("div", class_="x-teaser__premium-label"):
#             continue
#
#         a_tag = li.find("a", class_="js-teaser-heading-link")
#         if not a_tag:
#             continue
#
#         title = a_tag.get_text(strip=True)
#         link = a_tag.get("href")
#
#         # Fix relative URLs
#         if link.startswith("/"):
#             link = "https://www.ft.com" + link
#
#         results.append((title, link))
#
#     return results
#
#
# # Build FT email sections
# def build_ft_body():
#     body = ""
#     for section_name, url in FT_PAGES.items():
#         articles = scrape_ft_page(url)
#
#         body += f"{section_name}:\n\n"
#         for title, link in articles:
#             body += f"- {title}\n  {link}\n"
#         body += "\n\n"
#
#     return body
#
#
# # ----------------------------------------------------
# # COMBINE EVERYTHING INTO ONE EMAIL
# # ----------------------------------------------------
# hn_section = scrape_hacker_news()
# ft_section = build_ft_body()
#
# email_body = hn_section + "\n" + ft_section
#
# print(email_body)  # For debugging
#
#
# # ----------------------------------------------------
# # SEND EMAIL (UTF-8 SAFE)
# # ----------------------------------------------------
#
#
#
#
# load_dotenv()
#
# MY_EMAIL = os.getenv("MY_EMAIL")
# MY_PASSWORD = os.getenv("MY_PASSWORD")
#
# def send_email():
#     msg = EmailMessage()
#     msg["Subject"] = "Daily News Digest — HN + FT"
#     msg["From"] = MY_EMAIL
#     msg["To"] = MY_EMAIL
#     msg.set_content(email_body)
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.send_message(msg)
#
#
# # ----------------------------------------------------
# # RUN EVERY HOUR (your automation loop)
# # ----------------------------------------------------
# send_email()
# print("Email sent successfully. Program completed and exiting...")


















import requests
from bs4 import BeautifulSoup

url = "https://www.reuters.com/world/"
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
print(html[:2000])
















#
#
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# from email.message import EmailMessage
# from dotenv import load_dotenv
# import os
#
# # ----------------------------------------------------
# # SCRAPE HACKER NEWS — TOP 15
# # ----------------------------------------------------
# def scrape_hacker_news():
#     response = requests.get("https://news.ycombinator.com/news")
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     articles = soup.select(".titleline > a:first-child")
#
#     article_texts = []
#     article_links = []
#
#     for i, article_tag in enumerate(articles):
#         if i >= 15:
#             break
#
#         title = article_tag.getText()
#         link = article_tag.get("href")
#
#         article_texts.append(title)
#         article_links.append(link)
#
#     # Build formatted section
#     hn_body = "🔶 Top 15 Hacker News Posts:\n\n"
#     for i in range(15):
#         hn_body += f"{i+1}. {article_texts[i]}\n"
#         hn_body += f"   {article_links[i]}\n\n"
#
#     return hn_body
#
#
# # ----------------------------------------------------
# # GENERIC REUTERS SCRAPER
# # (extracts all <a> inside headline divs)
# # ----------------------------------------------------
# def scrape_reuters_page(url, section_name):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     results = []
#
#     # All Reuters headline links share this div + link class
#     headline_divs = soup.find_all("div", class_="title-module__title__Lr6MH")
#
#     for div in headline_divs:
#         a_tag = div.find("a")
#         if not a_tag:
#             continue
#
#         title = a_tag.get_text(strip=True)
#         link = a_tag.get("href")
#
#         # Fix relative URLs
#         if link.startswith("/"):
#             link = "https://www.reuters.com" + link
#
#         results.append((title, link))
#
#     # Build section text
#     body = f"🔷 {section_name}:\n\n"
#     for title, link in results:
#         body += f"- {title}\n  {link}\n"
#     body += "\n\n"
#
#     return body
#
#
# # ----------------------------------------------------
# # SCRAPE REUTERS TECHNOLOGY / SCIENCE / BUSINESS
# # ----------------------------------------------------
# def scrape_reuters_all():
#     pages = {
#         "Reuters Technology": "https://www.reuters.com/technology/",
#         "Reuters Science": "https://www.reuters.com/science/",
#         "Reuters Business": "https://www.reuters.com/business/",
#     }
#
#     combined = ""
#     for name, url in pages.items():
#         combined += scrape_reuters_page(url, name)
#
#     return combined
#
#
# # ----------------------------------------------------
# # COMBINE EVERYTHING INTO ONE EMAIL
# # ----------------------------------------------------
# hn_section = scrape_hacker_news()
# reuters_section = scrape_reuters_all()
#
# email_body = hn_section + "\n" + reuters_section
#
# print(email_body)
#
#
# # ----------------------------------------------------
# # SEND EMAIL
# # ----------------------------------------------------
# load_dotenv()
#
# MY_EMAIL = os.getenv("MY_EMAIL")
# MY_PASSWORD = os.getenv("MY_PASSWORD")
#
# def send_email():
#     msg = EmailMessage()
#     msg["Subject"] = "Daily News Digest — HN + Reuters"
#     msg["From"] = MY_EMAIL
#     msg["To"] = MY_EMAIL
#     msg.set_content(email_body)
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.send_message(msg)
#
#
# # ----------------------------------------------------
# # RUN ONCE AND EXIT
# # ----------------------------------------------------
# send_email()
# print("Email sent successfully. Program completed and exiting...")
