# Darbuka 


## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- create a variable like `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- between Git Pulls do not forget to run `pip install -r requirements.txt`

- *if* new dependencies have been added run `pip freeze > requirements.txt`
