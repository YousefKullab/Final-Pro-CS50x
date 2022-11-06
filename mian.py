from JoBa import create_app

# https://docs.python.org/3/
# https://flask.palletsprojects.com/en/2.2.x/
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True, host="0.0.0.0", port=8000)


# Software Engineer Joseph. 
