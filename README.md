# Basic Django Redis Caching


https://user-images.githubusercontent.com/104749779/174723004-a0f40d78-568f-4e37-b07f-d10082a9ed03.mov


### Create a virtual environment
- virtualenv venv

### Activate the virtual environement
- source venv/bin/activate

### Install the requirements
- pip install -r requirements.txt

### Migrations
- python manage.py makemigrations
- python manage.py migrate

### Start redis server
- redis-server
- ctrl+C to close

### Run django development server
- python manage.py runserver

### View the Pokemon list view
- 127.0.0.1:8000/pokemon/
