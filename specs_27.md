
# Features

Add your new app to the settings.py, and configure the urls for this new app at the root level of your project
Working in the lender-books/ directory:

Create a new model for Book, which represents an item that will be lent to another person, with the following attributes:

    cover_image: An image field
    title: Text field
    author: Text field
    year: Multiple choice field for year published
    status: Multiple choice field for available or checked-out statuses
    date_added: Auto-generated date field
    last_borrowed: Auto-updated date field

Create a new template called book_list.html that inherits from base.html, which will render out a list of all books in the system for the current user

Create a new template called book_detail.html that inherits from base.html, which will render out the detail for a single book

Create a simple view controller for each of the templates defined above

Create a urls.py for this app, which connects your view controllers and their templates to your application at an appropriate route

Use docker-compose to run makemigrations and migrate once you’ve configured your new model.

You will want to use the Admin console to add some records to your database, so you can verify that data is correctly rendering on the site

Run your application and ensure that all things are as they should be!

# Testing

You are required to meet or exceed an 80% coverage benchmark for this application.
Your focus for the time being will be unit testing your view controllers and models, and you should follow our standard format of roughly three test assertions for each controller or model you define for the application
Note: Be sure you do not test functionality that Django provides
