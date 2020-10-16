# liqu0r

## <i> Third Milestone Project - Data Centric Development - Code institute </i>

---

**liqu0r** is a Web based cocktail app that allows anyone to upload a recipe and share it with the world.

---

![AmIresponsive](https://github.com/kompeet/third-milestone-project/blob/master/static/images/responsive.JPG "Responsive")

---

## Table of Contents

1. [**UX**](#ux)
    - [**Project Goals**](#Project-Goals)
    - [**User Stories**](#User-Stories)
    - [**Developer Goals**](#Developer-Goals)
    - [**Design**](#Design)
        - [**Color Scheme**](#Color-Scheme)
        - [**Fonts**](#Fonts)
        - [**Wireframes**](#wireframes)
6. [**Features**](#Features)
    - [**Existing Features**](#Existing-Features)
    - [**Future Features**](#Future-Features)
7. [**Testing**](#Testing)
8. [**Deployment**](#Deployment)
5. [**Technologies**](#Technologies)
9. [**Credits & Acknowledgements**](#Credits-&-Acknowledgements)


---


## UX

### Project Goals

Lockdown Kitchen is part of my Code Institute Full Stack Software Development studies, the Data Centric Development module.
The scope for this milestone project is to "Create a web application that allows users to store and easily access cooking recipes", using the CRUD operations of Create, Read, Update, and Delete for their recipes. 
My directive was to make an online cokctail app that users could find and share recipes, at the same time impoving their bussineses.
Inspire, entertain and educate anyone—and everyone—interested in what happens in the glass.

### User Stories

- [x] easily acces cocktail recipes from different kind of devices.
- [x] all recipes in one place.
- [x] find cocktails by spirits.
- [x] find cocktails by ingredients I have at home.
- [x] share cocktails by adding them to database.
- [x] edit existing cocktails when I find a mistake or I have a better version of the recipe.
- [x] delete recipes.
- [x] send a feedback to the developer.
- [x] get success or error message to know my feedback was successfully submitted.

### Developer Goals

- Provide a nice, easy to use online cocktail book where the user can create, edit, delete recipes, and filter them by categories and ingredients.
- Learn by practice about databases, Jinja templating, Materialize, and how to use Python with JavaScript.
- Get an insight into Heroku's platform.

### Design

To make an integrated design for this site I used Materialize Icons and Materializecss. 
The cards with borders, the logo with forms. The best-used components are cards. I choosed cards as container of the infos, recipes, and detailed descriptions because the structure of a card helps me to organize the information in a user-friendly way.
For providing feedback and adding recipe I used forms with simply put placeholders.

### Color Scheme

The Colour scheme has modern colours. The supplementary colours are a mix of colours (white,grey,red) used in the cards that is throughout and at the Delete button I set red background color. It contrasts nicely with the text.  The two most important colors are dark blue and the "brick brown"used for the Header/Navigation/Footer and the Feedback form.

### Fonts

The fonts I selected to this page are Arvo and Playfair from [GoogleFonts](https://fonts.google.com/) because it fits perfectly to playful and clear-out theme of the site.

### Wireframes

I made wireframes for each page of the site from three different type of devices:

1. [Desktop](https://github.com/kompeet/third-milestone-project/tree/master/wireframes/desptop)

2. [Tablet](https://github.com/kompeet/third-milestone-project/tree/master/wireframes/tablet)

3. [Mobile](https://github.com/kompeet/third-milestone-project/tree/master/wireframes/mobile)


---


[Back to Top](#table-of-contents)

## Features

### Existing Features

#### Search recipes

- the user can search for recipes sorting the results by ingredients.
- if there are no results found for the keyword, the user can quickly browse for other cocktails.

#### Get all recipes

- the user can reach the list of all the available recipes on one page.

#### Sort recipes

- the user can easily sort recipes by categories from the menu or from the recipe card itself.

#### Edit, Update and delete recipes

- when the user clicks on the detailed recipe page at the bottom they can see a dropdown menu with More options, where they can choose between editing or deleting the recipe.
- if the user chooses to edit the recipe, it will pop up a form with the data of the selected recipe in an editable version.
- by hitting the delete button, the recipe will be removed from the database.

#### Add new recipe

- the user can add a new recipe by using a form.
- the placeholders set in the form help the user how to fill it out.
- a dropdown menu contains the categories, so they can easily choose one.

#### Send feedback

- in the footer the user can find a feedback form which allows them to send their bug report, so I can fix them as fast as possible.
- to get the feedback I used EmailJS.
- after submitting the feedback, they get a success or an error message depending on the successfulness of the action.
- messages are set with timeOut.

### Future Features

- As we haven't learnt yet and it's not part of the requirements I didn't implement authentication.
- A comment section to leave advice or ideas to future users.
- To tag a recipe as favourite so the users may keep a list of all the recipes they enjoyed the most, to keep in their profile.


---


[Back to Top](#table-of-contents)

# Testing

- The first phase of testing is a step by step basis. As I implemented a new code I did run the app on my localhost with the debugger on. If any of the Flask routes did not work, the debugger would catch them.
- If the routes are loaded, I tested them on Chrome and Firefox Developer Tools.
- I tested HTML with W3 Validator. I got an illegal character from [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) templates. They are acceptable errors as Flask needs the templates to connect throughout the site.
- I tested CSS with W3 CSS Validator. I only got errors with misspelled variables, left commas, semicolons.
- I tested all the links to make sure they worked as intended.
- I tested the CRUD capabilities to make sure they all worked.
- All of the codes are validated and beatufied.
    - [HTMLValidation](https://validator.w3.org/):
    - [CSSValidation](https://jigsaw.w3.org/css-validator/):
        - No error found, valid.
    - [JavaScript Validation](https://esprima.org/demo/validate.html):
        - No error found, code is syntactically valid.
    - [PythonCodeChecker](https://extendsclass.com/python-tester.html):
        - No syntax errors detected.
- I tested on my old Sony Xperia Z1 Compact and asked my friends and family members to check on their devices.
- I ran the application through [Website Responsive Testing](https://responsivetesttool.com) to make sure it is responsive. Below is a list of devices:

<details>
<summary>Mobiles</summary> 
<ul>
<li>Apple iPhone 3/4/4s/5/5s/6/6s/6plus/7/7Plus/8/8Plus/X</li>
<li>Nexus 6P/5X</li>
<li>Google Pixel 2/XL</li>
<li>Samsung Galaxy S5/S6/S7/S8/S8+/S9/S9+</li>
<li>Samsung Galaxy Nexus/Note 8</li>
<li>LG G5</li>
<li>LG Optimus G</li>
<li>LG 5</li>
<li>Pantech Vega n6</li>
<li>Lenovo K900</li></li>
<li>Motorola Nexus 6</li>
<li>One Plus 3</li>
<li>ZTE Grand S</li>
<li>Sony XperiaZ3</li>
<li>Blackberry Torch 9800</li>
<li>Microsoft Lumia 1020/1520</li>
</details>
 <details>
<summary>Tablet</summary> 
<ul>
<li>Apple iPad Pro/Pro9.7/1/2/mini</li>
<li>Samsung Galaxy Tab 3 10"/Tab 2 10"/Tab (8.9")/Tab 2 (7")</li>
<li>Samsung Nexus 10</li>
<li>HTC Nexus 9</li>
<li>Asus Nexus 7</li>
<li>LG G Pad 8.3</li>
<li>Amazon Kindle Fire/HD7/HD8.9</li>
<li>Microsoft Surface Pro 2/3</li>
<li>Blackberry Playbook</li>
</details>
  <details>
<summary>Desktops</summary> 
<ul>
<li>Desktop/Laptop</li>
<li>1024 x 768</li>
<li>1280 x 800</li>
<li>1680 x 1050</li>
</details>


---


[Back to Top](#table-of-contents)

# Deployment

### How to deploy the site

To deploy the site on Heroku, you have to follow these steps:

1. Create a Procfile with the terminal command `echo web: python app.py > Procfile`.
2. Create a requirements.txt: `pip3 freeze --local > requirements.txt`.
3. Login to Heroku and create a new app.
4. Push and commit your requirements.tx and Procfile to GitHub repo.
5. On the Heroku page of the app, click on the Deploy and then to the Connect to GitHub.
6. Select the repository and link to the Heroku collection.
7. Set the Config Vars in the Settings:
    - Debug: False;
    - IP: 0.0.0.0;
    - PORT: 5000;
    - MONGO_URI: `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority;`
    - SECRET_KEY: <your_secret_key>.
8. Go back to the Deploy page, click on the Deploy then on Deploy Branch.
9. The app is deployed on heroku, you can open by clicking on the Open app.

### How to deploy locally

Ensure that you have these components:

- [Pip](https://pip.pypa.io/en/stable/installing/);
- [MongoDBaccount](https://www.mongodb.com/cloud/atlas) and set up database.
- [Python3](https://www.python.org/downloads/);
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

1. Download the repository from GitHub by clicking the "download zip" button.
You can clone the respository with the following command:
`git clone https://github.com/kompeet/third-milestone-project`
2. Unpack the files, then navigate them to the correct file location.
3. Create an env which has to contain the MONGO_URI and SECRET_KEY values.
4. Install all requirements from the requirements.txt file using this command:
`sudo -H pip3 -r requirements.txt`
5. Create a Procfile and set the web scale.
`echo web: python app.py > Procfile`
`heroku ps:scale web=1`
6. Sign in to the MongoDB and create a new database.
7. Type to the terminal
`python app.py`

The app's preview should be available.


---


[Back to Top](#table-of-contents)

# Technologies

- [GitHub](https://github.com/);
- [GitPod](https://gitpod.io/);
- [Heroku](https://dashboard.heroku.com/);
- [MongoDB](https://www.mongodb.com/);
- [HTML](https://en.wikipedia.org/wiki/HTML5);
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript);
- [Jquery](https://jquery.com/);
- [Materialize](https://materializecss.com/);
- [Python](https://www.python.org/download/releases/3.0/);
- [EmailJS](https://www.emailjs.com/);
- [MarkDownLit](https://dlaa.me/markdownlint/);
- [Balsamiq](https://balsamiq.com/);
- [HTMLValidator](https://validator.w3.org/);
- [CSSValidator](https://jigsaw.w3.org/css-validator/)
- [JavaScriptValidator](https://esprima.org/demo/validate.html);
- [HTMLFormatter](https://htmlformatter.com/);
- [CSSBeautifier](https://www.freeformatter.com/css-beautifier.html);
- [JSHint](https://jshint.com/);
- [PythonCodeChecker](https://extendsclass.com/python-tester.html);
- [ColorSpace](https://mycolor.space/);
- [GoogleFonts](https://fonts.google.com/);
- [AmIResponsive](http://ami.responsivedesign.is/);
- [Flask](https://flask.palletsprojects.com/en/1.1.x/);
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/);
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [PEP8](http://pep8online.com/)

# Credits & Acknowledgements

##### Code Tutorials

- [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) ~ YouTube
- [Udemy](https://www.udemy.com/)
- I learned a lot from the Code Institute Data Centric Development Mini Project.[Code Institute](https://courses.codeinstitute.net)
- Threads from [Stackoverflow](https://stackoverflow.com/)
- I used [w3schools](https://www.w3schools.com/) instead of [Google](https://www.google.co.uk/)

#### Media

- The Cocktail recipes and images from [Liquor](https://www.liquor.com/)
- The error image from [The empty glass](http://www.artnet.com/artists/alexandre-jacques-chantron/the-empty-glass-NFm-jxTBSr_WebG1yK4rxA2)

#### Acknowledgements

Special thanks to:
- Student Care Team for the understanding and supporting me. I was going through rough times in the past few months. 
- Everybody who did take time to test this page and gave me feedback.


---


#### Disclamer

This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 3!

Peter Komaromi 



