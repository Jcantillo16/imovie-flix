Imovie-Flix
===========

python: 3.10.8
django: 4.1.3

# Setup
1. Create a virtual environment
2. Install requirements.txt
3. load the categories from seeds/load_categories.py
4. run the migrations
5. run the server
6. create a superuser


# Create a virtual environment
`python -m venv venv`

# Activate the virtual environment
`source venv/bin/activate`

# Install requirements.txt
`pip install -r requirements.txt`

# Run migrations
`python manage.py makemigrations`
`python manage.py migrate`



