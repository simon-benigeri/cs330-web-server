# Set-Up Instructions

## Step 1: Install Dependencies using PIP

```shell
# from the command line, navigate to this directory and run the following:
pip3 install -r requirements.txt
```

## Step 2: 
Set up your database connection string by creating an .env file in the root of this directory. Here is a sample .env file:

```bash
# Your environment variables (edit this), extracted from your DB connection string
PASSWORD=<your_password>
DATABASE_NAME=<your_database_name>
USERNAME=<your_database_username>
HOST=<your_host_address>
```

## Step 3: 
To run:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```