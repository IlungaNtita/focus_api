# Create a virtual environment to isolate our package dependencies locally

# these instructions assume a linux or wsl environment

1. sudo apt-get install python3-pip
2. sudo pip3 install virtualenv
3. virtualenv venv
4. source venv/bin/activate
5. pip install -r requirements.txt

# graphene-django fixes

the current version of graphene uses force_Text which is not used in django 4 so this needs to be manually patched till the package is https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding/70390648

# Python version

Minimum required version for python is Python 3.10.1. Make sure you have the latest version installed on your system from https://www.python.org/downloads/.

# GraphQL fixes

in Lib/site-packages/jwt/api_jws.py file
replace line 5 'from collections import Mapping' to
'from collections.abc import Mapping'

Also for api_jwt.py in the same folder location

also replace graphql_jwt folder in lib/site-packages/
with the one provided in the resources folder