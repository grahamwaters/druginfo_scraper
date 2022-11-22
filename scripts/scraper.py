import requests
# using beautiful soup
from bs4 import BeautifulSoup
import pandas as pd
import time
import tqdm
from tqdm import tqdm
import random

base_url = 'https://druginfo.nlm.nih.gov/drugportal/drug/names/' # will be followed by letters a-z which indicate new pages with drugs starting with that letter.

# get the html from the page and parse it
def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

# get the links to the drugs
def get_drug_links(html):
    drug_links = []
    for link in html.find_all('a'):
        # the links to the drugs are in the format /drugportal/name/DrugName
        if link.get('href') != None and '/drugportal/name/' in link.get('href'):
            drug_links.append(link.get('href'))
    return drug_links

# get the name of the drug from the link
def get_drug_name(link):
    return link.split('/')[-1]

drug_dataframe = pd.DataFrame(columns=['Medication Name', 'Medication Link'])

# loop through all the letters
for letter in tqdm('abcdefghijklmnopqrstuvwxyz'):
    # sleep for 1 to the length of the most recent drug name seconds // 2
    try:
        time.sleep(random.randint(1, len(drug_dataframe['Medication Name'].iloc[-1]) // 4)) # sleep for a random amount of time to avoid being blocked
    except IndexError:
        time.sleep(1)
    # get the new page with a try/except block in case the page doesn't exist
    try:
        html = get_html(base_url + letter)
    except:
        continue
    # get the links to the drugs
    drug_links = get_drug_links(html)
    # loop through the links
    for link in drug_links:

        # get the name of the drug
        drug_name = get_drug_name(link)
        # replace % with space in the name
        drug_name = drug_name.replace('%20', ' ')
        drug_name = drug_name.replace('%2C', ',')
        drug_name = drug_name.replace('%2F', '/')
        drug_name = drug_name.replace('%28', '(')
        drug_name = drug_name.replace('%29', ')')
        drug_name = drug_name.replace('%26', '&')
        drug_name = drug_name.replace('%2B', '+')
        drug_name = drug_name.replace('%3A', ':')
        drug_name = drug_name.replace('%3B', ';')

        # add the name and link to the dataframe
        drug_name = drug_name.replace('%', ' ')

        # actual medication link is the base url + the link
        drug_link = 'https://druginfo.nlm.nih.gov' + link

        # add the info to the dataframe
        # using concat instead of append because of future deprecation of append
        drug_dataframe = pd.concat([drug_dataframe, pd.DataFrame([[drug_name, drug_link]], columns=['Medication Name', 'Medication Link'])], ignore_index=True)

# save the dataframe to a csv file
drug_dataframe.to_csv('./data/drug_info.csv', index=False)
