When using ngrok in the program or changing the domain, you need to change the DOMAIN in the .env file and the API_DOMAIN variable in the JavaScript files to the new domain.

Docker is not used in the program, Docker will be added to the program soon.

To run the program (without using docker) you need to run the first django project: python3 manage.py runserver
And to run telegram bot: python3 app.py (app.py in folder: bot/)

Using Docker: 
1. Open Docker Desktop
2. You need to write these commands:
   1. docker compose build
   2. docker compose up

The program uses Django, DRF and Aiogram 2