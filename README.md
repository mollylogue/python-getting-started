# Spekit Coding Challenge

I used the tutorial in the article [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) to create a barebones Django app deployed to Heroku. I forked the tutorial [repo](https://github.com/heroku/python-getting-started) and committed my changes so that it's easier to see where I added functionality vs where I used the template repo from the tutorial.

TODOs:
- The most notable TODO here is to actually upload a document somewhere, presumably in some sort of document storage location like S3 or something similar. Since the coding challenge focused on the Python/Django/Postgres/Heroku stack, I decided to punt on that portion for now, but add a column in the Documents DB for a link to the actual document itself (i.e. an S3 link). The idea would be that when a POST request is made to the /document/ endpoint, the attachment is uploaded to S3 and the link is stored in the documents table. When a GET request is issued to the /document/ID/ endpoint, the document is fetched from S3 and downloaded.

- More unit tests! In the timebox I gave myself, I prioritized learning Django patterns and getting things up and running over adding robust testing. I'd like more test scenarios in test_views.py, as well as another test file test_models.py to test the underlying models.
