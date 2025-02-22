# create a virtual irtual enviroment 
python -m venv venv

# activate the venv
venv\Scripts\activate

# install all the requirments
pip install -r requirements.txt

# start the project
flask run

# connect to postgres db locally 
1. create .env file
2. give database url with user,password and database name
3. make sure database is created in postgress
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase

# migration 
flask db init    # for first time
flask db migrate  # eveytime after changes to model file 
flask db upgrade   # every time changes to model follwed by migrate

# run python shell(interact with db from cmd)
flask shell
flask <path> import <class name of model> -- src.models.category import Category