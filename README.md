# poggle
Wordle Clone (but POG)

## Setup instructions (Backend)
> Instructions below will run properly on a unix based machine, but might need some adjustments to run on a windows based machine
### Virtual Environment
- Navigate to the `backend/poggle` directory
- Run the `python3 -m venv ./venv` command to create a new virtual environment
- Navigate to the newly created `./venv` directory
- Run the  `touch .env` command to create a file for holding environment variables
- Run the `python3` command to open up an interactive shell, and run the block below to get a random secret key for your .env file
 ```py
 from django.core.management.utils import get_random_secret_key
 print(get_random_secret_key())
 ```
- Copy the `KEY` that is printed, and type SECRET_KEY='`KEY`' in your `.env` file and save (note that there are no spaces)
- To activate your virtual environment, navigate to the `backend/poggle` directory and run `source venv/bin/activate`
### Requirements
- Activate your virtual environment (venv)
- Run `pip3 install -r requirements.txt` to install requirements for this project in your venv
- **Don't forget to run `pip3 freeze > requirements.txt` before you commit new code**
### Starting up project
- Navigate to the `backend/poggle` directory
- Run `python3 manage.py makemigrations` and `python3 manage.py migrate` to make and apply any model changes/creations to your local database every time you update your code
- Run `python3 manage.py runserver` to run the server and visit http://127.0.0.1:8000/ to see the app, or test the API
