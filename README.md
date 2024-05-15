# Fetch_govt_price
Fetching fruits and vegetables daily price from government website

## How to fetch data

- Need to execute price list fetching script once daily manually (recommended time 12:30pm when price pdf is uploaded on govt website) for now as:
      cd ..../Fetch_govt_price/
      python ./execute_all_scripts_daily.py
  
- If you have a constant running server so define a cron job for that to execute at 12:30pm daily

## How to run the api locally

Simply go to ...../Fetch_govt_price/   
Run following command in terminal :
       uvicorn serve_prices:app --reload --host 0.0.0.0 --port 8000 

# Docker container

Video link :
https://www.youtube.com/watch?v=HyCO6nMdxC0

To build docker image : 
docker build -t govtprice-image .

To create docker container out of image and run : 
docker run -d --name govtprice-cont -p 8030:8030 govtprice-image

To login from our terminal into remote azure container registry(get credentails from access keys of the container registry)
docker login server_url -u user_name -p password  

To build in remote registry
docker build -t registryqualityassessmentapi.azurecr.io/govtprice-image . 

docker push registryqualityassessmentapi.azurecr.io/govtprice-image