import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path) -> list[str]:
    """Open a csv and retrieve the websites and return them as a list"""
    websites = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader: 
            if 'https://' not in row[1] or 'http://' in row[1]:
                websites.append(f'https://{row[1]}')
            else: 
                websites.append(row[1])
                
    return websites


def get_user_agent() -> str: 
    ua = UserAgent()
    return ua.firefox


def get_status_description(status_code) -> str: 
    for value in HTTPStatus: 
        if value == status_code: 
            description = f'({value} {value.name}) {value.description}'
            return description
        
    return '(???) Unknown status code...'


def check_website(website, user_agent): 
    try: 
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception: 
        print(f"Could not get information for website {website}")
        

def main():
    sites = get_websites('websites.csv')
    user_agent = get_user_agent()
    for site in sites: 
        check_website(site, user_agent)
        

if __name__ == '__main__':
    main()
            