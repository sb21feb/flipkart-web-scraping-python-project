from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find(class_="B_NuCI").get_text().strip()

    except AttributeError:
        title = ""

    return title

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find(class_="_30jeq3 _16Jk6d").get_text().strip()

    except AttributeError:
        price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find(class_="_3LWZlK").get_text().strip()

    except AttributeError:
        rating = ""

    return rating


# Function to extract Number of User Reviews and Ratings
def get_review_and_ratings_count(soup):
    try:
        review_count = str(soup.find(class_="_2_R_DZ").text.strip()).replace('\xa0', ' ')

    except AttributeError:
        review_count = ""

    return review_count


# Function to know about Warranty
def get_warranty(soup):
    try:
        warranty = soup.find(class_="_352bdz").get_text().strip().replace('Know More','')

    except AttributeError:
        warranty = ""

    return warranty

if __name__ == '__main__':

    # add your user agent
    HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_48b7db82-1162-4e18-9fd7-7e0e47dad627_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all(class_='_1fQZEK')

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    d = {"title": [], "price": [], "ratings": [], "rating_and_reviews_count": [], "warranty": []}

    # Loop for extracting product details from each link
    for link in links_list:
        new_webpage = requests.get("https://www.flipkart.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['rating_and_reviews_count'].append(get_review_and_ratings_count(new_soup))
        d['warranty'].append(get_warranty(new_soup))

    flipkart_df = pd.DataFrame(d,index=list(range(0,len(links_list))))
    flipkart_df['title'].replace('', np.nan, inplace=True)
    flipkart_df = flipkart_df.dropna(subset=['title'])
    flipkart_df.to_csv("flipkart_data.csv", header=True, index=False)


