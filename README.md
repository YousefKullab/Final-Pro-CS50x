# Full Responsive E-commerce Website 

The proposed concept involves creating a fully adaptable e-commerce website that seamlessly adjusts to different devices and screen sizes.

### [YouTube Video Demo For Website](https://www.youtube.com/watch?v=GQIYdkfCGBc)

## Techniques That Use

- Html, Css, Js & Bootstrap For Front-End.
- Python, Flask & SQLAlCHEMY For Back-End.

## Requirements to run flask website ( E-commerce Website )

- Open [VS code](https://code.visualstudio.com/)
- Install some required extensions.
  - [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
  - [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
- [Install Python](https://www.python.org/downloads/)
- Install pip use this command in teminal `py -m ensurepip --upgrade` and than run this command `py get-pip.py`.
- Install Flask use this command `pip install -U Flask`.
- Install SQLAlchemy For Flask use this command `pip install -U Flask-SQLAlchemy`.
- Finally run this command is your termianl `python -m flask run` or click in **Run** button.

## File Structure

- `mian.py`: From this file you start run the flask website.
- `instance/`: It is created automatically when the site starts, and it creates a database for the site.
- `JoBa/`: Contains all website files.
	- `static/`: Contains all css, js file and images for website.
		- `css/`: Contains all css files.
			- `style.css`: It is a file written use CSS3 language that works on designing a web page in terms of fonts, colors, and how to display elements.
		- `js/`: Contains all javascript files.
			- `main.js`: It is a file written use JavaScript language that works to make the website more interactive and dynamic.
		- `images/`: Contains all images for the website.
	- `templates/`: Contains all html file for the website.
		- `base.html`: It is a file written use HTML5, It is the basic structure of all pages of the site and using Jinja template language the rest of the web pages can inherit the basic elements of a site like head, nav, footer.
		- `home.html`: It is the home page of the site that contains some of the featured products in JoBa. website.
		- `profile.html`: It is a page that contains some basic information about the user such as name, email and budget.
		- `cart.html`: It is a page containing the pending products selected by the customer until the process is confirmed and the product is shipped.
		- `login.html`: Normal login page using HTML Form and post request use Python
		- `sign_up.html`: Normal sign_up page using HTML Form and post request use Python
		- `contact_us.html`: Contact support page The communication via e-mail has been programmed using JS sendEmail function use [emailjs](https://www.emailjs.com/)
		- `shop1.html` `shop2.html` `shop3.html`: They are pages to display the products available in JoBa. website
		- `product.html`: It is a product page that contains information about the product and an image. The gallery inside the page has been programmed using JavaScript.
	- `init.py`: The `init.py` files are required to make Python treat the directories as containing packages, i create the SQLAlchemy database and make the create_app method to initialize a flask app.
	- `auth.py`: It contains some root like login, sing_up that use to authentication the user to access to their accounts.
	- `models.py`: It contains two classes to allow you to make the user table and product table in you database.
	- `views.py`: It contains the rest of the root on the site and using HTML Forms and use post, get request you can get the user input and modify them in proportion to the site and store them in databases.
- `requirements.txt`: It is just a text document containing some of the libraries used within the project.

## License

Copyright © 2022 JoBa. E-commerce
