# Flask Large App Boilerplate

This project is a basic flask modular large app boilerplate with a simple login system and, a powerful admin panel!

This project should be of great assistance for almost any application you're planning to build.

## How to use
* **Clone this repository** `git clone https://github.com/sheyziSilver/flask_largeapp_boilerplate.git`
* Rename the file if needed
* Move to the directory `cd flask_largeapp_boilerplate`
* Run it in the terminal with `python run.py`

## Todo
* Change the navbar title in flask_largeapp_boilerplate/app/templates/base.html
* Add an if statement to the navbar so once the user is logged in they wouldn't see the "Sign up" and "Login" options but a logout menu instead.
You can access the user logged in version by passing the `current_user` object to the template and checking if the user is logged in
  by using `current_user.is_authenticated`. **Note: it returns a boolean value. `True` when logged in and `False` otherwise**

  
## Admin Panel
You can access the admin panel at `127.0.0.1/admin` but you wouldn't be allowed till you signup as an admin.
#### How do you signup as an admin?
At first, you would have to sign up normally with the admin details you are planning to use, 
you would then log out and, log in with this details

**Username:** sheyzi
**Password:** password

you would then see the account you created edit it and make sure you make `is_admin` variable = `True`
you can now access the admin dashboard with the other details you
had created.
