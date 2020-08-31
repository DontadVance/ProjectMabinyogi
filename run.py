#This app variable must exist within __init__.py inside the package
from mabinyogi import app
#Starting the server inside our code!
if __name__  == '__main__':
    app.run(debug=True)
