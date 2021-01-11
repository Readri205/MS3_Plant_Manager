![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/amiresponsive.png?raw= "Garden Manager")

[View the live **GARDEN MANAGER**  :seedling:  project here.](https://plant-manager-flask-mongodb.herokuapp.com/)

![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/perennial254287.jpg?raw= "Garden Logo")

# **GARDEN MANAGER :seedling:**

## Contents

* [Site Goals](#site-goals)
* [User Experience (UX)](#user-experience--ux-)
  + [User stories](#user-stories)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [Frequent User Goals](#frequent-user-goals)
    - [Mobile Menu](#mobile-menu)
  + [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Box Content Structure](#box-content-structure)
    - [Imagery](#imagery)
  + [Wireframes](#wireframes)
    - [Original Wireframe Design (July 2, 2020).](#original-wireframe-design--july-2--2020-)
    - [Actual Site Design.](#actual-site-design)
* [Features](#features)
  + [Responsive for Device Size](#responsive-for-device-size)
  + [Interactive Elements](#interactive-elements)
  + [Future Features](#future-features)
* [Technologies Used](#technologies-used)
  + [Languages Used](#languages-used)
  + [Frameworks, Libraries & Programs Used](#frameworks--libraries---programs-used)
  + [Application Programming Interfaces (API's) Used](#application-programming-interfaces--api-s--used)
* [Site Construction](#site-construction)
  + [Consistent Page Components](#consistent-page-components)
  + [Home Page](#home-page)
  + [Country Details Page (Nigeria has been used by way of example)](#country-details-page--nigeria-has-been-used-by-way-of-example-)
  + [Contacts Page](#contacts-page)
  + [Construction  Table](#construction--table)
* [Testing](#testing)
  + [Known Bugs and Issues](#known-bugs-and-issues)
* [Deployment](#deployment)
  + [GitHub Pages](#github-pages)
  + [Forking the GitHub Repository](#forking-the-github-repository)
  + [Making a Local Clone](#making-a-local-clone)
* [Credits](#credits)
  + [Code](#code)
  + [Content](#content)
  + [Media](#media)
  + [Acknowledgements](#acknowledgements)
* [Version Control](#version-control)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Site Goals

* This website provides a functional site that allows users to create a list of plants in collections, either by entering plant details or by uploading from a search. The searches can be made in a number of ways, including by name, image or by filters. Users are able to update the details of plants and collections in their lists. Users are also able to delete plants and collections. A user can also move a plant from one collection to another if so desired. A user can also amend their personal details including email, username and telephone number. A user is also able to fully delete their login and all plants and collections listed on that login. Each users logn and details are specific to that user and cannot be viewed by any other user.

* The website is **'functional'**, allowing users to enter information about **Plants** and to view information on specific plants. The site is designed to show details on **Plants** where required.
* The website concept is to provide a user with a useful list of plants;
  * what is the name of the plant?
  * what are the scientific names and details?
  * what collection do I have the plant in?
* The structure for the **Plants** is provided by;
  * a list of **plants** entered by and for, a specific user;
  * a list of **collections** entered in which plants can be listed;
* The plants to be entered can be made using the following methods;
  * **manual** where a user already has details for a plant, external to the application;
  * **search** to identify a **name** characteristic for a plant;
  * **filter** to identify **colour** characteristics for a plant; and
  * **image** using a computer or mobile device to upload a **file image**.

* The website sources data from the **[Trefle.io](https://trefle.io/)** and **[Plant.id](https://plant.id/)**. The website primarily makes use of Application Programming Interfaces (API's) to construct the plant search data. The **[MongoDB](https://www.mongodb.com/cloud/atlas)** is used to store user data and allows for create, read, update and delete data for plant details and their user login data. API and other data source details are provided in the **'Application Programming Interfaces (API's) Used'** section below.

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

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Scroll Down")

          * be able to easily navigate throughout the site to find content;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Scroll Down on Home Page")

          * view the carousel images just beneath the header;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Landing Page")

          * scroll down through the information, read the content, view each of the function cards;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Scroll Down on Home Page")

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Scroll Down on Home Page")

          * register for the site and create login credentials;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Search Menu")

          * enter plant details for plants they are interested in;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Search Menu")
            * login to the site;
            * immediately view their plants list;
            * view their collections list;
            * scroll down through the information, read the content, view the map of Africa, then view the line graphs and the pie charts;

          * contact us to ask about data projects that they may be interested to have completed as an item of work.
            * Per images above

    *   #### Returning Visitor Goals
        * The returning visitor will want to;
          * login to the site;
          * immediately view their plants list;
          * view their collections list.
        * **A returning visitor** may want to go straight to the 'Country' search function<sup id="a1">[1](#f1)</sup>;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Search Bottom of Home Paget")

          * search the details for a specific country from the dropdown menu;
          * read the information about that country, view the map, zoom in and out on that map, review the line graphs and review the pie charts;
          * search for another country and read the information about that country, view the map, zoom in and out on that map, review the line graphs and review the pie charts;
          * see the data points on the line graphs or pie charts possible with a mouse hover on desktop/laptop, or touch screen on a mobile device.
          * navigate easily back to the 'Home' page;
          * search for another country and read the information about that country;
        * **A returning visitor** may want to go straight to the 'Contact Us' page;
          * contact us for more information or to provide comments about the site;
          * contact us to ask about data projects that they may be interested to have completed as an item of work.

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Contact in Menu Bar")

    *   #### Frequent User Goals
        * The frequent visitor will want to;
          * find any new information supplied;
          * view the carousel images just beneath the header;
          * scroll down through the information, read the content, view the map of Africa, then view the line graphs and the pie charts;
        * **A frequent visitor** may want to go straight to the 'Country' search function<sup id="a2">[2](#f2)</sup>;
          * Scroll down the Home page to reach the 'Search Function';

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Search Bottom of Home Page")

          * search the details for a specific country from the dropdown menu (the site is easy and intuitive to use for a frequent visitor);
          * read the information about that country, view the map, zoom in and out on that map, review the line graphs and review the pie charts;
          * see the data points on the line graphs or pie charts possible with a mouse hover on desktop/laptop, or touch screen on a mobile device.
          * search for another country and read the information about that country, view the map, zoom in and out on that map, review the line graphs and review the pie charts;
          * navigate easily back to the 'Home' page;
          * search for another country and read the information about that country;
        * **A frequent visitor** may want to go straight to the 'Contact Us' page;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Contact in Menu Bar")

          * contact us for more information or to provide comments about the site;
          * contact us to ask about data projects that they may be interested to have completed as an item of work.

    *   #### Mobile Menu
          * On mobile devices the menu is shown as a 'hamburger' drop down;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Mobile Menu")

          * On mobile devices the search function operates in the same manner as for larger screens;  

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/daisy.jpg?raw= "Mobile Search")

*   ### Design
    *   #### Colour Scheme
        *   The main colour is 'Ivory' (#FFFFF0), designed to provide a light neutral background to highlight dark text, line graphs, pie charts, images and the country flags.
    *   #### Typography
        *   The "Roboto" font is the main font used throughout the whole website with Sans Serif as the fallback font in case the font isn't imported into the site correctly. "Roboto" is a clean font which is both attractive and appropriate.
    *   #### Box Content Structure
        *   The box content structure is used to highlight specific messages and themes through the site. This identifies the text high level summaries on the 'Home' and the 'Country Details' page. In addition the box structure is used to highlight the maps, the line graphs and pie charts on the 'Home' and 'Country Details' pages. The 'Contact Us' page uses the same box structure to present the 'contact form'. Each of the boxes has a shadow effect to lift them from the background and to provide a definitive outline for the contained information.
    *   #### Imagery
        *   The header contains an Africa theme with a simple title. The large images in the carousel are designed to be striking and catch the user's attention and to provide some unique image themes from the African continent. To provide some context on larger screens each image has a clear title description sourced from the original image provided by the contributor. Note that on some screen sizes the titles can be difficult to read where they blend into the image. As the titles are not fundamental to the website information it has been considered 'acceptable'. On small screens the image titles are removed, due to space and readability constraints.

*   ### Wireframes
    *   #### Original Wireframe Design (July 2, 2020).
        *   The **'Home'** page includes an **'Information box'**, **'Population and GDP line graphs'**. On scroll down the page would reveal an **'Africa Map'** and an **'Information Table'** listing all 54 countries with their respective **'Population and GDP'** sizes. The **'Information Table'** is intended to be 'clickable' to search for more details on any Country. **'Country Search'** and **'Contact Us'** boxes are also included.
        *   The **'Country Search'** page includes a **Country Name** header title with an image of the **National Flag**, an image of the **Capital City**, an **'Information Table'** of historical **Population and GDP data**, **Country Map** and **Line Graphs** of the same data. **'Country Search'** and **'Contact Us'** boxes are also included.
        * Sources for data were considered as follows;
          1. Maps - [Google Maps](https://console.cloud.google.com/google/maps-apis/)
          1. Africa country codes - [Referential](https://rapidapi.com/referential/api/referential) API via [RapidAPI](https://rapidapi.com/)
          1. Capital City, Population and GDP data - [World Bank Database](https://databank.worldbank.org/home.aspx)
          1. National Flag images - [CountryFlags](https://www.countryflags.io/)
          1. Line and Pie Chart Capability - [Chartsjs](https://www.chartjs.org/)
          1. Automated Email Response - [Emailjs](https://www.emailjs.com/)
        *   The **Original Wireframe Design** can be viewed here - [View](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/wireframes/africa.pdf)
    *  #### Actual Site Design.
        * The developed site uses many of the concepts from the original Wireframe design. Variations are as follows;
          1. The main header image was switch to the 'Africa' header image which conveys a strong but not overwhelming 'Africa' theme;
          1. The **'Contact Form'** was moved to its own page to **declutter** the two main pages. It is accessible from every page either through the main menu or from the footer;
          1. The **Capital City** images were switch to dynamic  **carousel theme** images on all the pages and placed just beneath the main header image. The images are unique and vibrant. If a desktop is left on the site, the images are eye catching due to **vivid colours** and the **carousel movement**;
          1. The **'Information Tables'** were switched to more graphically appealing **Pie Charts** that are easy to read;
          1. The **'Search Function'** remains at the bottom of both the 'Home' and 'Country Details' pages.
        * The above listed sources were utilised, except for [Google Maps](https://console.cloud.google.com/google/maps-apis/). The following were used primarily to provide a learning experience for the developer;
          1. Javascript Library - [Leaflet](https://leafletjs.com/)
          1. Imagery - [Mapbox](https://docs.mapbox.com/mapbox-gl-js/api/)
          1. Data - [OpenStreetMap](https://www.openstreetmap.org)

## Features

*   ### Responsive for Device Size
    * Mobile / Smaller screen size
      * The site is designed primarily for use on a mobile. The 'Box Content' structure using Bootstrap Grid System has been utilised so that the information boxes (text, maps, line graphs, pie charts) will stack vertically on small screens for readability.
      * The menu system uses the Bootstrap 'navbar' functionality for small screens using the 'toggle' capability for the 'drop down' menu list from a 'hamburger' icon.
      * The navbar is 'fixed' to the top of the screen at all times on page scroll down for easy access.
      * The navbar is coloured 'black' to make it distinctive from the site pages.
      * The 'hamburger' is coloured 'off-white' to make it visible yet not intrusive when view the site details.
      * The 'drop down' site page options are coloured 'off-white' with the current page shown as 'white' and 'grey' background.
      * The header image and the carousel images are suitably sized for smaller screens.
    * Desktop / Laptop large screen size
      * The 'Box Content' is effective on wide screens. The Bootstrap Grid System allows for the 'Box Content' to align horizontally in themes that are consistent on each of the 'Home' and 'Country Details' pages.
      * The header menu system uses the Bootstrap 'navbar' functionality with the menu option pages listed to the left.
      * The navbar is coloured 'black' to make it distinctive from the site pages.
      * The menu item list is coloured 'off-white' to make it visible yet not intrusive when view the site details.
      * The 'drop down' site page options are coloured 'off-white' with the current page shown as 'white' and 'grey' background.
      * The header image and carousel images are designed to be larger and 'impactful' on the larger screen size.

*   ### Interactive Elements
    * The key feature of the site is the interactive search for any of the 54 African Countries details returned on the 'Country Details' page.
      * Note that if a user goes from the 'Home' page direct to the 'Country Details' page using the 'navbar' menu, the default Country on the 'Country Details' page is Nigeria.
      * The 'Search' box is found on scroll down through the 'Home' page.
      * The 'Search' box is also found on scroll down through the 'Country Details' page.
      * In each case the user can open the drop down menu and pick a country of their choice. The search will return the details for that country on the 'Country Details' page.
      * The details from the search are returned using a various API sources. The details returned are;
        * First header text box;
          * 'Country Name' as a title;
          * 'Country Flag' as a colour image;
          * Name of the Capital City; and
          * Three text lines with information describing that country relative to the rest of Africa;
            * Land size;
            * population; and
            * GDP.
        * Second header box;
          * returns a map of that country, centred on the capital city. Note that the default zoom level is 6. The user can zoom in to see more country detail, or out to see the country in a wider Africa context.
        * Third and fourth boxes;
          * return the Population and GDP growth from 1970 to 2019.
        * Country Pie charts;
          * return land size, population (2019) and GDP (2019) relative to the rest of Africa.
        * Top 5 Pie charts;
          * return visual detail about the largest 5 countries in terms of land size, Population (2019) and GDP (2019) in Africa.
    * The user is able to contact us via the 'Contact Us' page.
      * This page has an interactive contact form that the user can complete and submit their details through to us.
      * There is an open text box so that the user can submit comments.
      * When the user submits their details by clicking the 'Send Contact Details' button, a modal pops up to confirm that details have been sent.

*   ### Future Features
    * A 'quick search' will be placed at the top of both the 'Home' page and the 'Country Details' to facilitate regular users that wish to immediately see the details for any particular country as soon as they come onto the site.
    * Expand the site to include more details on the countries.
    * Update the API references for data such that the site 'maintains' itself when the World Bank Database updates the API data. Currently, some data is supplied via 'Manual Input' and 'CSV File' input which will require a manual process to update when the data is refreshed.
    * Amend the 'Home' page pie charts to ensure appropriate rendering on screen sizes at 280px size.
    * Social media icons link to respective social media website home pages. Social media links will in future feature link directly to RMC Ltd social media connections.


## Technologies Used

### Languages Used

*   [HTML5](https://en.wikipedia.org/wiki/HTML5)
*   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
*   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
*   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

* [Bootstrap 4.5.0:](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    * Bootstrap was used to assist with the responsiveness and styling of the website.
* [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the contact details types and for social media icons in the footer to add the float transition while being hovered over.
* [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Exo' (main content in all pages) and 'Roboto' (for footer) fonts into the style.css file which are used on all pages.
* [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for the website to add icons for aesthetic and UX purposes.
* [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used to support JavaScript and is loaded from the [Google CDN](https://www.w3schools.com/jquery/jquery_get_started.asp).
* [GitPod:](https://www.gitpod.io/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
* [Atom:](https://atom.io/)
    - Atom was used as a Markdown Text Editor for README.md and Testing.md
* [Mapbox:](https://docs.mapbox.com/mapbox-gl-js/api/)
    - Mapbox javascript library is used to create the maps on the 'Home' and 'Country' pages.
* [Leaflet:](https://leafletjs.com/)
    - Leaflet provides a javascript library for Mapbox maps on the 'Home' and 'Country' pages.
* [OpenStreetMap:](https://www.openstreetmap.org)
    - OpenStreetMap provides the detail for Mapbox maps on the 'Home' and 'Country' pages.
* [Chartsjs:](https://www.chartjs.org/)
    - Chartjs is used to create the line charts and pie charts.
* [Emailjs:](https://www.emailjs.com/)
    - Emailjs is used to send the email from the contact form on the 'Contact Us' page.
* [Favicon.io:](https://favicon.io/)
    - Favicon.io was used for Favicon :earth_africa: web page title images.
* [Quackit:](https://www.quackit.com/character_sets/emoji/)
    - Quackit was used for the search function emojis.
* [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to resize images and edit photos for the website.
* [dirtyMarkup:](https://www.10bestdesign.com/dirtymarkup/)
    - dirtyMarkup was used to format HTML, CSS and JS files
* [Adobe Stock:](https://stock.adobe.com/uk/)
    - Adobe Stock was used as a library source for images.
* [Unsplash:](https://unsplash.com/)
    - Unsplash was used as a library source for images.
* [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes]() during the design process.
* [Am I Responsive:](http://ami.responsivedesign.is/#)
    - Am I Responsive was used to test the page layouts during the build process.  [Results](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/testscreenshots/amiresponsive.png)

### Application Programming Interfaces (API's) Used

* The website sources data from the **[World Bank Database](https://databank.worldbank.org/home.aspx)**. The website primarily makes use of API's to construct the country data, however in certain instances CSV files are used to provide summary level information. The **[Referential](https://rapidapi.com/referential/api/referential)** API via **[RapidAPI](https://rapidapi.com/)** is used to source country codes to construct country information and **[CountryFlags](https://www.countryflags.io/)** for country flag images. **[Leaflet](https://leafletjs.com/)** is used as a javascript library for **[Mapbox](https://www.mapbox.com/)** maps with **[OpenStreetMap](https://www.openstreetmap.org)** tile data, but use the API data to return a Country map for a specific country in the search function.
* jQuery AJAX is used to load the API calls asynchronously.

  * [Referential API](https://rapidapi.com/referential/api/referential)
      * The Referential API (sourced via [RapidAPI](https://rapidapi.com/)) was used to provide the country code to source all the country data in the search function. It provides the full list of countries in the drop down menu and on country selection, the country codes drive the other API's to return the required information. The Referential API is loaded with the 'Continent' denominator for the African Countries 'AF' (shown at the end of the link below). The API returns a full list of countries each with their respective two digit country codes (example: Nigeria='NG'). Please note that the API requires an Application Key so the link will not return a result. Please see the screenshot image of two countries' data, Nigeria (Key=NG) and Rwanda (Key=RW) as an example return (Note the API returns all 54 countries). The full API string is also shown below for documentation purposes.
        * [Country Code List](https://referential.p.rapidapi.com/v1/country?fields=currency%25252Ccurrency_num_code%25252Ccurrency_code%25252Ccontinent_code%25252Ccurrency%25252Ciso_a3%25252Cdial_code&continent_code=AF), **https://referential.p.rapidapi.com/v1/country?fields=currency%25252Ccurrency_num_code%25252Ccurrency_code%25252Ccontinent_code%25252Ccurrency%25252Ciso_a3%25252Cdial_code&continent_code=AF**

            ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/referentialcountrycode33.jpg "Country Codes from Referential API")
  * [World Bank Database](https://databank.worldbank.org/home.aspx)

      * The World Bank Database was used as the primary source for the data in the site. The relevant World bank API's are requested for data once a user selects a country in the search function which drives the relevant country code. Once the country code is determined, a number of different API's are used to determine Capital City, Land Size, Population and GDP for the World sectors, Africa and the 54 African Countries listed. The World Bank uses a standard link to reach the core of its data (https://api.worldbank.org/v2/country/YY/indicator/XX.XXX.XXX.XX), where;
          * **'YY'** = 'Country Code' eg 'NG'; and
          * **'XX.XXX.XXX.XX'** = 'relevant data string for land, population or GDP data' - see below.   
      * By way of example, the list below links directly to the API 'raw' data return for 'Nigeria', with country code 'NG' in the API link. The links below are also shown in full for documentation purposes;
        * [Capital City, Latitude and Longitude](https://api.worldbank.org/v2/country/NG), **https://api.worldbank.org/v2/country/NG**
        * [Land Size](https://api.worldbank.org/v2/country/NG/indicator/AG.LND.TOTL.K2), **https://api.worldbank.org/v2/country/NG/indicator/AG.LND.TOTL.K2**
        * [Population](https://api.worldbank.org/v2/country/NG/indicator/SP.POP.TOTL), **https://api.worldbank.org/v2/country/NG/indicator/SP.POP.TOTL**
        * [GDP](https://api.worldbank.org/v2/country/NG/indicator/NY.GDP.MKTP.CD), **https://api.worldbank.org/v2/country/NG/indicator/NY.GDP.MKTP.CD**
      * Note that not all countries have complete data in the API's either completely or for any number of years between 1970 and 2019. This will be evident in the line graph returns for any country. Sudan and South Sudan do not return any Land Size data in the land size data API. As this is the case, the Land Size numbers for [Sudan](https://en.wikipedia.org/wiki/Sudan) and [South Sudan](https://en.wikipedia.org/wiki/South_Sudan) are sourced from Wikipideia and the Land Size total for Africa has also been adjusted accordingly.
  * [CountryFlags](https://www.countryflags.io/)
      * The Country Flags API was used to return the national flag for the country selected in the search Function. By way of example, the list below links directly to the API return for 'Nigeria', with country code 'NG' in the API link. The link below is also shown in full for documentation purposes;
        * [Country Flag, Nigeria](https://www.countryflags.io/ng/shiny/64.png), **https://www.countryflags.io/ng/shiny/64.png**

## Site Construction

* ### Consistent Page Components
    * All pages of the site contain the same 'header', 'navbar', 'carousel' and 'footer';
      * **Header** consists of a title image with hand drawn doodles and a scripted 'Africa'.
      * **Navbar** is a menu top bar that is fixed to the top of the screen even on scroll down. It has a black background with light coloured lettering. There is a light backdrop highlighting the page that the user is on. The menu allows for easy access to any of the three pages at all time. If a user selects the 'Country Details' page, Nigeria is the default country selected. On mobile devices, the menu becomes a 'hamburger' and muct be 'touched' in order to select any of the three pages,
      * **Carousel** Just beneath the main 'title' header image is a carousel of five images. These images are large and designed to create visual impact, especially as they scroll through from one to the other. The images are the same for all three pages. The images have been selected to represent 'Africa' but not necessarily in a traditional sense. Images of 'animals' and portraits of 'people' have been explicitly avoided.
      * **Footer** The footer is displayed on all three pages and is consistent. There are three sections **'About'** - describes 'us' as an organisation, **'Data Analysis and Presentation Requirements?'** - describes what we do, and **'Contact'** - describes how to contact **'us'** to discuss what we can do for **'you'**.
* ### Home Page
    * Information Box
      * Contains the details as to the intention of the site and a how it can be used. It also contains the basic information for Africa in a high level context.
      * The data included in the information box for the **World** figures is computed using the **worldstats.js** file for each of Land Size, Population and GDP. The respective sizes for **Africa** are computed separately from the World Bank Database Excel file download located [here](XX).
      * Note that as the World Bank Database does not show any Land Size data for [Sudan](https://en.wikipedia.org/wiki/Sudan) and [South Sudan](https://en.wikipedia.org/wiki/South_Sudan), the values have been sourced from Wikipideia, and adjusted for Africa and the World Land Size Totals.
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/informationbox10050.jpg "INFO Box")
    * Map
      * The Africa Map is constructed using the **africamap.js** file which uses the [Leaflet](https://leafletjs.com/) library, based on [Mapbox](https://www.mapbox.com/) Map imagery and[OpenStreetMap](https://www.openstreetmap.org) data providers. The Map is centred on Ouesso, Republic of Congo (1.6155N, 16.0464E) in the Map Box.

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/africamap10025.jpg "AFRICA Map")
    * Line Graphs and Pie Charts
      * The graphs and charts use the [Chartsjs](https://www.chartjs.org/) javascript library.
      * The Line Graphs and Pie Charts are all computed in the **totalcharts.js** file.
        * The Line Graphs reference [pop.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/pop.csv) and [gdp.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/gdp.csv) respectively to create the historical data between 1970 and 2019.

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/pop10025.jpg "Population Chart")

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/gdp10025.jpg "GDP Chart")
        * The Pie Charts are directly loaded with the data in the **totalcharts.js** file.

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/africaland10050.jpg "Land Pie Chart")

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/africapop10050.jpg "Population Pie Chart")

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/africagdp10050.jpg "GDP Pie Chart")
    * Country Search Function
      * the Search Function is a drop down menu that references the **getcountries.js** file. The country selection made by the user will return the required information about the Country selected on the 'Country Details' page. The **getcountries.js** file will return the required two digit **countryCode** that is fed into all the relevant API's (described below in the 'Country Details' Page section) that in turn generate the required returns for the Country selected.

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/searchmenu10050.jpg "Search Function")
* ### Country Details Page (Nigeria has been used by way of example)
    * Country Information
      * Contains the basic information for the **Country** selected.
      * The Country Name, National Flag and Capital City is returned in the **countrystats.js** file  from the relevant API's.
      * The data included in the information box for the **Country** figures and percentages is computed in the **countrystats.js** file for each of Land Size, Population and GDP on returns from the relevant API's. The respective sizes for **Africa** are computed separately from the **World Bank Database** Excel file download located [here](XX).
      * Note that as the World Bank Database does not show any Land Size data for [Sudan](https://en.wikipedia.org/wiki/Sudan) and [South Sudan](https://en.wikipedia.org/wiki/South_Sudan), the values have been sourced from Wikipideia, and adjusted for Africa and the World Land Size Totals.
      * The following code at **line 107** in the **countrystats.js** file is used to account for Sudan and South Sudan Land Size data after the API from the search function is called;

      ```JavaScript
        function writeLandSize(data) {
          if (countryCode == "SD") {
              landsize = 1886068;
            } else if (countryCode == "SS") {
              landsize = 619745;
            } else {
              item = data[1];
              landsize = item[1].value.toFixed(0);
            }
            perc = (landsize / 295097.44).toFixed(2);
            document.getElementById("landsize").innerHTML += ("Land Size:   " + landsize + "   Sq. Kms" + " " + " - " + perc + "% of total Africa Land Size (29.51 Mn Sq. Kms)");
          }
        ```
        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriainfo10050.jpg "Country Information")
    * Country Map
      * The Country Map is centred on the Capital City Latitude and Longitude. The map is generated by reference to the **countrymap.js** file which uses the [Leaflet](https://leafletjs.com/) library, based on [Mapbox](https://www.mapbox.com/) Map imagery and[OpenStreetMap](https://www.openstreetmap.org) data providers.
        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriamap10050.jpg "Country Map")
    * Country Line Graphs
      * The Country Line Graphs are returned in the **countrygraphs.js** file  from the relevant API's.
        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriapopline10050.jpg "Country Population Line Graph")

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriagdpline10050.jpg "Country GDP Line Graph")

    * Country and Top 5 Pie Charts
      * The Country and Top 5 Pie charts are returned in the **piecountry.js** file  from the relevant API's.
      * The following code at **line 18** in the **piecountry.js** file is used to account for Sudan and South Sudan Land Size data (in the Land Size Pie Chart) after the API from the search function is called;
      ```javascript
        function writeLand(data) {
          if (countryCode == "SD") {
            item = data[1][1];
            countland = 1886068 / 1000000;
            } else if (countryCode == "SS") {
            item = data[1][1];
            countland = 619745 / 1000000;
            } else {
            item = data[1][1];
            countland = item.value / 1000000;
            }
            const roaland = (29.509744 - countland);
          }
      ```
        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigerialandpie10050.jpg "Country Land Size Pie Chart")

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriapoppie10050.jpg "Country Population Pie Chart")

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/nigeriagdppie10050.jpg "Country GDP Pie Chart")

      * The Top 5 Pie charts are computed in the **piecountry.js** file. Each chart for Land Size, Population and GDP references CSV files; [land.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/land.csv), [poptotes.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/poptotes.csv) and [gdptotes.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/gdptotes.csv) respectively.

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/top5landpie10050.jpg "Top 5 Land Size")

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/totpoppie10050.jpg "Top 5 Population Pie Chart")

        ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/topgdppie10050.jpg "Top 5 GDP Pie Chart")

    * Country Search Function

      * The Search Function is a drop down menu that references the **getcountries.js** file. The country selection made by the user will return the required information about the Country selected on the 'Country Details' page. The **getcountries.js** file will return the required two digit **countryCode** that is fed into all the relevant API's (described above in the 'Country Details' Page section above) that in turn generates the required information return for the Country selected.
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/searchmenu10050.jpg " Country Search Function")
      * Note that the [Referential API](https://rapidapi.com/referential/api/referential) does not return the list of countries in full alphabetical order (mostly, but not exclusively). To place the country list into alphabetical order, the following code is utilised after the data is called (many thanks to [W3C Schools](https://www.w3schools.com/js/js_array_sort.asp));
      ```javascript
      data.sort(function(a, b){
          const x = a.value.toLowerCase();
          const y = b.value.toLowerCase();
          if (x < y) {return -1;}
          if (x > y) {return 1;}
          return 0;
        });
      ```
* ### Contacts Page

    * The Contacts Page contains the 'Contact Form' for a user to supply contact information and to provide comments, questions or to provide a request for some work.
    * The 'Contact Form' will generate an email by referencing the **sendemail.js** file when a user submits their information.

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/contact10025.jpg "Contact Form")

* ### Construction  Table

    * The following table provides a summary of how the Site Pages and Sections are compiled;

        Site Page | Page Section | Javascript File | CSV Files / Manual Input | API Reference |
        ----------|--------------|-----------------|-----------|---------|
        Home | Information Box | worldstats.js | N/A | [World Bank Database - World Stats](https://api.worldbank.org/v2/country/wld/indicator/AG.LND.TOTL.K2?format=json) |
        Home | Africa Map | africamap.js | N/A | [Mapbox](https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}) (Requires Access Token)|
        Home | Line Graphs | totalcharts.js | [pop.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/pop.csv), [gdp.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/gdp.csv) | N/A |
        Home | Pie Charts | totalcharts.js | Manual Inputs | N/A |
        Home | Search Function | getcountries.js | N/A | [Referential via RapidAPI - Africa Country List](https://referential.p.rapidapi.com/v1/country?fields=currency%25252Ccurrency_num_code%25252Ccurrency_code%25252Ccontinent_code%25252Ccurrency%25252Ciso_a3%25252Cdial_code&continent_code=AF) (Requires Access Token) |
        Country Details | Information Box | countrystats.js | N/A | [CountryFlags National Flags](https://www.countryflags.io/ng/shiny/64.png), [World Bank Database - Capital City](https://api.worldbank.org/v2/country/ng?format=json), [World Bank Database - Land Size](https://api.worldbank.org/v2/country/ng/indicator/AG.LND.TOTL.K2?format=json),[World Bank Database -  Population](https://api.worldbank.org/v2/country/ng/indicator/SP.POP.TOTL?format=json), [World Bank Database - GDP](https://api.worldbank.org/v2/country/nd/indicator/AG.LND.TOTL.K2?format=json) |
        Country Details | Country Map | countrymap.js | N/A | [Mapbox](https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}) (Requires Access Token)|
        Country Details | Country Line Graphs | countrygraphs.js | N/A | [World Bank Database - Country Population](https://api.worldbank.org/v2/country/ng/indicator/SP.POP.TOTL?format=json), [World Bank Database - Country GDP](https://api.worldbank.org/v2/country/ng/indicator/NY.GDP.MKTP.CD?format=json)
        Country Details | Country Pie Charts | piecountry.js |  N/A | [World Bank Database - Country Land Size](https://api.worldbank.org/v2/country/ng/indicator/AG.LND.TOTL.K2?format=json), [World Bank Database - Country Population](https://api.worldbank.org/v2/country/ng/indicator/SP.POP.TOTL?format=json), [World Bank Database - Country GDP](https://api.worldbank.org/v2/country/ng/indicator/NY.GDP.MKTP.CD?format=json) |
        Country Details | Top 5 Pie Charts | piecountry.js | [land.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/land.csv),[poptotes.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/poptotes.csv), [gdptotes.csv](https://github.com/Readri205/MS2_Project/blob/master/assets/csv/gdptotes.csv) | N/A |
        Country Details | Search Function | getcountries.js | N/A | [Referential via RapidAPI - Africa Country List](https://referential.p.rapidapi.com/v1/country?fields=currency%25252Ccurrency_num_code%25252Ccurrency_code%25252Ccontinent_code%25252Ccurrency%25252Ciso_a3%25252Cdial_code&continent_code=AF) (Requires Access Token) |
        Contact | Contact Form | sendemailjs.js | N/A | [Emailjs](https://www.emailjs.com/) (Website)

## Testing

Testing information can be found in a separate [testing.md](https://github.com/Readri205/MS2_Project/blob/master/testing.md) file.

### Known Bugs and Issues

*   Users may wish to know the full list of countries in each of the World Bank Database sectors listed in the pie charts on the 'Home' page. Future updates to the site will provide an appendix list for each of the sectors. The lists are provided in the [testing.md](https://github.com/Readri205/MS2_Project/blob/master/testing.md) file under the **Numerical Validation Testing** section.
*   Mapbox and Country.io API requests can return CORS issues. The cookies submitted by these API sites have been updated with 'SameSite' = "None" and "Secure" per the [Google Chrome documentation](https://web.dev/samesite-cookies-explained/) by updating the Cookies in the Web Developer Tools in 'Application/Storage/Cookies'.
*  To accommodate the pie chart rendering for iPhone 6 screen sizes (375px in portrait mode), the global default font size for the [Chartsjs:](https://www.chartjs.org/) charts is set at 8px for the 'Home' page and 10px for the 'Country Details' page. This font size is (in my opinion) too small for larger screens on desktops and laptops. Future site updates will look at other charting options to allow more flexible solutions to accommodate a larger variety of screen sizes.
*  On some screen sizes at 280px in portrait mode, the pie charts on the 'Home' page can become squeezed and will not render appropriately. Testing on devices such as *Galaxy Fold* (Chrome Developer Tools) evidenced this issue. Future site updates will look at other charting options to allow more flexible media query solutions for various screen sizes.
*  On some screen sizes 320px in portrait mode the search menu text box sometimes squeezes outside the frame. Whilst aesthetically, not pleasing for the user the search function still works. Due to time constraints this function will be amended in future releases.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following process;

1. The project was written in [GitPod](https://www.gitpod.io/) and pushed to GitHub Pages ready for deployment by taking the following steps;
1. Logged in to GitHub and located the [GitHub Repository](https://github.com/Readri205/MS2_Project);
1. At the top of the Repository, the "Settings" Button was selected on the menu;
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/deployment10050.jpg "See Settings").
1. Scrolled down the Settings page until the "GitHub Pages" Section was located;
1. Under "Source", the dropdown showing "None" was selected and then "Master Branch" was chosen;
1. The selection was then saved and the page automatically refreshed; and
1. The published site is found by scrolling back down the page to the "GitHub Pages" section to find the live site - [**EARTH AFRICA** :earth_africa:](https://readri205.github.io/MS2_Project/).
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/deployedgithubpages10050.jpg "Github Pages Deployed Site")

### Forking the GitHub Repository

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and  changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Readri205/MS2_Project);
1. At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/forking10050.jpg "Fork Button"); and
1. Click to create a copy of the original repository in your own GitHub account.

### Making a Local Clone

1. Log in to **GitHub** and locate the [GitHub Repository](https://github.com/Readri205/MS2_Project)
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, click the top right hand link click "Use HTTPS";
1. Copy the link under "Clone with HTTPS";
      ![alt text](https://readri205.github.io/MS2_Project/assets/images/readmeimg/clone10050.jpg "HTTPS Clone")
1. Open your Code Editor and access the appropriate process to paste the clone link;
1. Change the current working directory to the location where you want to keep the cloned directory;
1. Paste the URL you copied in step 4 above.

Note that different Code Editors will have different processes for making the clone once the HTTPS link copy is made in step 4 above.

  * If using **GitHub Desktop**, the clone can de saved directly into GitHub Desktop from the "Code" dropdown menu by choosing **'Open with GitHub Desktop'**.

A **Zip File** clone can be downloaded from the same "Code" drop down above;
  * Select **'Download ZIP'** and the complete zip file will be saved to you local computer.

## Credits

### Code

*   My Mentor (Adegbenga Adeye (email:adegbenga.adeye@outlook.com, slack:gbenga_mentor)) for providing help, guidance, inspiration and input on the challenging components particularly for the 'Country Search' Function.

*   [Code Institute course](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute%20%2Bcourses&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-443742237303&hsa_ad=407017470923&hsa_acc=8983321581&hsa_grp=62188641040&hsa_mt=b&hsa_cam=1578649861&hsa_kw=%2Bcode%20%2Binstitute%20%2Bcourses&hsa_ver=3&hsa_src=g&gclid=CjwKCAjw4MP5BRBtEiwASfwAL3-Oi3uDo1sBfn2KpQVAlLb07T2ndP-Q2mCFxdGgpvoBMoPIAtbg9xoCyZgQAvD_BwE&gclsrc=aw.ds) (the Star Wars example) for the API fetch function that is used extensively across all the API calls in this website.

*   [Code Institute course](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute%20%2Bcourses&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-443742237303&hsa_ad=407017470923&hsa_acc=8983321581&hsa_grp=62188641040&hsa_mt=b&hsa_cam=1578649861&hsa_kw=%2Bcode%20%2Binstitute%20%2Bcourses&hsa_ver=3&hsa_src=g&gclid=CjwKCAjw4MP5BRBtEiwASfwAL3-Oi3uDo1sBfn2KpQVAlLb07T2ndP-Q2mCFxdGgpvoBMoPIAtbg9xoCyZgQAvD_BwE&gclsrc=aw.ds) (the [Emailjs](https://www.emailjs.com/) example) for the 'Contact Form' email return function used in this website.

*   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

*   [W3C Schools](https://www.w3schools.com/) referenced for the following code;
    * The Navbar;
    * The Carousel;
    * Contact Form jQuery submission confirmation; and
    * Country list menu drop down alphabetical sort.

### Content

*   All content was written by the developer.

### Media

*   All images [© Unsplash.com](https://unsplash.com/) unless otherwise stated;
    *   Header image - [Hand draw doodles of Africa word. Colorful illustration. Background with lots of objects.](https://stock.adobe.com/uk/contributor/206263469/leo-d?load_type=author&prev_url=detail) By leo_d [© stock.adobe.com](https://stock.adobe.com/uk/);
    *   Carousel image - [Dallol, Ehiopia](https://unsplash.com/photos/UQJP4eEqRV0) By Trevor Cole [© Unsplash.com](https://unsplash.com/);
    *   Carousel image - [Aït Benhaddou, Morocco](https://unsplash.com/photos/pcbSQTQr2-I) By Toa Heftiba [© Unsplash.com](https://unsplash.com/);
    *   Carousel image - [Tema, Greater Accra region, Ghana](https://unsplash.com/photos/8hi9WGb4qMA) By Efe Kurnaz [© Unsplash.com](https://unsplash.com/);
    *   Carousel image - [Colonial houses and crosswalk, pedestrian crossing in Mindelo on the island of Sao Vicente in Cape Verde,a beautiful clouded sky.](https://stock.adobe.com/fr/contributor/208162006/clara?load_type=author&prev_url=detail) By clara [© stock.adobe.com](https://stock.adobe.com/uk/);
    *   Carousel image - [Kirche in Malawi](https://stock.adobe.com/fr/contributor/208173857/christian-horras?load_type=author&prev_url=detail) By Christian Horras [© stock.adobe.com](https://stock.adobe.com/uk/);


### Acknowledgements

*   My Mentor **Adegbenga Adeye**, (email: adegbenga.adeye@outlook.com, slack:gbenga_mentor) for continuous helpful feedback. Ade has been an amazing in helping and supporting me with this site. It has proven much harder and much more work for me to develop than I ever thought (severe case of 'what you don't know when you start').
*   **Tutor support** at Code Institute for their support. When I have requested help, it has come quickly and efficiently when needed.
*   **Student assessment** at Code Institute. I have looked to accommodate comments back on MS1 to reduce any re-occurring issues in MS2.
*   **Other students** (Slack Code Institute Workspace) on the Full Stack Developer Course, via the [Slack Communication Platform](https://slack.com/intl/en-gb/).
*   **Peer Code Review** (Slack Channel)
The website was uploaded to the 'Peer Code Review' Slack Channel designed to receive direct inputs from other developers. This provides useful third party feedback on the website;
    * @Dante **Dante Healy** for continuous positive feedback on the site usability and design and for testing the EmailJS service;
    * @Eamonn **Eamonn Smythe** for positive feedback and suggestion to include a margin around the maps to assist page scrolling on mobile devices and for testing the EmailJS service; and
    * @Jimlynx **Jim Morel** for his review and extremely positive feedback on the site.
*   **Friends and family** providing review and feedback on the site content, navigation and screen size testing. This has been invaluable with two very 'have mobile, will travel' daughters, it is often brutal but effective.

## Version Control

*   All through the development phase of the project, commits have been made from the GitPod Repository to GitHub. The version control list below mirrors the GitHub Commit list. It is designed to provide a direct track on commits in the README file for easy access as to code status in GitPod. Note that feedback from MS1 Project was received on July 8th, 2020 which stated that commits should be in the imperative tense. Any commits after this date (approx. V6.4) that are not in the imperative is in error.
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
    - V7.9 Amend app for get trefle search
    - V8.0 Further amend app for search
    - V8.1 Amend styles in html pages
    - V8.2 Add more styles to html pages
    - V8.3 Update Procfile for flask
    - V8.4 Revert Procfile change
    - V8.5 Updadte get trefle search page
    - V8.6 Amend Procfile python3 to python
    - V8.7 Add trefle token to heroku amend navbar and style
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
    - V9.9 Amend card size in trefle search
    - V10.0 Amend card size on card search large screen
    - V10.1 Add page links and styles to trefle search page
    - V10.2 Amend card size trefle search
    - V10.3 Add pagination function
    - V10.4 Adjust to page=2 for trefle search
    - V10.5 Amend card size for trefle search
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
    - V11.7 Add trefle_many get function test
    - V11.8 Add trefle searches pages htmls
    - V11.9 Add get_next first test
    - V12.0 Update search test
    - V12.1 Update search for first and last page
    - V12.2 Add PlantID to search function
    - V12.3 Add target blank redirect in url wiki search
    - V12.4 Move plantID key to env variables
    - V12.5 Add home page content, similar images PlantID
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
    - V20.1 Amend search row size on trefle search
    - V20.2 Amend site title
    - V20.3 Amend cloudinary image upload styles
    - V20.4 Update wiki plant links in trefle search
    - V20.5 Update for cloudinary destroy method
    - V20.6 Update for next_page testing
    - V20.7 Amend wiki links to scientific names
    - V20.8 Add page iteration test code
    - V20.9 Update for page iteration test
    - V21.0 Update css styles on cards
    - V21.1 Add direct trefle plant upload
    - V21.2 Amend add trefle plant descriptors
    - V21.3 Add plant details search in app
    - V21.4 Amend add trefle plant for collections input
    - V21.5 Amend page numbers on search
    - V21.6 Amend page number structure for search
    - V21.7 Amend page numbers for 3 pages and less
    - V21.8 Add cloudinary delete image function
    - V21.9 Amend cloudinary delete function syntax
    - V22.0 Update cloudinary image tags
    - V22.1 Amend cloudinary image tag style
    - V22.2 Delete old trefle html pages
    - V22.3 Add plant details html page
    - V22.4 Add plant detail styles to html page
    - V22.5 Update plant detail styles
    - V22.6 Update styles on plant details
    - V22.7 Remove duplicate bloom months in details
    - V22.8 Amend spelling and plant detail styles
    - V22.9 Amend home page image to daisy
    - V23.0 Switch url direction from Plant ID page
    - V23.1 Add trefle filter searches
    - V23.2 Update trefle filter search
    - V23.3 Updates to trefle filter page search
    - V23.4 Updated plant details page for no image
    - V23.5 Add tests for Shamrock wrapper for trefle
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
***
<b id="f1">1</b> **&** <b id="f2">2</b> **Future Features** in the [README.md](https://github.com/Readri205/MS2_Project/blob/master/README.md) identifies that a 'quick search' could be placed at the top of both the 'Home' page and the 'Country Details' page to facilitate regular and frequent users. Regular and frequent users may wish to immediately see the details for any particular country as soon as they come onto the site. This allows quick access to Country search rather than having to scroll down to the bottom of the page. 1[↩](#a1);2[↩](#a2)
