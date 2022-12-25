# Darbuka 
A Babadum.com clone

## Credits
- Images forked from https://github.com/rpaaron/chinese_babadum_trainer but all credit/rights due to http://babadum.com
- Slide in pop ups - https://codepen.io/Web_Cifar/pen/qBEvGrZ?editors=1000
- Turkiye, Azarbayjan, Pakistan & US flag - by [Melvin ilham Oktaviansyah](https://freeicons.io/profile/8939)
- Palestine & UK flag by [Ahmad Smadi](https://freeicons.io/profile/203466?page=7)
- <a target="_blank" href="https://icons8.com/icon/HbhxNiiI7KtP/translate">Translate</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/63766/globe">Globe</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/103661/circled-menu">Circled Menu</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/103798/home-page">Home Page</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/46351/area-chart">Area Chart</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/YsISDBQ47eI0/scoreboard">Scoreboard</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/ScZWTm5akXlG/sign-out">Sign Out</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/TIcq6nNACnhE/autumn">Autumn</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- Illustration by <a href="https://icons8.com/illustrations/author/zD2oqC8lLBBA">Icons 8</a> from <a href="https://icons8.com/illustrations">Ouch!</a>

## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- create a variable like `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- between Git Pulls do not forget to run `pip install -r requirements.txt`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

## TODOs
- [x] Create homepage
- [x] Add language links to bottom right
- [x] colour background of cells a pastel colour
- [x] randomise colours with page reload
- [x] Use HTMX to submit answers as clicks
- [x] auto load next question 2 seconds after answer is shown
- [ ] Animate number changes
- [X] Create stats page
- [x] Create high scores page
- [ ] Create attribution page
- [ ] Use gTTS to read each word!