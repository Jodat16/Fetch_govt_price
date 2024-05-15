import requests
from bs4 import BeautifulSoup
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

def find_and_download_latest_files(webpage_url, save_directory):
    try:
        response = requests.get(webpage_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        tbody = soup.find('tbody')

        rows = tbody.find_all('tr')

        download_count = 0
        iterator = 0
        for row in rows:
            iterator +=1
            if iterator == 1:
                continue
            if download_count == 2:
                break

            cells = row.find_all('td')
            if len(cells) == 3:  # Ensure it's a data row with four cells
                date = cells[0].text.strip().replace('-', '')  # Format date
                category = cells[1].text.strip().lower()  # Convert to lowercase
                href = cells[2].find('a')['href']
                
                #filename = f"{os.path.basename(href).split('.')[0]}_{category}_{date}.pdf"
                filename = f"{category}_{date}.pdf"
                local_filename = os.path.join(save_directory, filename)

                download_url = href if href.startswith('http') else f"https://commissionerkarachi.gos.pk{href}"
                download_file(download_url, local_filename)
                download_count +=1

        print("Latest fruit and vegetable PDF files downloaded successfully.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

download_directory = "./price_list_pdf"
os.makedirs(download_directory, exist_ok=True)
find_and_download_latest_files(webpage_url, download_directory)