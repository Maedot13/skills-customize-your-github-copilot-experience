from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# TODO: Create a home route that renders the home page
# @app.route('/')
# def home():
#     pass

# TODO: Create an about route that renders the about page
# @app.route('/about')
# def about():
#     pass

# TODO: Create a contact route that handles both GET (display form) and POST (process form)
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     pass

# TODO: (Optional) Create a route to display submitted feedback or messages
# @app.route('/messages')
# def messages():
#     pass

if __name__ == '__main__':
    app.run(debug=True)
