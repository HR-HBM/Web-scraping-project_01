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
# MY_EMAIL = ""
# MY_PASSWORD = ""
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
# # COMBINE INTO ONE EMAIL
# # ----------------------------------------------------
# hn_section = scrape_hacker_news()
#
# email_body = hn_section
#
# print(email_body)
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
#     msg["Subject"] = "Daily News Digest"
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


# from bs4 import BeautifulSoup
# import requests
# import smtplib
# from email.message import EmailMessage
# from dotenv import load_dotenv
# import os
# from playwright.sync_api import sync_playwright
# import time
# from datetime import datetime


# # ----------------------------------------------------
# # SCRAPE HACKER NEWS — TOP 10
# # ----------------------------------------------------
# def scrape_hacker_news():
#     response = requests.get("https://news.ycombinator.com/news")
#     soup = BeautifulSoup(response.text, "html.parser")

#     articles = soup.select(".titleline > a:first-child")

#     article_texts = []
#     article_links = []

#     for i, article_tag in enumerate(articles):
#         if i >= 10:
#             break

#         title = article_tag.getText()
#         link = article_tag.get("href")

#         article_texts.append(title)
#         article_links.append(link)

#     # Build formatted section
#     hn_body = "🔶 Top 10 Hacker News Posts:\n\n"
#     for i in range(10):
#         hn_body += f"{i + 1}. {article_texts[i]}\n"
#         hn_body += f"   {article_links[i]}\n\n"

#     return hn_body


# # ----------------------------------------------------
# # SCRAPE PRODUCT HUNT
# # ----------------------------------------------------
# def scrape_product_hunt():
#     try:
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=True)
#             context = browser.new_context(
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#             )
#             page = context.new_page()

#             print("Loading Product Hunt...")
#             page.goto("https://www.producthunt.com/", wait_until="domcontentloaded")

#             print("Waiting for content to load...")
#             page.wait_for_selector("div.flex.flex-col.gap-10", timeout=15000)

#             time.sleep(3)

#             content = page.content()
#             browser.close()

#             print("Parsing content...")
#             soup = BeautifulSoup(content, "html.parser")

#             main_div = soup.find("div", class_="flex flex-col gap-10")

#             if not main_div:
#                 print("Could not find main container")
#                 return "⚠️ Could not find Product Hunt content\n\n"

#             content_div = main_div.find("div", class_="flex flex-col")

#             if not content_div:
#                 print("Could not find content container")
#                 return "⚠️ Could not find Product Hunt content container\n\n"

#             sections = content_div.find_all("section",
#                                             class_=lambda x: x and "group relative isolate flex flex-row" in x)

#             print(f"Found {len(sections)} sections")

#             product_texts = []
#             product_links = []

#             for section in sections:
#                 flex_div = section.find("div", class_="flex min-w-0 flex-1 flex-col")
#                 if flex_div:
#                     text_div = flex_div.find("div", class_=lambda x: x and "text-16 font-semibold" in x)
#                     if text_div:
#                         link_tag = text_div.find("a")
#                         if link_tag:
#                             title = link_tag.get_text(strip=True)
#                             link = link_tag.get("href")

#                             if link and link.startswith("/"):
#                                 link = f"https://www.producthunt.com{link}"

#                             product_texts.append(title)
#                             product_links.append(link)

#             if len(product_texts) == 0:
#                 print("No products found")
#                 return "⚠️ No products found on Product Hunt\n\n"

#             print(f"Successfully scraped {len(product_texts)} products")
#             ph_body = "🚀 Product Hunt Featured Products (Today's Trending):\n\n"
#             for i in range(len(product_texts)):
#                 ph_body += f"{i + 1}. {product_texts[i]}\n"
#                 ph_body += f"   {product_links[i]}\n\n"

#             return ph_body

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return f"⚠️ Error scraping Product Hunt: {str(e)}\n\n"


# # ----------------------------------------------------
# # COMBINE INTO ONE EMAIL
# # ----------------------------------------------------
# print("Starting scraping process...")
# ph_section = scrape_product_hunt()
# hn_section = scrape_hacker_news()

# email_body = ph_section + "\n" + hn_section

# print("\n" + "=" * 60)
# print("EMAIL PREVIEW:")
# print("=" * 60)
# print(email_body)
# print("=" * 60 + "\n")

# # ----------------------------------------------------
# # SEND EMAIL
# # ----------------------------------------------------
# load_dotenv()

# SENDER_EMAIL = os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


# def send_email():
#     today = datetime.now().strftime("%B %d, %Y")

#     msg = EmailMessage()
#     msg["Subject"] = f"Daily News Digest - {today}"
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = RECIPIENT_EMAIL
#     msg.set_content(email_body)

