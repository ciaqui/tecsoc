# tecsoc

-----------------------------------------------------

Python version: 3.10

### Required set up configurations:

Create a virtual environment in the neighbourfy/ folder using the following windows (or equivalent) terminal commands

    > py -m venv venv

    > venv\Scripts\activate

    > py -m pip install -r requirements.txt

note: if you do not activate the Venv before installing the requirements.txt,
then it will be installed to your main python directory

-----------------------------------------------------

## config.py file is needed and should look simular to below
Create a file in tecsoc/main/ called 'config.py'
this must contain the folowing variables:

``` python
from datetime import timedelta
secret_key = '<- add secret key here ->'
database_uri = 'mysql+pymysql://<- DB Password ->@<- DB domain/IP (localhost normally) ->/<- DB Name ->'
debug_setting = True
remember_cookie_duration = timedelta(days=1)
sqlalchemy_track_modifications = False
```

-----------------------------------------------------

### Secret key generation  
secret_key: Use the following commands to generate a secret key:

    > python

    >>> import os

    >>> os.urandom(24).hex()


database_uri: replace the <- -> with the correct info

-----------------------------------------------------

### Creare DB Tables
To add the tables to your local testing database, for example you can use the following commands:

    > python

    >>> from main import db

    >>> db.create_all()

-----------------------------------------------------

### How to update a feature branch from main

    > git checkout <feature branch> 

    > git merge origin/main

    > git push origin <feature branch>

-----------------------------------------------------

### ~~How to Deploy to Heroku~~
### ~~no longer needed after moving to ci/cd with heroku~~
### Still needed

    > git push origin main:deploy

-----------------------------------------------------
