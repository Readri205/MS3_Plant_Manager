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
  * [User stories](#user-stories)
    + [Functional User Tests by Browser](#functional-user-tests-by-browser)
  * [Automated Testing](#automated-testing)
  * [API Fail Message Test](#api-fail-message-test)
  * [Contact Form Testing](#contact-form-testing)
  * [Further Testing](#further-testing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User stories

A [Functional User Tests by Browser](#functional-user-tests-by-browser) testing schedule has been prepared and is shown below. User functionality has been tested across four key web browsers; Chrome, Safari, MSEdge, Opera and Internet Explorer. Internet Explorer has returned 'test fails' but it is expected that any Internet Explorer users will upgrade to MS Edge or migrate to other mainstream browsers.

### Functional User Tests by Browser

  * All the functional user tests have been made per the attached [Test Schedule](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet.xlsx). All functional tests have been on different Browsers including Chrome, MS Edge, Firefox, Opera and Internet Explorer.
  * Note that there are functional **'fails'** returned from **Internet Explorer** for any search functionality. Internet Explorer was **NOT** tested on mobile. However, **MS Edge** was tested **successfully** on large screen and mobile. The results are shown below;
  * MacBook Pro 16" Screen;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet1.png "Functional Test Schedule - MacBook Pro 16 Screen")

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet2.png "Functional Test Schedule - MacBook Pro 16 Screen")

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/testsheet3.png "Functional Test Schedule - MacBook Pro 16 Screen")

  * iPhone X 375px screen;

    * On the mobile device the Trefle Search issue with apostrpohe's is highlighted as an 'amber' issue.

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

* The website makes use of a number of API calls as described in the main README.md. If an API request fails with an error code 403 or 404, the user will be directed to an error page as illustrated below;

  ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/apifail10050.jpg "API Fail Message to User")

* In Heroku and on a mobile device, the application will return an error if a user places and apostrophe in the main Trefle search function to search for a plant. This error does not occur on a desktop device. A specific error page has been set up to reference this error as illustrated below;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/oops_error_message.png?raw= "Error Message")

## Contact Form Testing

- The 'Contact Form' was tested for input on all fields, submission confirmation back to the user and that an email was received via Emailjs based on the users details being submitted;

- Input validation

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_contact.png?raw= "Contact Verify")

- Submission Confirmation to User

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_contactconfirm.png?raw= "Contact Confirm")

- Email Receipt Confirmation

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_email.png?raw= "Email Confirm")

## Further Testing

- The website was tested using Google Chrome Developer Tools Responsive Design feature for small screen sizes. Screen sizes down to 320px will render the Pie Charts appropriately in Portrait Mode. Screen size of 280px in portrait mode (Galaxy Fold) will not render the Home Page Pie Charts and must be viewed in landscape mode.

  - iPhone 6 375px Portrait Mode

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/iphone_6_375.png "iPhone 6 375px")

  - iPhone 5 320px Portrait Mode

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/iphone_5_320.png "iPhone 5 320px")

  - iPad 768px Portrait Mode

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/ipad_768.png "iPad 768px")

  - iPhone4 320px Portrait Mode Country Details Charts

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/iphone_6_375.png "iPhone 6 375px")

  - Galaxy Fold 280px Portrait Mode

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/galaxy_fold_280.png "Galaxy Fold 280px")

  - Galaxy Fold 280px Portrait Mode Plant Details

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/galaxy_fold_280_deets.png "Galaxy Fold 280px Plant Details")

  - Galaxy Fold 653px Landscape Mode

      ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/assets/documents/galaxy_653_portrait.png "Galaxy Fold 653px Plant Details")

***
