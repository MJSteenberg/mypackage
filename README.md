# mypackage
Team 9 Functions

# building this package locally
python setup.py sdist

# use this to install this package from Github
pip install git+https://github.com/MJSteenberg/mypackage

# upgrading this package from Github
pip install --upgrade+https://github.com/MJSteenberg/mypackage

# usage
# In your .py file use:
import mypackage.myModule as mm

# calling the functions
mm.<functionname>(<parameters>)

