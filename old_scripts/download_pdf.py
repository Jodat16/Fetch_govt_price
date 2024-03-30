import requests
from bs4 import BeautifulSoup
import re
import os

webpage_url = "https://commissionerkarachi.gos.pk/price-list"

def download_file(url, save_as):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(save_as, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        print(f"File downloaded successfully as {save_as}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def find_and_download_first_matching_file(webpage_url, save_directory, file_extensions):
    try:
        response = requests.get(webpage_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)

        pdf_count = 0
        download_pdf_urls = []
        for link in links:
            href = link['href']
            if pdf_count < 3:
                if re.search(file_extensions, href, re.IGNORECASE):
                    pdf_count+=1
                    download_url = href if href.startswith('http') else f"{webpage_url.rstrip('/')}/{href}"

                    download_pdf_urls = download_pdf_urls + [download_url] 
                    
        local_filename_fruit = os.path.join(save_directory, os.path.basename(download_pdf_urls[1]))
        download_file(download_pdf_urls[1], local_filename_fruit)
        local_filename_vegetables = os.path.join(save_directory, os.path.basename(download_pdf_urls[2]))
        download_file(download_pdf_urls[2], local_filename_vegetables)
        return
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

download_directory = "./price_list"

os.makedirs(download_directory, exist_ok=True)

file_extensions = r'\.(pdf|docx|xlsx|zip)'
find_and_download_first_matching_file(webpage_url, download_directory, file_extensions)
