# 📘 Assignment: Building a Simple Web App with Flask

## 🎯 Objective

Learn the basics of web development by creating a multi-page web application using the Flask framework. You will practice routing, HTML templating, and handling user input through forms to build an interactive website.

## 📝 Tasks

### 🛠️ Set Up Flask and Create Routes

#### Description
Initialize a Flask application and create multiple routes to handle different pages.

#### Requirements
Completed program should:

- Install Flask
- Create a Flask application instance
- Define at least three routes (e.g., home, about, contact)
- Return simple HTML responses or render basic templates
- Run the development server and verify all routes work
- Example routes:
  - `/` - Home page
  - `/about` - About page with information
  - `/contact` - Contact page


### 🛠️ Use Templates and Static Files

#### Description
Separate HTML from Python code using Flask templates and add styling with CSS.

#### Requirements
Completed program should:

- Create a `templates/` directory with HTML template files
- Use Jinja2 templating to render dynamic content
- Pass data from routes to templates using context variables
- Create a `static/` directory for CSS files
- Add CSS styling to make pages visually appealing
- Link static files (CSS) to templates properly
- Create a base template for shared layout (header, navigation, footer)


### 🛠️ Handle Form Data (Stretch Goal)

#### Description
Create a form to collect user input and process the submitted data.

#### Requirements
Completed program should:

- Create an HTML form with multiple input fields (e.g., name, email, message)
- Set up a POST route to handle form submissions
- Validate and process form data
- Display a confirmation message or redirect after submission
- Implement basic error handling for empty or invalid fields
- Example: Build a simple feedback or survey form
