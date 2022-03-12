# MAROMBA
#### Video Demo: https://youtu.be/5lC67fpRKfA
#### Description: 

This is a project that gives you relevant information to start the diet, all done in Flask.

It starts with a "register" and "login" made with Flask-Login, where the forms are made with Flask-WTF and the hashes are made in Werkzeug, we save everything in a sqlite database managed through Flask-SQLAlchemy, in it we create tables to store the user's information.

Now logged into the site, we are redirected to "index", where we get a message to go to "calculator" if we haven't been there before.

In calculator, we have to put our information in the form, again done with Flask-WTF, the site will get your information with the "POST" method and create a table in the database with your data and additional information that are calculated from them and give you redirect to index.

In index we will now have a table made with html and bootstrap that will contain your data that you have given, the calculated ones, suggestions and a button that, when clicked, will activate a javascript function that will create a form for you to change the value of the item in the row. Python will read this form and change the item in the database and redirect to index.

If you want to logout the site there is a link to it, you just need click in logout.