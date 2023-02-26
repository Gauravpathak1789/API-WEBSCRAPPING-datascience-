#!/usr/bin/env python
# coding: utf-8

# Q1. What is Flask Framework? What are the advantages of Flask Framework?

# In[1]:


#Flask is a popular Python web framework that is designed to be lightweight, flexible, and easy to use. It was created by Armin Ronacher and released in 2010 as an open-source project. 
#Lightweight and Flexible: Flask is a lightweight framework that does not include a lot of overhead or unnecessary features. This makes it easy to use and flexible, allowing developers to build web applications quickly and easily.

#Easy to Learn: Flask has a simple and intuitive API that is easy to learn and understand, even for developers who are new to web development.

#Extensible: Flask allows developers to add their own extensions as needed, making it easy to customize and extend the functionality of the framework.

#Large Community: Flask has a large and active community of


# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in 
# Jupyter Notebook

# In[2]:


from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'


# Q3. What is App routing in Flask? Why do we use app routes

# In[3]:


#In Flask, app routing refers to the process of mapping URLs to specific functions or views that handle requests to those URLs. 

#Organizing Code: App routes help organize code in a Flask application by separating different types of requests and their corresponding actions into separate functions.

#Handling User Input: App routes allow developers to define specific actions to take when users interact with the application by sending requests to specific URLs.


# Q4.  Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” 
# route to show the following details:
# 
#     Company Name: ABC Corporation
# 
#     Location: India
# 
#     Contact Detail: 999-999-9999 

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """Company Name: ABC Corporation

        Location: India

        Contact Detail: 999-999-9999 """

@app.route("/welcome")
def welcome_message():
    return "Welcome to ABC Corporation"

if __name__=="__main__":
    app.run(host="0.0.0.0")


# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the 
# url_for() function.

# In[ ]:


#In Flask, the url_for() function is used for URL building. This function generates a URL to a specific function or endpoint based on its name.
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/admin')
def admin():
    return 'Welcome to the admin page!'

with app.test_request_context():
    print(url_for('index'))  # Output: /
    print(url_for('show_user_profile', username='John Doe'))  # Output: /user/John%20Doe
    print(url_for('show_post', post_id=1))  # Output: /post/1
    print(url_for('admin'))  # Output: /admin


# In[ ]:




