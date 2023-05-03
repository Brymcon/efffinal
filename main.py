import requests
import re
import csv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from datetime import datetime


#Acclaim groups
def group1(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        # Perform specific steps for Group 1
        page.get_by_role("button", name="Document Type").click()
        page.get_by_role("button", name="I accept the conditions above.").click()
        page.wait_for_timeout(3000)
        # Retrieve the date information
        content = page.content()
        browser.close()
    return content


#group2
def group2(url):
    # Click-through steps for Group 2
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        page.get_by_role("button", name="Doc Type").click()
        page.get_by_role("button", name="I accept the conditions above.").click()
        page.wait_for_timeout(5000)
        page.wait_for_timeout(10000)
        content = page.content()
        browser.close()
    return content

#Group3
def group3(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("button", name="Doc Type").click()
        page.get_by_role("button", name="I accept the conditions above.").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#Group4
def group4(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("link", name="Name Name").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content


#Aumentum

def group5(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("link", name="Official Records").click()
        page.get_by_role("link", name="Search Official Public Records").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content


#Gadsden and Taylor county click through function
def group6(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

# click through function for landmark websites

def group7(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Search", exact=True).click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Accept").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#click through for Bay county
# def group8(url):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto(url)
#         page.wait_for_timeout(2000)
#         page.get_by_role("link", name=" Search").click()
#         page.wait_for_timeout(2000)
#         page.get_by_role("link", name="Accept").click()
#         page.wait_for_timeout(3000)
#         content = page.content()
#         browser.close()
#     return content

#click through for Hernando landmark to indian
def group8(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Document Search").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Accept").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#click through function for indian river up to suwannee for landmark

def group88(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("link", name="Document Search").click()
        page.get_by_role("link", name="Accept").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#Suwannee click through

def group9(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.get_by_role("link", name="Search", exact=True).click()
        page.get_by_role("link", name="Accept").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#click through for NewVision
def group10(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content


#click through for Myflorida Bradford
def group11(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content


#Indian river
def group89(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.get_by_role("link", name=" Search").click()
        page.get_by_role("link", name="Accept").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#inhouse 1 Charlotte click through function

def group41(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

# group42 collier county click through steps

def group42(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Get the screen size
        page.goto(url)
        page.frame_locator("internal:text=\"<span style=\\\"display: inline-block; width: 0px; overflow: hidden; line-height: 0\"i").get_by_role("link", name="Document Search").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#Hillsborough county custom click through events

def group43(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#Leon county custom click through events to get to date

def group44(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#custom click through function forr getting the date from Manatee
def group45(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#custom click through function for Marion county


def group46(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#custom click through function for Miami-dade county


def group47(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#custom click through events for orange county


def group48(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("button", name="I Acknowledge").click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content

#custom click through events for putnam county

def group49(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_label("I have read and accept the terms of this disclaimer.").check()
        page.get_by_role("link", name="Accept").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="Official Records", exact=True).click()
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
    return content


#BS4 parsing function with native python re #1
def extract_date_group1(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date and instrument number using regex
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        instrument_match = re.search(r'\d{4}\d{4,}', text)
        instrument_number = instrument_match.group(0) if instrument_match else None

        as_of_match = re.search(r'As of\s+(\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}:\d{2}\s+(?:AM|PM))', text)
        as_of = as_of_match.group(1) if as_of_match else None

        return date, instrument_number, as_of
    return None, None, None


#Permanent Index from Aumentum #2
def extract_date_group5(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the latest date (second date) from the Permanent Index
        permanent_index_match = re.search(r'Permanent Index From \d{2}/\d{2}/\d{4} to (\d{2}/\d{2}/\d{4})', text)
        latest_date = permanent_index_match.group(1) if permanent_index_match else None

        return latest_date, None, None
    return None, None, None


#Gadsden and Taylor County Parsing Function Creative Data Solutions #3

def extract_date_group6(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    general_element = soup.select_one(date_selector)
    if general_element:
        date_match = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', general_element.get_text().strip())
        if date_match:
            latest_date = date_match.group(1)
            instrument_number = None  # No instrument number found in the provided HTML
            as_of = None  # No as of field found in the provided HTML
            return latest_date, instrument_number, as_of
    return None, None, None

#Parsing function for landmark websites
def extract_date_group7(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#Parsing function for Osceola Verified through date Newvision

def extract_date_group8(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#parsing function for myflorida county websites to get the date and left release date

def extract_date_group9(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        # Get the 'td' elements within the row
        td_elements = date_element.find_all('td')
        if len(td_elements) >= 3:
            # Extract the release date from the third 'td' element
            text = td_elements[2].get_text().strip()

            # Extract the date using regex
            date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
            date = date_match.group(0) if date_match else None

            return date, None, None
    return None, None, None

#parsing inhouse 1 Charlotte county function

def extract_date_group41(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#Collier county parsing function

# def extract_date_group42(content, date_selector):
#     soup = BeautifulSoup(content, "html.parser")
#     date_element = soup.select_one(date_selector)
#     if date_element:
#         text = date_element.get_text().strip()
#
#         # Extract the date using regex
#         date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
#         if date_match:
#             date_str = date_match.group(0)
#             date_obj = datetime.strptime(date_str, '%m/%d/%Y')
#             date = date_obj.strftime('%m/%d/%Y')
#         else:
#             date = None
#
#         return date, None, None
#     return None, None, None


#Custom parsing function for Hillsborough county


def extract_date_group43(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#Custom parsing function for Leon county

def extract_date_group44(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the second date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}\s+through\s+(\d{1,2}/\d{1,2}/\d{4})', text)
        second_date = date_match.group(1) if date_match else None

        return second_date, None, None
    return None, None, None

# Custom parsing function for Manatee county

def extract_date_group45(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'(\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{1,2}:\d{1,2}\s+[AP]M)', text)
        date = date_match.group(1) if date_match else None

        # Pad the date with zeros
        if date:
            date = datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p').strftime('%m/%d/%Y')

        return date, None, None
    return None, None, None

#Custom parsing function to grab the effective date for Marion County

def extract_date_group46(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#Custom parsing function to grab the effective date for Miami-dade county

def extract_date_group47(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        return date, None, None
    return None, None, None

#custom parsing function for orange county

def extract_date_group48(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        # Extract the text from the element
        text = date_element.get_text().strip()

        # Convert the text to a datetime object and format it as 'MM/DD/YYYY'
        date = datetime.strptime(text, '%B %d, %Y').strftime('%m/%d/%Y')

        return date, None, None
    return None, None, None

#custom parsing function for putnam

def extract_date_group49(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)

    if date_element:
        text = date_element.get_text().strip()

        # Extract the date using regex
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
        date = date_match.group(0) if date_match else None

        if date:
            month, day, year = date.split('/')
            padded_date = f"{month.zfill(2)}/{day.zfill(2)}/{year}"
            return padded_date, None, None
    return None, None, None

#custom parsing function for sarasota :

def extract_date_group50(content, date_selector):
    soup = BeautifulSoup(content, "html.parser")
    date_element = soup.select_one(date_selector)
    if date_element:
        # Extract the text from the element
        text = date_element.get_text().strip()

        # Find the second date in the text
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        dates = re.findall(date_pattern, text)
        if len(dates) >= 2:
            second_date = dates[1]

            # Convert the text to a datetime object and format it as 'MM/DD/YYYY'
            date = datetime.strptime(second_date, '%m/%d/%Y').strftime('%m/%d/%Y')

            return date, None, None
    return None, None, None


def main():
    county_websites = {
        # Acclaim
        'Brevard': ('Acclaim', 'https://vaclmweb1.brevardclerk.us/AcclaimWeb/', group1, "div.releaseHolder > span.releaseInfo", extract_date_group1),
        'Broward': ('Acclaim', 'https://officialrecords.broward.org/AcclaimWeb/', group1, "div.releaseHolder > span.releaseInfo", extract_date_group1),
        'Duval': ('Acclaim', 'https://oncore.duvalclerk.com/', group2, "#main > div.releaseHolder > span", extract_date_group1),
        'Highlands': ('Acclaim', 'http://acclaim.hcclerk.org/', group2, "#main > div.releaseHolder > span", extract_date_group1),
        'Lake': ('Acclaim', 'https://officialrecords.lakecountyclerk.org/', group3, "#main > div.releaseHolder > span.releaseInfo", extract_date_group1),
        'Pinellas': ('Acclaim', 'https://officialrecords.mypinellasclerk.org/', group2, "div.releaseHolder > span.releaseInfo", extract_date_group1),
        ###'Saint Lucie': ('Acclaim', 'https://acclaimweb.stlucieclerk.com/AcclaimWeb/Home/Index', group4, "#ReleaseThroughDate", extract_date_group1),
        'Santa Rosa': ('Acclaim', 'https://acclaim.srccol.com/AcclaimWeb/', group2, "#main > div.releaseHolder > span", extract_date_group1),
        #Aumentum
         'Alachua': ('Aumentum', 'http://isol.alachuaclerk.org/RealEstate/SearchEntry.aspx', group5, "#cphNoMargin_lblSearchSummary", extract_date_group5),
        #Pasco
        #'Pasco': ('CivicPlus'), 'https://app.pascoclerk.com/appdot-public-online-services-forms-or-search.asp', group6, "", extract_date_group6),
        #Create_data_solutions
        'Gadsden': ('Create_data_solutions', 'http://www.gadsdenclerk.com/PublicInquiry/Search.aspx?Type=Name', group6, "#ctl00_panelDisclaimer > table > tbody > tr:nth-child(2) > td.content > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > b", extract_date_group6),
        'Taylor': ('Create_data_solutions', 'http://67.158.150.97/PublicInquiry/Search.aspx?Type=Name', group6, "#ctl00_panelDisclaimer > table > tbody > tr:nth-child(2) > td.content > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > b", extract_date_group6),
        #landmark
        'Baker': ('Landmark', 'https://bakerclerk.com/landmarkweb', group7, "#cfnVerifiedThrough > div", extract_date_group7),
        'Bay': ('Landmark', 'http://records2.baycoclerk.com/Recording/', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Citrus': ('Landmark', 'https://search.citrusclerk.org/LandmarkWeb/home/index', group8, "#cfnVerifiedThrough", extract_date_group7),
        'Clay': ('Landmark', 'http://landmark.clayclerk.com/LandmarkWeb/home/index', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Escambia': ('Landmark', 'https://dory.escambiaclerk.com/LandmarkWeb1.4.6.134', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Flagler': ('Landmark', 'https://apps.flaglerclerk.com/Landmark/', group8, "#cfnVerifiedThrough > div", extract_date_group7),
        'Hernando': ('Landmark', 'https://or.hernandoclerk.com/LandmarkWeb/', group88, "#cfnVerifiedThrough > div", extract_date_group7),
        'Indian_River': ('Landmark', 'https://ori.indian-river.org/', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Lee': ('Landmark', 'https://or.leeclerk.org/LandMarkWeb', group8, "#cfnVerifiedThrough > div", extract_date_group7),
        ### 'Levy': ('Landmark', 'https://online.levyclerk.com/landmarkweb', group7, "#cfnVerifiedThrough > div", extract_date_group7),
        'Martin': ('Landmark', 'http://or.martinclerk.com/LandmarkWeb', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Okaloosa': ('Landmark', 'https://clerkapps.okaloosaclerk.com/Landmarkweb', group89, "#cfnVerifiedThrough > div", extract_date_group7),
        'Okeechobee': ('Landmark', 'https://pioneer.okeechobeelandmark.com/LandmarkWebLive', group8, "#cfnVerifiedThrough", extract_date_group7),
        'Saint Johns ': ('Landmark', 'https://erec.mypalmbeachclerk.com/', group8, "#cfnVerifiedThrough", extract_date_group7),
        'Suwannee': ('Landmark', 'http://records.suwgov.org/LandmarkWeb/Home/index', group9, "#cfnVerifiedThrough > div", extract_date_group7),
        'Union': ('Landmark', 'https://records.unionclerk.com/landmarkweb', group8, "#cfnVerifiedThrough", extract_date_group7),
        'Wakulla': ('Landmark', 'http://www.wakullaclerk.com/Landmarkweb/Home/Index', group89, "#cfnVerifiedThrough", extract_date_group7),
        'Walton': ('Landmark', 'https://orsearch.clerkofcourts.co.walton.fl.us/', group9, "#cfnVerifiedThrough", extract_date_group7),
        #NewVision websites
        'Osceola': ('NewVision', 'https://officialrecords.osceolaclerk.org/browserview/', group10, "#verifyDate > div", extract_date_group8),
        'Polk': ('NewVision', 'https://apps.polkcountyclerk.net/browserviewor/', group10, "#verifyDate > div", extract_date_group8),
        #My Florida County Websites
        'Bradford': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=04', group11, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Calhoun': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=07', group11, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Columbia': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=12', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'De_Soto': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=14', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Dixie': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=15', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Franklin': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=19', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Gilchrist': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=21', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Glades': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=22', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Gulf': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=23', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Hamilton': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=24', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Hardee': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=25', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Hendry': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=26', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Holmes': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=30', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Jackson': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=32', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Jefferson': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=33', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Lafayette': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=34', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Liberty': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=39', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        'Madison': ('myfl', 'https://www3.myfloridacounty.com/ori/dateRange.do?search=DOCUMENT&countynumber=40', group10, "#county_range > tbody > tr:nth-child(30)", extract_date_group9),
        #Inhouse website
        'Charlotte': ('inhouse', 'https://recording.charlotteclerk.com/', group41, "#lblVerifyMessage", extract_date_group41),
        ###'Collier': ('inhouse', 'https://collierclerk.com/records-search/search-official-records/', group42, ".row-fluid .span6 div div", extract_date_group42),
        'Hillsborough': ('inhouse', 'https://pubrec6.hillsclerk.com/ORIPublicAccess/customSearch.html', group43, "#releaseDate", extract_date_group43),
        'Leon': ('inhouse', 'https://cvweb.leonclerk.com/public/clerk_services/official_records/index.asp', group44, "body > div.container.main_container > div:nth-child(3) > div > p.gray_14_medium", extract_date_group44),
        'Manatee': ('inhouse', 'https://records.manateeclerk.com/OfficialRecords/Search', group45, "#content > div:nth-child(2) > div.panel.panel-danger > div.panel-body > p > strong:nth-child(8)", extract_date_group45),
        'Marion': ('inhouse', 'https://nvweb.marioncountyclerk.org/BrowserView/', group46, "body > div.container-fluid.ng-scope > div:nth-child(2) > div > div:nth-child(1)", extract_date_group46),
        'Miami_dade': ('inhouse', 'https://onlineservices.miami-dadeclerk.com/officialrecords/(X(1)S(3u123cw1gurp2ectu4x511j1))/Default.aspx', group47, "#lblOfficialRecordDate > strong", extract_date_group47),
        'Nassau': ('inhouse', 'https://www.myfloridacounty.com/orisearch/45', group10, "#wrapper > div:nth-child(1)", extract_date_group46),
        'Orange': ('inhouse', 'https://or.occompt.com/recorder/eagleweb/docSearch.jsp', group48, "#proofDate", extract_date_group48),
        ###'Putnam': ('inhouse', 'https://apps.putnam-fl.com/peas/peasApplications/or_viewer/publicORIRedact.php', group49, "body > table:nth-child(4) > tbody > tr:nth-child(2) > td", extract_date_group49),
        ###'Putnam': ('inhouse', 'https://apps.putnam-fl.com/peas/peasApplications/or_viewer/publicORIRedact.php', group49, "td.verifyfont", extract_date_group49),
        'Sarasota': ('inhouse', 'https://secure.sarasotaclerk.com/OfficialRecords.aspx', group47, "#cphBody_lIndex", extract_date_group50),
         'Volusia': ('inhouse', 'https://app02.clerk.org/or_m/inquiry.aspx', group47, "#lastInstr", extract_date_group1),

    }


#main function which writes parameters to csv


    with open('county_dates.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['County', 'URL', 'Date', 'Instrument Number', 'As of']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        for county, (software, url, click_through_func, date_selector, extract_date_func) in county_websites.items():
            content = click_through_func(url)
            date, instrument_number, as_of = extract_date_func(content, date_selector)
            print(f"Date for {county}: {url}: {date}")

            # Write the data to the CSV file
            writer.writerow(
                {'County': county, 'URL': url, 'Date': date, 'Instrument Number': instrument_number, 'As of': as_of})


if __name__ == "__main__":
    main()