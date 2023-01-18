
# Django GraphQL User Authentication
This project is a demonstration of how to implement user authentication in a Django project using GraphQL.

Features
Register a new user
Log in an existing user
Log out a logged in user
View the current authenticated user
Prerequisites
Python 3.11.x
Django 4.x

# Installation
Clone the repository: 
- git clone https://github.com//MuhammadZainJaved/BasicAuthentication.git
# Install the requirements:
- pip install -r requirements.txt
# Run migrations: 
- python manage.py migrate
# Start the development server:
- python manage.py runserver
# Usage

Register a user
To register a new user, send a mutation request to the /graphql endpoint with the following variables:

# Copy code
mutation {
  register(username: "YOUR-USERNAME", email: "YOUR-EMAIL", password: "YOUR-PASSWORD") {
    user {
      id
      username
      email
    }
    token
  }
}
# Log in a user
To log in an existing user, send a mutation request to the /graphql endpoint with the following variables:

Copy code
mutation {
  login(email: "YOUR-EMAIL", password: "YOUR-PASSWORD") {
    user {
      id
      username
      email
    }
    token
  }
}
<!-- Log out a user
To log out a logged in user, send a mutation request to the /graphql endpoint with the following variables:

Copy code
mutation {
  logout
} --> # Logout is not implemented 

# View the current authenticated user
To view the current authenticated user, send a query request to the /graphql endpoint with the following variables:

Copy code
query {
  me {
    id
    username
    email
  }
}
Note
It's important to set the header with the token that receive after registration or login with the key Authorization and value JWT YOUR_TOKEN

Contribute
If you have any suggestions or improvements, feel free to open an issue or a pull request.
