# Darbuka 
A Babadum.com clone

## Credits
Images forked from https://github.com/rpaaron/chinese_babadum_trainer but all credit/rights due to http://babadum.com
Slide in pop ups - https://codepen.io/Web_Cifar/pen/qBEvGrZ?editors=1000


## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- create a variable like `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- between Git Pulls do not forget to run `pip install -r requirements.txt`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

## TODOs
- [ ] Create homepage
- [ ] Add language links to bottom right
- [ ] colour background of cells a pastel colour
- [ ] randomise colours with page reload
- [x] Use HTMX to submit answers as clicks
- [ ] auto load next question 2 seconds after answer is shown
- [ ] Animate number changes