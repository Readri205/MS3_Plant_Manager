# **GARDEN MANAGER :seedling: - Testing Information**

![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_orchid.png?raw= "Garden Manager")

[View the live **GARDEN MANAGER** :seedling: project here.](https://plant-manager-flask-mongodb.herokuapp.com/)

The project uses two key API interfaces as shown here;
### [Trefle.io](https://trefle.io/)
![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/trefle_header.png?raw= "Trefle Logo")

### [Plant.id](https://plant.id/)
![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/plant_id_header.png?raw= "Plant.ID Logo")

View the Main [README here](https://github.com/Readri205/MS3_Plant_Manager/blob/master/README.md)

## Contents

- [User stories](#user-stories)
    + [First Time Visitor Goals](#first-time-visitor-goals)
    + [Returning Visitor Goals](#returning-visitor-goals)
    + [Frequent User Goals](#frequent-user-goals)
    + [Mobile Menu](#mobile-menu)
  * [Functional User Tests by Browser](#functional-user-tests-by-browser)
- [Automated Testing](#automated-testing)
- [API Fail Message Test](#api-fail-message-test)
- [Contact Form Testing](#contact-form-testing)
- [Further Testing](#further-testing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User stories

The user stories are annotated below to describe actual functionality. Screenshot images of the site have been provided in the main [README.md](https://github.com/Readri205/MS3_Plant_Manager/blob/master/README.md). A [Functional User Tests by Browser](#functional-user-tests-by-browser) testing schedule has been prepared and is shown below. User functionality has been tested across four key web browsers; Chrome, Safari, MSEdge, Opera and Internet Explorer. Internet Explorer has returned 'test fails' but it is expected that any Internet Explorer users will upgrade to MS Edge or migrate to other mainstream browsers.

*   #### First Time Visitor Goals
    * The first time visitor will want to;
      * easily understand the main purpose of the site;

      * be able to easily navigate throughout the site to find content;

      * view the carousel images just beneath the header;

      * scroll down through the information, read the content, view each of the function cards;

      * register for the site and create login credentials;

      * enter plant details for plants they are interested in;

        * login to the site;
        * immediately view their plants list;
        * view their collections list;
        * search for plants in one of the search methods;
          * name;
          * filter by attribute;
          * image upload.
        * add a plant to users plant list and a collection.

      * contact us to ask about data projects that they may be interested to have completed as an item of work.
        * Per images above

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

      * On mobile devices the search function operates in the same manner as for larger screens;

- ### Functional User Tests by Browser

    * All the functional user tests have been made per the attached [Test Schedule](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet.xlsx). All functional tests have been on different Browsers including Chrome, MS Edge, Firefox, Opera and Internet Explorer.
    * Note that there are functional **'fails'** returned from **Internet Explorer** for any search functionality. Internet Explorer was **NOT** tested on mobile. However, **MS Edge** was tested **successfully** on large screen and mobile. The results are shown below;
      * MacBook Pro 16" Screen;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet1.png "Functional Test Schedule - MacBook Pro 16 Screen")

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet2.png "Functional Test Schedule - MacBook Pro 16 Screen")

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet3.png "Functional Test Schedule - MacBook Pro 16 Screen")

      * iPhone X 375px screen;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet4.png "Functional Test Schedule - iPhone X 375 Screen")

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet5.png "Functional Test Schedule - iPhone X 375 Screen")

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet6.png "Functional Test Schedule - iPhone X 375 Screen")

## Automated Testing

The following automated tools were used to test the website during development of the website;

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) used extensively **during development** to test outputs and to identify issues arising during the development phase. This tool was used to determine results for;
  - Python Requests API returns;
  - Shamrock Library API returns;
  - Javascript function results;
  - CORS issues and resolutions;
  - Element styling;
  - Site upload speeds for API's and image loading;
  - Device type screen size testing.

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - used to validate HTML, resulted in highlight for Flask functions in html pages;
- **Home Page**
    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/w3c_html.png?raw=  "HTML W3C Validator Check")

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - used to validate CSS;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/w3c_css.png?raw= "CSS W3C Validator Check")
- [JSHint](https://jshint.com/) - used to validate javascript;
  - Each of the javascript files has been validated using JSHint.

    - **image_upload.js**

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/jshint_materialize.png?raw= "Image Upload")
    - **script.js**

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/jshint_image.png?raw= "Image Upload")

      The missing semicolons on lines 13 and 15 do not appear to be an issue.

    - **sendemail.js**

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/jshint_sendemailjs.png?raw= "Image Upload")

## API Fail Message Test

The website makes use of a number of API calls as described in the main README.md. If an API request fails to be returned the user will receive an error message telling the user of the error and to ask them to contact us to let us know. This function was tested on a 'local' domain that precludes the API being called. This returned the following message;

  ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/apifail10050.jpg "API Fail Message to User")

## Contact Form Testing

- The 'Contact Form' was tested for input on all fields, submission confirmation back to the user and that an email was received via Emailjs based on the users details being submitted;

- Input validation

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/contactpageinputcheck10025.jpg "Contact Form Input Required")

- Submission Confirmation to User  

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/submissionconfirmation10050.jpg "Submission Confirmation")

- Email Receipt Confirmation

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/emailreceipt10050.jpg "Email Receipt")

## Further Testing

- The website was tested using Google Chrome Developer Tools Responsive Design feature for small screen sizes. Screen sizes down to 320px will render the Pie Charts appropriately in Portrait Mode. Screen size of 280px in portrait mode (Galaxy Fold) will not render the Home Page Pie Charts and must be viewed in landscape mode.

  - iPhone 6 375px Portrait Mode Home Page Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/iphone6375px10050.jpg "iPhone 6 375px Portrait Home Page Charts")

  - iPhone 5SE 375px Portrait Mode Home Page Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/iphone5se320px10050.jpg "iPhone 6 375px Portrait Home Page Charts")

  - iPhone4 320px Portrait Mode Home Page Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/iphone4320px10050.jpg "iPhone 4 320px Portrait Home Page Charts")

  - iPhone4 320px Portrait Mode Country Details Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/iphone4320pxcountry10050.jpg "iPhone 4 320px Portrait Country Details Charts")

  - Galaxy Fold 280px Portrait Mode Home Page Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/galaxyfold280px10050.jpg "Galaxy Fold 280px Portrait Home Page Charts")

  - Galaxy Fold 653px Landscape Mode Home Page Charts

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/galaxyfoldlandscape653px10050.jpg "Galaxy Fold 653px Landscape Home Page Charts")

***
