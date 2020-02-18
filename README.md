# mypackage
Team 9 Functions

# building this package locally
python setup.py sdist

# use this to install this package from Github
pip install git+https://github.com/MJSteenberg/mypackage

# upgrading this package from Github
pip install --upgrade git+https://github.com/MJSteenberg/mypackage

# usage
# In your .py file use:
import mypackage.myModule as mm

# calling the functions
mm.<functionname>(<parameters>)

# the Dataframes file contains all data used in the predict
Need to use stopwords dict for Function 6.