#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(SENDER_EMAIL, SENDER_PASSWORD)
#         connection.send_message(msg)


# # ----------------------------------------------------
# # RUN ONCE AND EXIT
# # ----------------------------------------------------
# send_email()
# print("Email sent successfully. Program completed and exiting...")




from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright
import time
from datetime import datetime

# ----------------------------------------------------
# SCRAPE HACKER NEWS — TOP 15
# ----------------------------------------------------
def scrape_hacker_news():
    response = requests.get("https://news.ycombinator.com/news")
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select(".titleline > a:first-child")

    article_texts = []
    article_links = []

    for i, article_tag in enumerate(articles):
        if i >= 10:
            break

        title = article_tag.getText()
        link = article_tag.get("href")

        article_texts.append(title)
        article_links.append(link)

    # Build formatted section
    hn_body = "🔶 Top 10 Hacker News Posts:\n\n"
    for i in range(10):
        hn_body += f"{i+1}. {article_texts[i]}\n"
        hn_body += f"   {article_links[i]}\n\n"

    return hn_body


# ----------------------------------------------------
# SCRAPE PRODUCT HUNT WITH PLAYWRIGHT
# ----------------------------------------------------
def scrape_product_hunt():
    try:
        with sync_playwright() as p:
            # Launch browser in headless mode with minimal dependencies
            browser = p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu'
                ]
            )
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            
            print("Loading Product Hunt...")
            # Navigate to Product Hunt
            page.goto("https://www.producthunt.com/", wait_until="domcontentloaded", timeout=30000)
            
            # Wait longer and try multiple selectors
            print("Waiting for content to load...")
            try:
                # Try waiting for any of these common selectors
                page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(5)  # Extra wait for JavaScript
            except:
                print("Network idle timeout, continuing anyway...")
                time.sleep(5)
            
            # Get the page content
            content = page.content()
            browser.close()
            
            print("Parsing content...")
            # Parse with BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")
            
            # Find the main container
            main_div = soup.find("div", class_="flex flex-col gap-10")
            
            if not main_div:
                print("Could not find main container")
                return "⚠️ Could not find Product Hunt content\n\n"
            
            # Find the nested div with flex flex-col
            content_div = main_div.find("div", class_="flex flex-col")
            
            if not content_div:
                print("Could not find content container")
                return "⚠️ Could not find Product Hunt content container\n\n"
            
            # Find all section tags
            sections = content_div.find_all("section", class_=lambda x: x and "group relative isolate flex flex-row" in x)
            
            print(f"Found {len(sections)} sections")
            
            product_texts = []
            product_links = []
            
            for section in sections:
                # Navigate through the nested divs to find the link
                flex_div = section.find("div", class_="flex min-w-0 flex-1 flex-col")
                if flex_div:
                    text_div = flex_div.find("div", class_=lambda x: x and "text-16 font-semibold" in x)
                    if text_div:
                        link_tag = text_div.find("a")
                        if link_tag:
                            title = link_tag.get_text(strip=True)
                            link = link_tag.get("href")
                            
                            # Make sure link is absolute
                            if link and link.startswith("/"):
                                link = f"https://www.producthunt.com{link}"
                            
                            product_texts.append(title)
                            product_links.append(link)
            
            # Build formatted section
            if len(product_texts) == 0:
                print("No products found")
                return "⚠️ No products found on Product Hunt\n\n"
            
            print(f"Successfully scraped {len(product_texts)} products")
            ph_body = "🚀 Product Hunt Featured Products (Today's Trending):\n\n"
            for i in range(len(product_texts)):
                ph_body += f"{i+1}. {product_texts[i]}\n"
                ph_body += f"   {product_links[i]}\n\n"
            
            return ph_body
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"⚠️ Error scraping Product Hunt: {str(e)}\n\n"


# ----------------------------------------------------
# COMBINE INTO ONE EMAIL
# ----------------------------------------------------
print("Starting scraping process...")
ph_section = scrape_product_hunt()
hn_section = scrape_hacker_news()

email_body = ph_section + "\n" + hn_section

print("\n" + "="*60)
print("EMAIL PREVIEW:")
print("="*60)
print(email_body)
print("="*60 + "\n")

# ----------------------------------------------------
# SEND EMAIL
# ----------------------------------------------------
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_email():
    # Get current date for unique subject
    today = datetime.now().strftime("%B %d, %Y")  # e.g., "December 05, 2024"
    
    msg = EmailMessage()
    msg["Subject"] = f"Daily News Digest - {today}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(email_body)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.send_message(msg)


# ----------------------------------------------------
# RUN ONCE AND EXIT
# ----------------------------------------------------
send_email()
print("Email sent successfully. Program completed and exiting...")
