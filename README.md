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


