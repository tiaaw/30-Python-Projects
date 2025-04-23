import re
from typing import Final 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[ 
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


def scrape_emails(driver, url: str) -> set:
    print(f'Scraping {url} for emails')
    driver.get(url)
    page_source = driver.page_source
    
    list_of_emails = set()
    
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        list_of_emails.add(re_match.group())
        
    return list_of_emails


def close_browser(driver) -> None:
    print('Closing browser...')
    driver.close()


def main(): 
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    
    driver = webdriver.Chrome(options=chrome_options)
    emails = scrape_emails(driver, 'https://www.randomlists.com/email-addresses?qty=50')
    close_browser(driver)
        
    for i, email in enumerate(emails, start=1):
        print(i, email, sep=': ')
        

if __name__ == '__main__':
    main()