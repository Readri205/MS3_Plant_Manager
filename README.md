  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_tulip.png?raw= "Garden Manager")

[View the live **GARDEN MANAGER**  :seedling:  project here.](https://plant-manager-flask-mongodb.herokuapp.com/)

The project uses two key API interfaces as shown here;
### [Trefle.io](https://Trefle.io/)
  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/trefle_header.png?raw= "Trefle Logo")

### [Plant.id](https://plant.id/)
  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/plant_id_header.png?raw= "Plant.ID Logo")

# **GARDEN MANAGER :seedling:**

## Contents

- [**GARDEN MANAGER :seedling:**](#--garden-manager--seedling---)

- [Site Goals](#site-goals)
- [User Experience (UX)](#user-experience--ux-)
  * [User stories](#user-stories)
    + [First Time Visitor Goals](#first-time-visitor-goals)
    + [Returning Visitor Goals](#returning-visitor-goals)
    + [Frequent User Goals](#frequent-user-goals)
    + [Mobile Menu](#mobile-menu)
  * [Design](#design)
    + [colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + ['Materialize' Card Structure](#-materialize--card-structure)
    + [Imagery](#imagery)
  * [Wireframes](#wireframes)
    + [Original Wireframe Design (October 15, 2020).](#original-wireframe-design--october-15--2020-)
    + [Actual Site Design.](#actual-site-design)
- [Features](#features)
  * [Responsive for Device Size](#responsive-for-device-size)
  * [Interactive Elements](#interactive-elements)
  * [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Database Used](#database-used)
  * [Frameworks, Databases, Libraries & Programs Used](#frameworks--databases--libraries---programs-used)
  * [Application Programming Interfaces (API's) Used](#application-programming-interfaces--api-s--used)
- [Site Construction](#site-construction)
  * [Consistent Page Components](#consistent-page-components)
  * [Home Page](#home-page)
  * [Subsequent Pages](#subsequent-pages)
  * [Contacts Page](#contacts-page)
  * [Construction Table](#construction-table)
- [Testing](#testing)
  * [Known Bugs and Issues](#known-bugs-and-issues)
- [Deployment](#deployment)
  * [GitHub Pages](#github-pages)
  * [Heroku Deployment](#heroku-deployment)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  * [Code](#code)
- [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)
- [Version Control](#version-control)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Site Goals

  * This website provides a functionality for users to create a list of plants in collections, either by entering plant details or by uploading from a search. The searches can be made in a number of ways, including by name, image or by filters. Users are able to update the details of plants and collections in their lists. Users are also able to delete plants and collections. A user can also move a plant from one collection to another if so desired. A user can also amend their personal details including email, username and telephone number. A user is also able to fully delete their login and all plants and collections listed on that login. Each users logn and details are specific to that user and cannot be viewed by any other user.

  * **NOTE: This site is currently entirely for educational purposes only. Whilst there is an ability to register for the site, any personal details entered are not protected.**

  * The website is **'functional'**, allowing users to enter information about **Plants** and to view information on specific plants. The site is designed to show details on **Plants** where required.
  * The website concept is to provide a user with a useful list of plants;
    * what is the name of the plant?
    * what are the scientific names and details?
    * what collection do I have the plant in?
    * The structure for the **Plants** is provided by;
      * a list of **plants** entered by and for, a specific user;
      * a list of **collections** entered in which plants can be listed;
      * entering a plant can be made using the following methods;
        * **manual** where a user already has details for a plant, external to the application;
        * **search** to identify a **name** characteristic for a plant;
        * **filter** to identify **colour** characteristics for a plant; and
        * **image** using a computer or mobile device to upload a **file image**.

        * The website sources data from the **[Trefle.io](https://Trefle.io/)** and **[Plant.id](https://plant.id/)**. The website primarily makes use of Application Programming Interfaces (API's) to construct the plant search data. The **[MongoDB](https://www.mongodb.com/cloud/atlas)** is used to store user data and allows for create, read, update and delete data **(CRUD)** for plant details and their user login data. API and other data source details are provided in the **'Application Programming Interfaces (API's) Used'** section below.

* If the site is perceived as successful, it is anticipated that the site could be expanded as;
  * there is a significant amount of data in the Trefle database that can be utilised for more specific searches and filtering;
  * other API sources could also be utilised to improve the information set;
  * other functions could be added such as creating as a calendar for gardening jobs at a particular time of year.

* The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for interested users. The website was designed using **'Mobile First'** principles as the site must be perceived to be quick and easy to use and read as a reference site on a mobile device.

## User Experience (UX)

*   ### User stories

    *   #### First Time Visitor Goals
        * The first time visitor will want to;
          * easily understand the main purpose of the site;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_maininfo.png?raw= "Home")

          * be able to easily navigate throughout the site to find content;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mainmenu.png?raw= "Main Menu")

          * view the carousel images just beneath the header;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_carousel.png?raw= "Carousel")

          * scroll down through the information, read the content, view each of the function cards;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_maininfo.png?raw= "Cards")

          * register for the site and create login credentials;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_register.png?raw= "Register")

          * enter plant details for plants they are interested in;

            * login to the site;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_login.png?raw= "Login")

            * immediately view their plants list;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_myplants.png?raw= "My Plants")

            * immediately view a plant from list;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_viewplant.png?raw= "My Plants")

            * view their collections list;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mycollections.png?raw= "My Collections")

            * search for plants in one of the search methods;
              * name;

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_searchname.png?raw= "Search Name")

              * View plants returned from a search;

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_return.png?raw= "Search Name")

              * View individual plant details from a search return;

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_plantdeets.png?raw= "Search Name")

              * filter by attribute;

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_filter.png?raw= "search Filter")

              * image upload.

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_image.png?raw= "Image")

              ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_imagesuggestions.png?raw= "Image Suggestions")

            * add a plant to users plant list and a collection.

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_addplant.png?raw= "Add Plant")

          * see their user details and amend if necessary.

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mydetails.png?raw= "My Details")

          * contact us to ask about data projects that they may be interested to have completed as an item of work.

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_contact.png?raw= "Contact")

    *   #### Returning Visitor Goals
        * The returning visitor will want to;
          * login to the site;
          * immediately view their plants list;
          * view their collections list.
        * **A returning visitor** may want to go straight to the 'Plant' search function;

            * search for plants in one of the search methods;
              * name;
              * filter by attribute;
              * image upload.
            * on finding a plant the user in they may want to find out more details on that plant by choosing the 'plant details' button;
              * there a number of specific details including in the return;

            * the user may want to add the plant to their plant list and a collection.
        * **A returning visitor** may want to go straight to the 'Contact Us' page;
          * contact us for more information or to provide comments about the site;
          * contact us to ask about projects that they may be interested to have completed as an item of work.

    *   #### Frequent User Goals
        * The frequent user will want to;
          * login to the site;
          * immediately view their plants list;
          * view their collections list.
        * **A returning visitor** may want to go straight to the 'Plant' search function;

            * search for plants in one of the search methods;
              * name;
              * filter by attribute;
              * image upload.
            * on finding a plant the user in they may want to find out more details on that plant by choosing the 'plant details' button;
              * there a number of specific details including in the return;

            * the user may want to add the plant to their plant list and a collection.
        * **A frequent visitor** may want to go straight to the 'Contact Us' page;
          * contact us for more information or to provide comments about the site;
          * contact us to ask about projects that they may be interested to have completed as an item of work.

    *   #### Mobile Menu
          * On mobile devices the menu is shown as a 'hamburger' drop down;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobile.png?raw= "Mobile")

          * On mobile devices the menu is shown as a 'hamburger' drop down;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobilemenu.png?raw= "Mobile Menu")

          * On mobile devices the search function operates in the same manner as for larger screens;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobilesearch.png?raw= "Mobile Search")

          * On mobile devices an image can be captured and uploaded directly;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_capture.png?raw= "Mobile Capture")

*   ### Design
    *   #### colour Scheme
        * The main colour is 'Teal' (#008080), designed to provide a light neutral background to highlight a 'Yellow" (#FFFF00) text. The colours have been manipulated to lighten or darken them using 'Materialize' CSS properties. The various shades of 'Teal' are used to reference the the plant kingdom.
        * The main colours, 'Yellow" (#FFFF00)on a 'Teal' (#008080) background, were potentially a concern for the 'colour blind' fraternity. Some basic tests with colour blind persons did not present any issues, however the spectrum of colour blindness is vast so there may be some issues with some persons. The colour structure is relatively easy to change if there is negative feedback.
    *   #### Typography
        * The site uses the 'Materialize' 'Roboto' default font throughout the whole website. 'Roboto' is a clean font which is both attractive and appropriate.
    *   #### 'Materialize' Card Structure
        * The 'Materialize' card structure is used to return search results. This structures the returns into identifiable components with an image and corresponding details for a return. This keeps each return distinct and independent of each other.
        * The user plant and the collections lists are not constructed in 'Materialize' cards but are shown as accordion lists that the user can access to view more details on each item.
    *   #### Imagery
        * A 'Dark' theme has been intentionally chosen to make it distinct from other numerous 'plant' applications. The dark background provides a clear backdrop to highlight the colours and shapes of plants, and also to highlight clearly the information that is provided in the teal 'card' structure.
        * The header contains a carousel designed to be striking and catch the user's attention and to provide some unique image themes. To provide some context on larger screens each image has a clear title description sourced from the original image provided by the contributor. Note that on some screen sizes the titles can be difficult to read where they blend into the image. As the titles are not fundamental to the website information it has been considered 'acceptable'.
        * Note that the background, carousel and main home page cards all reference  [© Unsplash.com](https://unsplash.com/) for the images. As this is the case there is a risk that an image could be removed from the source and so the site image would fail. Copies of images are retained in the project image folder for backup.
        * The background image is of 'Dark plants ...', designed to provide a dark neutral background yet reference the plant kingdom. The header images are intended to blend into the background image with the 'deep black' backgrounds.

            ![alt text](https://images.unsplash.com/photo-1586990684319-40c14d005de9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1402&q=80)

            *['Dark plants ...'](https://unsplash.com/photos/aDvrHHFGAlE)  By Amir Nyct  [© Unsplash.com](https://unsplash.com/)*


*   ### Wireframes
    *   #### Original Wireframe Design (October 15, 2020).
        * The **'Home'** page includes a basic overall introduction to the purpose of the site. Cards are used to describe the main features of the site. The features are User Plant List, User Collections, Search by a Name, Filter, Image Upload and a  Year Calendar.
        * Once the User has a login these features are accessible from the menu.
        * The menu includes direct links to;
          1. User plant list;
          1. User Collection list;
          1. Search list;
          1. User details.
        * MongoDB to be used as the database core for the user, plant and collection details.
        * The search list is considered to return name and image upload searches as detail page returns.
        * Sources for search data were considered as follows;
          * Trefle.io plant search - [Trefle.io](https://Trefle.io/)
          * Plant.id for image recognition - [Plant.id](https://plant.id/)
        * The contact page uses the following source;
          * Automated Email Response - [Emailjs](https://www.emailjs.com/)
        * All images in the wireframe are by example only.
        *   The **Original Wireframe Design** can be viewed here - [View](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/wireframes/rhcgardenmanager.pdf)
    *  #### Actual Site Design.
        * The developed site uses many of the concepts from the original Wireframe design. Variations are as follows;
          1. The **Home** page has a number of cards explaining the key features of the site, but there is no **'Calendar View'** feature;
          1. The **Calendar Feature** has proven difficult to implement as information to support this appears lacking in the plant world. Most plant and gardening information providers appear to have their own databases to support this kind of feature as a Unique Selling Product (USP). The Trefle.io database has some details such as 'bloom months' and 'sowing months'. However, this data is not complete. The feature could be added as a future feature on the site.
          1. The **'Contact Form'** has its own page. It is accessible from every page either through the main menu or from the footer;
        * The listed API sources, [Trefle.io](https://Trefle.io/), [Plant.id](https://plant.id/) were utilised. [Emailjs](https://www.emailjs.com/) was utilised for email response.

## Features

  *   ### Responsive for Device Size
      * Mobile / Smaller screen size
        * The site is designed primarily for use on a mobile. The 'Box Content' structure using Materialize Grid System has been utilised so that the information boxes (search results) will stack vertically on small screens for readability.
        * The menu system uses the Materialize 'navbar' functionality for small screens using the 'toggle' capability for the 'drop down' menu list from a 'hamburger' icon.
        * The navbar is 'fixed' to the top of the screen at all times on page scroll down for easy access.
        * The navbar is coloured 'dark teal' to make it distinctive from the site pages.
        * The 'hamburger' is coloured 'dark yellow' to make it visible yet not intrusive when viewing the site details.
        * See comments above with regard to potential colour blindness impacts of the yellow and green colour mix.
        * The 'drop down' site page options are coloured 'dark yellow' with the current page shown with an 'off-white' background. Note that on a mobile, the drop down lists can prove 'sticky' on selection with touch screen and sometimes go through to the wrong selection.
        * The header image and the carousel images are suitably sized for smaller screens.
      * Desktop / Laptop large screen size
        * The 'Box Content' is effective on wide screens. The Materialize Grid System allows for the 'Box Content' to align horizontally in themes that are consistent on each of the 'Home' and 'Search' pages.
        * The header menu system uses the Materialize 'navbar' functionality with the menu option pages listed to the right.
        * The navbar is coloured 'dark teal' to make it distinctive from the site pages.
        * The menu item list is coloured 'dark yellow' to make it visible yet not intrusive when viewing the site details.
        * The 'drop down' site page options are coloured 'dark yellow' with the current page shown with an 'off-white' background.
        * The header image and carousel images are designed to be larger and 'impactful' on the larger screen size.

  *   ### Interactive Elements
      * The first key feature of the site is the ability for the user to;
         * enter their own list of plants;
         * place their listed plants into collections;
         * define their collections.
      * The second key features of the site is the ability for a user to search for plants;
         * by entering a 'name';
         * by using a filter for required 'colours'; or
         * upload an image from file.
      * Each method returns results that the user can;
         * review and choose to see more details on any particular return;
         * add the plant to their list and to a collection.
         * if the search is based on a Trefle.io search the Trefle.io plant id is also added to the list for cross reference to the database.
      * The user is able to contact us via the 'Contact Us' page.
         * This page has an interactive contact form that the user can complete and submit their details through to us.
         * There is an open text box so that the user can submit comments.
         * When the user submits their details by clicking the 'Send Contact Details' button, a modal pops up to confirm that details have been sent.

  *   ### Future Features
      * If a user adds a plant to their list from the Trefle.io search , it would be useful to link directly back to the Trefle.io database in order to return more of the details on that plant.
      * Increase the number of filter types in searches. Currently only 'colour' is provided but further filters could be included such as 'edible plants', 'soil types', 'plant height', and 'water conditions'.
      * More complex filters could also be provided to include more than one filter type such as 'colour' and 'soil type'.
      * Improve the quality of data returns for a specific plant in searches, either from updated data submissions in the Trefle.io database or supplement the plant data returns from other available databases.
      * Directly link any search to sources for plant purchase from;
          * local suppliers to the user based on geolocation identifiers; and/or
          * create the ability to online purchase from an identified supplier.
      * Provide an option for the user to image capture a plant and store that image in image form. Links to third party databases are possible for this feature such as AWS, Google and Cloudinary.
      * Provide an option for the user to image capture a plant in their garden which takes them directly to pertinent care details for that particular plant.
      * More sophisticated features include image identifying plants say at a garden centre and being able to compare the plant growing requirements to a users own garden conditions such as light, soil type, water, ph etc.
      * The **Calendar Feature** has proven difficult to implement as information to support this appears lacking in the plant world. Most plant and gardening information providers appear to have their own databases to support this kind of feature as a Unique Selling Product (USP). The Trefle.io database has some details such as 'bloom months' and 'sowing months'. However, this data is not complete. The feature could be added as a future feature on the site.
      * Amend the cards to ensure appropriate rendering on screen sizes at 280px size.
      * Social media icons link to respective social media website home pages. Social media links will in future feature link directly to RMC Ltd social media connections.
      * Note that at present there is no functionality for a user to delete their account. This can be provided as a future feature.

## Technologies Used

### Languages Used

*   [HTML5](https://en.wikipedia.org/wiki/HTML5)
*   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
*   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
*   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Database Used
* [MongoDB](https://www.mongodb.com/cloud/atlas)
  * MongoDb was used to store user data, user plant and collection lists for 'CRUD' purposes.
  * The database was planned to be as simple as possible with three MongoDB collections;
    1. Users - for user registration and login;

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_user.png?raw= "Users")
    1. Collections - for users to record their plant lists in their user defined collections;

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_collection.png?raw= "Collection")
    1. Plants - for users to record their plants as a complete list and divide these lists into their respective collections. Note that for any images in the database, they are referenced as an HTTP/HTTPS link only.

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_plant.png?raw= "Plant")

  * All plants in the database are directly referenced with the Users ObjectId and a Collection ObjectId.
  * All collections are directly referenced to a User ObjectId.

  * A key feature of the site is for users to reference the [Trefle.io](https://Trefle.io/) and [Plant.id](https://plant.id/) search capabilities and then upload the data from [Trefle.io](https://Trefle.io/) into their plant list. However, plants can be added to the user list manually, or by utilising the [Trefle.io](https://Trefle.io/) search functionality.
  * Images can be uploaded to MongoDB but only in an HTTP/HTTPS referenced form. The database is not designed to hold large images in standard image formats such as JPEG. As such all images are 'referenced' in this way. If a user wishes to upload an image, the user can if the user references a third party website or database.
  * Note that at present there is no functionality for a user to delete their account, but will be included as a future feature.


### Frameworks, Databases, Libraries & Programs Used

* [Materialize 1.0.0](https://materializecss.com/)
  * Bootstrap was used to assist with the responsiveness and styling of the website.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * Flask was used to generate the front end web page design, using python as the primary back end programming language.
* [MongoDB](https://www.mongodb.com/cloud/atlas)
  * MongoDb was used to store user data, user plant and collection lists for 'CRUD' purposes.
* [Hover.css:](https://ianlunn.github.io/Hover/)
  * Hover.css was used on the contact details types and for social media icons in the footer to add the float transition while being hovered over.
* [Font Awesome:](https://fontawesome.com/)
  * Font Awesome was used for the website to add icons for aesthetic and UX purposes.
* [jQuery:](https://jquery.com/)
  * jQuery came with Materialize to make the navbar responsive but was also used to support JavaScript and is loaded from the [CDJNS](https://cdnjs.com/libraries/materialize).
* [GitPod:](https://www.gitpod.io/)
  * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
  * GitHub is used to store the projects code after being pushed from Git.
* [Heroku:](https://www.heroku.com/)
    * Heroku is used to host the live site.
* [Atom:](https://atom.io/)
  * Atom was used as a Markdown Text Editor for README.md and Testing.md
* [Emailjs:](https://www.emailjs.com/)
  * Emailjs is used to send the email from the contact form on the 'Contact Us' page.
* [Favicon.io:](https://favicon.io/)
  * Favicon.io was used for Favicon :seedling: web page title images.
* [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
  * Photoshop was used to resize images and edit photos for the website.
* [GitPod IDE Markup:](https://www.gitpod.io/)
  * GitPod IDE markup was used to format HTML files. This easy to use and makes the code very easy to read. I understand this to be VS Code standard.
* [Adobe Stock:](https://stock.adobe.com/uk/)
  * Adobe Stock was used as a library source for images.
* [Unsplash:](https://unsplash.com/)
  * Unsplash was used as a library source for images.
* [Balsamiq:](https://balsamiq.com/)
  * Balsamiq was used to create the [wireframes]() during the design process.
* [Am I Responsive:](http://ami.responsivedesign.is/#)
  * Am I Responsive was used to test the page layouts during the build process;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_succ.png?raw= "Am I Responsive")

### Application Programming Interfaces (API's) Used

* The website sources data from the **[Trefle.io](https://Trefle.io/)** and the **[Plant.id](https://plant.id/)** databases. The API's provide search capabilities for users to identify plants in a number of ways.

 * [Trefle.io](https://Trefle.io/)
   * The [Trefle.io](https://Trefle.io/) database was used as the primary search database for a user;
     * entering a 'name'; or
     * by using a filter by 'colour'.

 * [Plant.id](https://plant.id/)
   * The [Plant.id](https://plant.id/) database was used as the source for plant searches based on a user image. Images can be captured directly from a mobile device or by file upload.

## Site Construction

* ### Consistent Page Components
   * All pages of the site contain the same 'header', 'navbar', 'carousel' and 'footer';
     * **Header** consists of a title carousel images with titles.
     * **Navbar** is a menu top bar dark yellow coloured lettering. There is a light backdrop highlighting the page that the user is on. The menu allows for easy access to any of the pages at all time. On mobile devices, the menu becomes a 'hamburger' and must be 'touched' in order to select any of the pages.
     * **Carousel** The main 'title' header image is carousel images. These images are large and designed to create visual impact, especially as they scroll through from one to the other. The images are the same for all pages. The images have been selected to represent the 'Plant Kingdom'.
     * **Footer** The footer is displayed on all pages and is consistent. There are three sections **'About'** - describes 'us' as an organisation, **'Data Analysis and Presentation Requirements?'** - describes what we do, and **'Contact'** - describes how to contact **'us'** to discuss what we can do for **'you'**.
* ### Home Page
   * Information Box
     * Contains the details as to the intention of the site and a how it can be used. It contains basic information in each card to explain the key features of the site;
       * User defined plant lists;
       * User defined collections lists;
       * Search functions by name, filter and image upload;
       * Register function for new users;
       * Login for registered users.
* ### Subsequent Pages
  * All subsequent pages follow a common theme (using Materialise CSS for font and colours);
    * Main Header Title in 'Yellow';
    * Card in 'Teal' background with information text in 'Dark Teal'.

* ### Contacts Page
   * The Contacts Page contains the 'Contact Form' for a user to supply contact information and to provide comments, questions or to provide a request for some work.
   * The 'Contact Form' will generate an email by referencing the **sendemail.js** file when a user submits their information.

* ### Construction Table
   * The following table provides a summary of how the Site Pages and Sections are compiled;
       Site Page | Page Section | Python File / Code Lines | JS File / Code Lines | API Reference |
       ----------|--------------|-----------------|-----------|---------|
       All | Carousel | N/A  | script.js / 7, 19 - 23 |N/A |
       All | Navbar | N/A  | script.js / 2 - 6 |N/A |
       Home | Card Boxes | app.py / 40 - 43 | N/A |N/A |
       Register | Card Box | app.py / 213 - 237 | N/A |N/A |
       Login | Card Box | app.py / 240 - 267 | N/A |N/A |
       Logout | Card Box | app.py / 282 - 287 | N/A |N/A |
       Plant List | Card Box | app.py / 51 - 54 | N/A  |N/A |
       Add / Update Plant | Add | app.py / 57 - 134 | script.js / 11 - 18 |N/A |
       Collection List | Card Box | app.py / 137 - 152 | N/A |N/A |
       Add / Update Collection | Add | app.py / 155 - 210 | script.js / 11 - 18 |N/A |
       Trefle Search | Search by 'name' | app.py / 321 - 476 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
       Trefle Filter | Filter by 'colour' | app.py / 538 - 683 | script.js / 53 - 63  |[Trefle.io](https://Trefle.io/) (Website) |
       Trefle Plant Details | Search / Filter Return | app.py / 504 - 535 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
       Add Trefle Plant Details | Add | app.py / 479 - 501 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
       Plant.id Search | Plant.id 'image upload' | app.py / 686 - 758 | image_upload.js |[Plant.id](https://plant.id/) (Website) |
       My Details | Card Box | app.py / 290 - 318 | N/A |N/A |
       Contact | Contact Form |N/A| sendemailjs.js | [Emailjs](https://www.emailjs.com/) (Website)|

## Testing
Testing information can be found in a separate [testing.md](https://github.com/Readri205/MS3_Plant_Manager/blob/master/testing.md) file.
### Known Bugs and Issues
* The python file 'app.py' could be rationalised into key functional items such as 'user, Trefle search and Plant.ID search' to make them more distinct and easier to reference specific functionality in the future.
* Likewise the templates could be rationalised into key functional folders such as 'user, Trefle search and Plant.ID search' to make them more distinct and easier to reference specific functionality in the future.
* Trefle search and filter functionality proved 'difficult' with reference to API pagination. The Trefle database restricts returns to 20 items per page. Identifying distinct pages and presenting them proved difficult even with the 'Shamrock' library, and as such there are a number of Trefle search and filter pages to accommodate pagination from the API return. As the current structure 'works' in terms of presentation (no impact to users), it was decided to submit as is and update the functionality at a later point.
* Note that on a mobile device the 'collections' drop down creates a 'mobile' type drop down selection that can be confusing initially, compared to a desktop drop down. It's a bit clunky but it works.
* Note that on a mobile, the drop down lists can prove 'sticky' on selection with touch screen and sometimes go through to the wrong selection. Again, this can be 'annoying' initially. Further review can look to resolve this for user aesthetics.
* Note that at present there is no functionality for a user to delete their account, but would be provided as a future feature.
* Note that the background, carousel and main home page cards all reference  [© Unsplash.com](https://unsplash.com/) for the images. As this is the case there is a risk that an image could be removed from the source and so the site image would fail. Copies of images are retained in the project image folder for backup.
* GitPod IDE markup was used to format HTML files. This easy to use and makes the code very easy to read. I understand this to be a VS Code standard.
* In the Heroku deployment, and on a mobile device, in the Trefle Search function, if a user enters a name with an apostrophe in it, the search with fail and report an Error (this issue is unique to Heroku deployment on a mobile device. The search will work on a desktop device or in Heroku Chrome Dev tools for mobile device screen sizes). The issue was discussed with CI Tutor Support with the suggestion to record the issue in the README.md file;

  * example of type of search;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/problem_search.png?raw= "Mobile Problem Search")

  * example of the error return;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/value_error.png?raw= "Mobile Device Error")

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following process;

1. The project was written in [GitPod](https://www.gitpod.io/) and pushed to GitHub Pages ready for deployment by taking the following steps;
1. Logged in to GitHub and located the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager);
1. From this point deployment was made linking the Github repository to Heroku;

### Heroku Deployment

1. The application was deployed in Heroku to run the Python Application on the Web front end.
1. An account was created in Heroku and then a new application was setup;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_new_app.png?raw= "Heroku New App")

1. In the 'Deploy' menu the Heroku application is connected to the Github Repository so that it is automatically updated when Github is deployed;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_github_deploy.png?raw= "Github to Heroku Deploy")

1. In the 'Settings' menu, all the relevant API token, Secret Key and config files are entered individually so that the application can run with reference to these inputs;

  * The application configs are set in the app.py file for reference;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_configs.png?raw= "Heroku Configs")

  * Heroku can reference them once they are set in the Config Vars. All the tokens and secret keys are entered into an environment variable file that is referenced by the offline application and are not uploaded to Github. Any user wishing to copy the application and deploy it will need to obtain and create their own environment variables as listed below;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_app_configs.png?raw= "Heroku App Configs")

1. A requirements file must be set in the Github application which is passed to Heroku so that it knows which libraries to run;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_reqv2.png?raw= "Heroku Deployment")

1. A 'Proc' file must also be set in the Github application which is passed to Heroku so that it knows which programme to run the web application;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_proc.png?raw= "Heroku Deployment")

1. The application is opened on the web by clicking on the "Open app" button;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_deployment.png?raw= "Heroku Deployment")

 - [Click to view site **GARDEN MANAGER** :seedling:](https://plant-manager-flask-mongodb.herokuapp.com/ "Heroku Deployed Site")

### Forking the GitHub Repository

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and  changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager);
1. At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
     ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/github_fork.png?raw= "Github Fork"); and
1. Click to create a copy of the original repository in your own GitHub account.

### Making a Local Clone

1. Log in to **GitHub** and locate the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager)
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, click the top right hand link click "Use HTTPS";
1. Copy the link under "Clone with HTTPS";
     ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/github_clone.png?raw= "Github Clone")
1. Open your Code Editor and access the appropriate process to paste the clone link;
1. Change the current working directory to the location where you want to keep the cloned directory;
1. Paste the URL you copied in step 4 above.

Note that different Code Editors will have different processes for making the clone once the HTTPS link copy is made in step 4 above.

 * If using **GitHub Desktop**, the clone can de saved directly into GitHub Desktop from the "Code" dropdown menu by choosing **'Open with GitHub Desktop'**.

A **Zip File** clone can be downloaded from the same "Code" drop down above;
 * Select **'Download ZIP'** and the complete zip file will be saved to you local computer.

## Credits

### Code

* My Mentor (Adegbenga Adeye (email:adegbenga.adeye@outlook.com, slack:gbenga_mentor)) for providing help, guidance, inspiration and input on the more challenging components.
* [Code Institute course](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute%20%2Bcourses&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-443742237303&hsa_ad=407017470923&hsa_acc=8983321581&hsa_grp=62188641040&hsa_mt=b&hsa_cam=1578649861&hsa_kw=%2Bcode%20%2Binstitute%20%2Bcourses&hsa_ver=3&hsa_src=g&gclid=CjwKCAjw4MP5BRBtEiwASfwAL3-Oi3uDo1sBfn2KpQVAlLb07T2ndP-Q2mCFxdGgpvoBMoPIAtbg9xoCyZgQAvD_BwE&gclsrc=aw.ds); (the 'Task List' example) by Tim Nelson for the [Flask](https://flask.palletsprojects.com/en/1.1.x/) / [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) / [MongoDB](https://www.mongodb.com/cloud/atlas) / [Materialize](https://materializecss.com/) example which is used for the base construction of this website.
* (the [Emailjs](https://www.emailjs.com/) example) for the 'Contact Form' email return function used in this website.
* Code for the Carousel was from [Learning Simplified](https://youtu.be/re2W7o6IsYo), a youtube channel doing some good things with the [Materialize 1.0.0](https://materializecss.com/) Library.
* [Julian Nash](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA) provided me with lots of useful tips for Flask and Python programming. The youtube videos are easy to follow and understand and are backed up with useful documentation.

## Content

* All content was written by the developer.

### Media

* All images [© Unsplash.com](https://unsplash.com/) unless otherwise stated;
 *   Background image - ['Dark plants ...''](https://unsplash.com/photos/aDvrHHFGAlE) By Amir Nyct [© Unsplash.com](https://unsplash.com/);
 *   Carousel image - ['Orchid in Bloom'](https://unsplash.com/photos/1PJnrGd6K1w) By Sanni Sahil [© Unsplash.com](https://unsplash.com/);
 *   Carousel image - ['Spring Red Tulips on Moody Background'](https://unsplash.com/photos/gH5ujsvtohE) By Michele Tardivo [© Unsplash.com](https://unsplash.com/);
 *   Carousel image - ['Floral Potrait...'](https://unsplash.com/photos/-yYaO0ioyOY) By Abhishek Dhakate [© Unsplash.com](https://unsplash.com/);
 *   Carousel image - ['Singapore Botanic Gardens, Singapore'](https://unsplash.com/photos/fQQBArliXGE) Elliot Lowe [© Unsplash.com](https://stock.adobe.com/uk/);
 *   Home page card image - ['Hazleton, United States'](https://unsplash.com/photos/Q2dxmAzbUbk) Honey Yanibel Minaya Cruz [© Unsplash.com](https://stock.adobe.com/uk/);
 *   Home page card image - ['Mystic Hydrangea'](https://unsplash.com/photos/FOrCwEMIgSI) Natasha Polyakova [© Unsplash.com](https://stock.adobe.com/uk/);
 *   Home page card image - ['Deep Red Leaves'](https://unsplash.com/photos/mdNQ3R5dT6w) Jessica Fadel [© Unsplash.com](https://stock.adobe.com/uk/);
 *   Home page card image - ['Pink Flowers'](https://unsplash.com/photos/ia1eeRnsbLg) Annie Spratt [© Unsplash.com](https://stock.adobe.com/uk/);

### Acknowledgements

* My Mentor **Adegbenga Adeye**, (email: adegbenga.adeye@outlook.com, slack:gbenga_mentor) for continuous helpful feedback. Ade has been an amazing in helping and supporting me with this site. It has proven much harder and much more work for me to develop than I ever thought (severe case of 'what you don't know when you start').
* **Tutor support** at Code Institute for their support. When I have requested help, it has come quickly and efficiently when needed.
* **Student assessment** at Code Institute. I have looked to accommodate comments back on MS2 to reduce any re-occurring issues in MS3.
* **Other students** (Slack Code Institute Workspace) on the Full Stack Developer Course, via the [Slack Communication Platform](https://slack.com/intl/en-gb/).
* **Friends and family** providing review and feedback on the site content, navigation and screen size testing. This has been invaluable with two very 'have mobile, will travel' daughters, it is often brutal but effective.

## Version Control

*   All through the development phase of the project, commits have been made from the GitPod Repository to GitHub. The version control list below mirrors the GitHub Commit list. It is designed to provide a direct track on commits in the README file for easy access as to code status in GitPod.

   - V1.0 Initial Commit
   - V1.1 Add requirements.txt
   - V1.2 Add Procfile
   - V1.3 Add MONGO_URI config in heroku
   - V1.4 Add app.route for MongoDB connection
   - V1.5 Add plants.html collections.html
   - V1.6 Add materialize design link and scripts
   - V1.7 Add plants list in collections
   - V1.8 Add add_plant.html and update collections.html
   - V1.9 Add additional fields to database, update add_plant.html
   - V2.0 Add insert_plant function in app.py
   - V2.1 Add insert_collection function, addcollections.html
   - V2.2 Add description, date added to collections.html, addcollections.html
   - V2.3 Amend collections.html for drop down to show details and edit buttons
   - V2.4 Add drop down collection details to addcollections.html
   - V2.5 Amend '/addplants' to 'collections' from 'plants'
   - V2.6 Remove name='action' in addplants.html submit button
   - V2.7 Add edit function to plants
   - V2.8 Add delete to plants, update and delete for collections
   - V2.9 Add navbar
   - V3.0 Adjust navbar for menu items
   - V3.1 Add hamburger menu for small screens
   - V3.2 Add font awesome icons for menu
   - V3.3 Add css style js script pages user register page
   - V3.4 Add secret key for user registration
   - V3.5 Add login for users
   - V3.6 Add flash messages on login and register
   - V3.7 Move js scripts to script file
   - V3.8 Add user profile page on registration and login
   - V3.9 Add user logout functionality
   - V4.0 Update hamburger menu to dark yellow colour
   - V4.1 Add icon in burger menu and menu text shadows
   - V4.2 Remove container div on navbar for mobile screens
   - V4.3 Move burger menu to right and amend font size in burger menu
   - V4.4 Add user profile to plants added and edited plants
   - V4.5 Add user profile to collections and edited collections
   - V4.6 Update html pages with appropriate row structure
   - V4.7 Update editplants.html row structure
   - V4.8 Remove matfix2 materialize eventlistener
   - V4.9 Update to materialize 1.0.0
   - V5.0 Remove matfix id's for materialize
   - V5.1 Update data-target in navbar for materialize 1.0.0
   - V5.2 Update for select dropdown validation code by timnelson @tim_ci
   - V5.3 Set up new Home landing page
   - V5.4 Add Register and Login buttons on Home page
   - V5.5 Restrict my plants list to list created by user
   - V5.6 Restrict my collections to list created by user
   - V5.7 Update home page with header image and remove plant lists
   - V5.8 Remove old base and script file and move image to body
   - V5.9 Update mobile menu for home and my plants page
   - V6.0 Amend menu font size for small screens
   - V6.1 Remove brand-logo class on main menu
   - V6.2 Add card panels to home page
   - V6.3 Add fixed navbar
   - V6.4 Expand register details for names email and phone
   - V6.5 First update to show user profile details
   - V6.6 Add user details page
   - V6.7 Add Trefle endpoints and token
   - V6.8 Add Trefle html and app route
   - V6.9 Amend menu for logout last
   - V7.0 Update Procfile and requirements.txt
   - V7.1 Update Procfile
   - V7.2 Update for home page
   - V7.3 Update env file for IP and PORT
   - V7.4 Update Heroku dynos
   - V7.5 Update for index home page
   - V7.6 Update for new requirements.txt
   - V7.7 Further update for requests module
   - V7.8 Update app.py take out print code
   - V7.9 Amend app for get Trefle search
   - V8.0 Further amend app for search
   - V8.1 Amend styles in html pages
   - V8.2 Add more styles to html pages
   - V8.3 Update Procfile for flask
   - V8.4 Revert Procfile change
   - V8.5 Updadte get Trefle search page
   - V8.6 Amend Procfile python3 to python
   - V8.7 Add Trefle token to heroku amend navbar and style
   - V8.8 Amend navbar style on burger menu
   - V8.9 Redirect register page on front menu
   - V9.0 Amend style in base navbar title
   - V9.1 Start App for pagination on search
   - V9.2 Update drop down icons for duo tone
   - V9.3 Collapse type updates from repositories
   - V9.4 Add testbed for API pagination
   - V9.5 Amend syntax in app file
   - V9.6 Redeploy to GitHub on lockup
   - V9.7 Redeploy to Heroku
   - V9.8 Add function to extract pages and total
   - V9.9 Amend card size in Trefle search
   - V10.0 Amend card size on card search large screen
   - V10.1 Add page links and styles to Trefle search page
   - V10.2 Amend card size Trefle search
   - V10.3 Add pagination function
   - V10.4 Adjust to page=2 for Trefle search
   - V10.5 Amend card size for Trefle search
   - V10.6 Add footer box and draft script and style
   - V10.7 Amend home card style two cards large screens
   - V10.8 Add search box and style changes
   - V10.9 Add style to search and page box
   - V11.0 Add style to contact box link
   - V11.1 Add pagination function test
   - V11.2 Update search function
   - V11.3 Update pagination search function
   - V11.4 Amend pagination search function
   - V11.5 Update pagination search function
   - V11.6 Amend pagination search function
   - V11.7 Add Trefle_many get function test
   - V11.8 Add Trefle searches pages htmls
   - V11.9 Add get_next first test
   - V12.0 Update search test
   - V12.1 Update search for first and last page
   - V12.2 Add Plant.ID to search function
   - V12.3 Add target blank redirect in url wiki search
   - V12.4 Move Plant.ID key to env variables
   - V12.5 Add home page content, similar images Plant.ID
   - V12.6 Update home page content
   - V12.7 Move logout to my details drop down
   - V12.8 Add carousel to user details page
   - V12.9 Amend text in home page
   - V13.0 Amend carousel in user details page
   - V13.1 Amend carousel to full width
   - V13.2 Add carousel to base, autoplay and images
   - V13.2 Amend footer styles
   - V13.3 Amend background image and opacity
   - V13.4 Amend carousel image height
   - V13.5 Upload favicon image
   - V13.6 Add Trefle API search function
   - V13.7 Update first Trefle API page
   - V13.8 Amends to Trefle search
   - V13.9 Amend search and remove webmanifest favicon
   - V14.0 Update Trefle filter searches
   - V14.1 Upload favicon images and links
   - V14.2 Update favicons
   - V14.3 Update to search function
   - V14.4 Test for filter function
   - V14.5 Update test filter function
   - V14.6 Add update filter test
   - V14.7 Add search test for plant id
   - V14.8 Add image upload test
   - V14.9 Add edit user - part
   - V15.0 Add edituser amends
   - V15.1 Remove PIL
   - V15.2 Add cloudinary db and file upload
   - V15.3 Amend image route path for plant id
   - V15.4 Add tests to cloudinary image db
   - V15.5 Update config variables in heroku
   - V15.6 Update heroku with line 630 amend
   - V15.7 Add cloudinary script file to my images
   - V15.8 Update style cloudinary image upload button
   - V15.9 Update my_images page for cloudinary images
   - V16.0 Amend for my_images test errors
   - V16.1 Amend for my_images errors
   - V16.2 Fix cloudinary images in my_images
   - V16.3 Move cloudinary widget to js file
   - V16.4 Remove test script from heroku deployment
   - V16.5 Amend cloudinary code for efficiency
   - V16.6 Update cloudinary api call code
   - V16.7 Further cloudinary api code amend
   - V16.8 Remove upload flask code
   - V16.9 Amend cloudinary api code
   - V17.0 Further amend to api code
   - V17.1 Further amend to api code
   - V17.2 Add cloudinary to requirements
   - V17.3 Amend for import requests
   - V17.4 Add requests to requirements file
   - V17.5 Update requests version
   - V17.6 Further update cloudinary heroku test
   - V17.7 Further amend cloudinary heroku test
   - V17.8 Additional cloudinary heroku test
   - V17.9 CI Heroku test commits
   - V18.0 CI heroku test commit 2
   - V18.1 CI heroku test commit 3
   - V18.2 CI heroku test commit 4
   - V18.3 CI heroku test commit 5
   - V18.4 CI heroku test commit 6
   - V18.5 CI heroku test commit 7
   - V18.6 CI heroku test commit 8
   - V18.7 CI heroku test commit 9
   - V18.8 Cloudinary api syntax heroku test
   - V18.9 Remove redundant filters, add cloudinary functions
   - V19.0 Update cloudinary functions
   - V19.1 Update mongo user update and referencing
   - V19.2 Update cloudinary upload widget scheme
   - V19.3 Amend pages to follow same name structure sequence
   - V19.4 Amend card text font and image sizes
   - V19.5 Add scientific name to plant cards
   - V19.6 Add wiki links to cards
   - V19.7 Title update GLM
   - V19.8 Adjust image height for small screens
   - V19.9 Adjust card size for small screens
   - V20.0 Amend styles for wiki links and profile page
   - V20.1 Amend search row size on Trefle search
   - V20.2 Amend site title
   - V20.3 Amend cloudinary image upload styles
   - V20.4 Update wiki plant links in Trefle search
   - V20.5 Update for cloudinary destroy method
   - V20.6 Update for next_page testing
   - V20.7 Amend wiki links to scientific names
   - V20.8 Add page iteration test code
   - V20.9 Update for page iteration test
   - V21.0 Update css styles on cards
   - V21.1 Add direct Trefle plant upload
   - V21.2 Amend add Trefle plant descriptors
   - V21.3 Add plant details search in app
   - V21.4 Amend add Trefle plant for collections input
   - V21.5 Amend page numbers on search
   - V21.6 Amend page number structure for search
   - V21.7 Amend page numbers for 3 pages and less
   - V21.8 Add cloudinary delete image function
   - V21.9 Amend cloudinary delete function syntax
   - V22.0 Update cloudinary image tags
   - V22.1 Amend cloudinary image tag style
   - V22.2 Delete old Trefle html pages
   - V22.3 Add plant details html page
   - V22.4 Add plant detail styles to html page
   - V22.5 Update plant detail styles
   - V22.6 Update styles on plant details
   - V22.7 Remove duplicate bloom months in details
   - V22.8 Amend spelling and plant detail styles
   - V22.9 Amend home page image to daisy
   - V23.0 Switch url direction from Plant ID page
   - V23.1 Add Trefle filter searches
   - V23.2 Update Trefle filter search
   - V23.3 Updates to Trefle filter page search
   - V23.4 Updated plant details page for no image
   - V23.5 Add tests for Shamrock wrapper for Trefle
   - V23.6 Add plant_id to menu in base
   - V23.7 Update requirements file
   - V23.8 Update detail for plant.id search
   - V23.9 Amend % for similarity in plant.id search
   - V24.0 Add styling to plant.id similarity cards
   - V24.1 Trefle page number tests on filters
   - V24.2 Image upload function in plant.id page
   - V24.3 Amend image upload function
   - V24.4 Amend plant.id return for null values
   - V24.5 Update plant.id image upload script
   - V24.6 Add testing for plant.id images
   - V24.7 Amend testing for plant.id images
   - V24.8 Amend for further plant.id testing
   - V24.9 Further plant.id image testing
   - V25.0 Add image test for plant.id
   - V25.1 Update get_plant_id method
   - V25.2 Add README update
   - V25.3 Further README updates
   - V25.4 Update README for functionality
   - V25.5 Update README for website purpose
   - V25.6 Update for first time user stories
   - V25.7 Update README for Design
   - V25.8 Update README for languages, programmes, libraries
   - V25.9 Update README code credits
   - V26.0 Update README for wireframe and features
   - V26.1 Update README for APIs
   - V26.2 Update README for Site Construction
   - V26.3 Further README updates for Site Construction
   - V26.4 Remove old images from README
   - V26.5 Format amends on README
   - V26.6 Further format amends on README
   - V26.7 Add contact us form
   - V26.8 Align plant.id images vertically
   - V26.9 Add margin to Trefle search buttons
   - V27.0 Amend static image in plant.id page
   - V27.1 Amend contact form placeholders to light teal
   - V27.2 Amend home page for my year to search engines
   - V27.3 Update main carousel images
   - V27.4 Change second carousel image and text
   - V27.5 Update search page numbers
   - V27.6 Remove cloudinary image functions
   - V27.7 Amend image search to python code from JS
   - V27.8 Amend image search to remove temporary files
   - V27.9 Update heroku for image file path
   - V28.0 Update heroku for plant_id directory
   - V28.1 Amend plant details page layout
   - V28.2 Update plant details page layout
   - V28.3 Update image search with if defence
   - V28.4 Update image search if statement
   - V28.5 Update css plant image sizes for media
   - V28.6 Update css styles for contact box
   - V28.7 Update media queries with important for heroku
   - V28.8 Update for Trefle details image auto refresh
   - V28.9 Update image in Trefle plant details
   - V29.0 Add search function to plant.id image search page
   - V29.1 Update search function with submit value
   - V29.2 Amend media image sizes in plant.id return
   - V29.3 Center file image upload in plant.id
   - V29.4 Update media image size in Trefle details page
   - V29.5 Amend plant details and image upload styles
   - V29.6 Amend styles in wiki search button position in plant.id page
   - V29.7 Amend plant.id image upload style
   - V29.8 Amend plant.id upload image size
   - V29.9 Further plant.id upload image sizing
   - V30.0 Change to materialize responsive image format
   - V30.1 Test 50% max width on plant.id image upload
   - V30.2 Style amends in plant_deets page for search bar
   - V30.3 Split search function media screen sizes
   - V30.4 Trial dark background
   - V30.5 List plants in collections
   - V30.6 Amend collections sorts for plants
   - V30.7 Add collection id to plant
   - V30.8 Amend family_name errors
   - V30.9 Update main search page
   - V31.0 Update Trefle filter search
   - V31.1 Amend filter search page numbers
   - V31.2 Amend Trefle search page numbers
   - V31.3 Add defensive code for Trefle API fail
   - V31.4 Add information for plant_id image loads
   - V31.5 Update Trefle information on search and filter pages
   - V31.6 Amend filter page numbers for first page on next filter
   - V31.7 Add button for plant details on filter pages
   - V31.8 Add web link to Trefle image on search page
   - V31.9 Amend typo in plant id page text
   - V32.0 Amend Trefle image web link on filter pages
   - V32.1 Amend pages in filter and search
   - V32.2 Amend filter checkbox styles
   - V32.3 Amend filter for first page
   - V32.4 Standardise all pages with yellow text header
   - V32.5 Update plants list pages with standard headers
   - V32.6 Change header images and titles
   - V32.7 Amend home page header styles
   - V32.8 Update header images and add references to Unsplash
   - V32.9 Amend all headings to standardize
   - V33.0 Amend page headers to standardize
   - V33.1 Remove card links on home page
   - V33.2 Add header spaces
   - V33.3 Amend plant names in collection to title case
   - V33.4 Amend header sub title spacing
   - V33.5 Add space for header image title
   - V33.6 Amend home page card images
   - V33.7 Amend home page images and add artist links
   - V33.8 Amend main background image
   - V33.9 Add Unsplash reference for background image
   - V34.0 Amend contact and Trefle details header to standardize
   - V34.1 Update amiresponsive and header readme images
   - V34.2 Update readme contents
   - V34.3 Adjust readme format
   - V34.4 Update readme notes
   - V34.5 Update image refs in readme
   - V34.6 Update readme content for image links
   - V34.7 Update for typos and move readme images
   - V34.8 Update header images in readme with titles
   - V34.9 Update Github Deploy in readme
   - V35.0 Update readme for MongoDB details
   - V35.1 Amends for mongoDB details
   - V35.2 App.py clean up
   - V35.3 First testing.md upload
   - V35.4 First cleanup of testing.md file
   - V35.5 Update main header image in testing.md
   - V35.6 Update with JSHint tests
   - V35.7 Update for CSS tests
   - V35.8 Update for html base file check
   - V35.9 Add Heroku deployment method
   - V36.0 Update Heroku Deployment
   - V36.1 Update readme text and github/heroku deployment
   - V36.2 Add GDPR disclaimer
   - V36.3 Amended personal details disclaimer
   - V36.4 Amended readme text
   - V36.5 Update Trefle header image
   - V36.6 Add functional user testing in testing.md
   - V36.7 Add highlight to Trefle and Plant.ID API in readme
   - V36.8 Update contents
   - V36.9 Add screen size tests in testing.md
   - V37.0 Amend galaxy 653 screen image link
   - V37.1 Update search pages with main search button
   - V37.2 Testing replace ' . - in query search
   - V37.3 Change int for float on mobile trefle search
   - V37.4 Remove prev_page from first search function
   - V37.5 Add prev_page and update remove ' query
   - V37.6 Add images for user stories
   - v37.7 Add more images for user stories
   - V37.8 Add further image to user stories
   - V37.9 Upload mobile images for user stories
   - V38.0 Add mobile image upload name
   - V38.1 Add contact us email confirmation test images
   - V38.2 Update construction box in readme
   - V38.3 Amend css styles, app code and readme txt
   - V38.4 Rationalise images and image folders
   - V38.5 Update construction box for js code lines
   - V38.6 Update construction box for my details code lines
   - V38.7 Update search field for no symbols or apostrophe's
   - V38.8 Update for debug=False
   - V38.9 Update search field text
   - V39.0 Update debug = True for testing
   - V39.1 Update my_image and thumbnail for plantid search
   - V39.2 Reset plant_image style for plantid images
   - V39.3 Upload my_image in main image folder
   - V39.4 Add uploads folder and my_image in plant_id folder
   - V39.5 Format html text in IDE
   - V39.6 Redeploy to upgrade Heroku-20 stack
   - V39.7 Add readme text on markup HTML
   - V39.8 Replace prev_page with 0 for mobile trefle search
   - V39.9 Replace int with int float for mobile search heroku
   - V40.0 Revert to int only, test fail for mobile
   - V40.1 Amend selfs for base10 integer
   - V40.2 Amend pages for first page trefle search
   - V40.3 Add validation and required for plantid image load
   - V40.4 Add heroku mobile search error details to readme
   - V40.5 Add trefle filter checkbox for at least one check
   - V40.6 Add scriptjs code lines to table for filter search
   - V40.7 Add AMIResponsive image
   - V40.8 Add query back after error delete
   - V40.9 Add API error handles and dying plant error image
   - V41.0 Amend trefle search landing to exclude return examples
   - V41.1 Debug=False tests in heroku, gitpod ports failing
   - V41.2 Update API error page with details
   - V41.3 Amend plant id url connect in api error page
   - V41.4 Text amends to trefle pages and api error page
   - V41.5 Amend text styling on api error page
   - V41.6 Further amends to styles on api error page
   - V41.7 Amend for mobile search text on trefle search page
   - V41.8 Add mobile search text to all trefle search pages
   - V41.9 Split api error page types 400 500
   - V42.0 Amend wording for error type returns
***
