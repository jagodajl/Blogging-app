A blog is a full-featured blog platform. It uses Flask, SQLAlchemy, as well as Bootstrap templates. It has the following features:
- user and eye-friendly interface
- storing entries in the form of a database
- viewing entries feature
- adding new entries feature
- deleting entries feature
- logging option
- drafts storage option

- Project is covered with: unit tests (80% files, 97% lines covered) and integration tests (Selenium, 90% files, 98% lines covered). 

How to run blog:
- install all the packages listed in the requirements.txt file (they are necessary for the proper operation of the program)
- please type "flask run" into terminal
- next click the link that comes up (http://127.0.0.1:5000/)

How to run Selenium tests:
- please run the app by typing 'flask run' into a terminal 
- if you don't have chrome web browser (Version 107) and m1 processor please download web driver appropriate for your PC from:
https://chromedriver.chromium.org/downloads
- also, when using other web driver, please adopt browser in pytest fixture in a blog/tests/test_selenium.py
