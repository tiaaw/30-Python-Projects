import os 
import requests

def get_extension(url:str) -> str|None:
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    for extension in extensions:
        if extension in url:
            return extension
    return None

def download_image(url: str, name: str, folder=None):
    
    if ext:=get_extension(url):
        if folder:
            image_name = f'{folder}/{name}/{ext}'
        else: 
            image_name = f'{name}/{ext}'
    else: 
        raise Exception('Image extension could not be found')
    
    # Check is name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists')
    
    try: 
        image_content = requests.get(url).content
        with open(image_content, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: {image_content} successfully')
    except Exception as e:
        print(f'Error: {e}')
        
if __name__ == '__main__':
    url = input('Enter a url: ')
    name = input('What would you like to name it: ')
    
    print('Downloading...')
    download_image(url, name, 'images')
    