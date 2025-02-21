# create a virtual irtual enviroment 
python -m venv venv

# activate the venv
venv\Scripts\activate

# install all the requirments
pip install -r requirements.txt

# start the project
flask run

# migration 
flask db migrate
flask db upgrade

# run python shell(interact with db from cmd)
flask shell
flask <path> import <class name of model> -- src.models.category import Category