# **GARDEN MANAGER :seedling: - Testing Information**

![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_orchid.png?raw= "Garden Manager)

[View the live **GARDEN MANAGER** :seedling: project here.](https://plant-manager-flask-mongodb.herokuapp.com/)

### [Trefle.io](https://trefle.io/)
![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/trefle_header.png?raw= "Trefle Logo")

### [Plant.id](https://plant.id/)
![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/plant_id_header.png?raw= "Plant.ID Logo")

View the Main [README here](https://github.com/Readri205/MS3_Plant_Manager/blob/master/README.md)

## Contents

- [User stories](#user-stories)
- [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent User Goals](#frequent-user-goals)
  - [Functional User Tests by Browser](#functional-user-tests-by-browser)
- [Automated Testing](#automated-testing)
- [API Fail Message Test](#api-fail-message-test)
- [Peer Code Review (Slack Channel)](#peer-code-review--slack-channel-)
- [Numerical Validation Testing](#numerical-validation-testing)
- [Contact Form Testing](#contact-form-testing)
- [Further Testing](#further-testing)

[Table of contents generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/)

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

    * All the functional user tests have been made per the attached [Test Schedule](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/testschedule.xlsx). All functional tests have been on different Browsers including Chrome, MS Edge, Firefox, Opera and Internet Explorer.
    * Note that there are functional **'fails'** returned from **Internet Explorer** for any search functionality. Internet Explorer was **NOT** tested on mobile. However, **MS Edge** was tested **successfully** on large screen and mobile. The results are shown below;
      * MacBook Pro 16" Screen;

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/testschedulemacbook10050.jpg "Functional Test Schedule - MacBook Pro 16 Screen")

      * iPhone X 375px screen;

          ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/testscheduleiphonex10050.jpg "Functional Test Schedule - Mobile Screen")

## Automated Testing

The following automated tools were used to test the website during development of the website;

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) used extensively **during development** to test outputs and to identify issues arising during the development phase. This tool was used to determine results for;
  - jQuery AJAX API returns;
  - Javascript function results;
  - CORS issues and resolutions;
  - Element styling;
  - Site upload speeds for API's and image loading;
  - Device type screen size testing.

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - used to validate HTML;
- **Home Page**
    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/indexhtmlw3cvalidation.png "HTML Home Page W3C Validator Check")

- **Country Details Page**
    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/countryw3chtmlcheck.png "HTML Country Details Page W3C Validator Check")

    **Note:** The validator returns two warnings per above, but it is understood from tutor support that this return is acceptable for the validation check. An alternative is to turn the 'h3' and 'h4' headers into 'divs' and fully style the headers using CSS, however this was deemed 'unnecessary'.

    Please see below the HTML code and the corresponding output referred to in the check;

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/headercodecountry.png "HTML Country Page Code")

      ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/headeroutput.png "HTML Country Page output")

- **Contact Page**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/contactw3chtmlcheck.png "HTML Contact Page W3C Validator Check")

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - used to validate CSS;

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/cssw3cvalidatorcheck.png "CSS W3C Validator Check")
- [JSHint](https://jshint.com/) - used to validate javascript;
  - Each of the javascript files has been validated using JSHint. The use of 'const' has returned a large number of warnings from the test. It has been used extensively for this website, and is perceived to be modern practice' per discussion with Code Institute 'Tutor Support'.

    - **africamap.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintafricamap.png "africamap.js")
    - **countrygraphs.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintcountrygraphs.png "countrygraphs.js")
    - **countrymap.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintcountrymap.png "countrymap.js")
    - **countrystats.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintcountrystats.png "countrystats.js")
    - **getcountries.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintgetcountries.png "getcountries.js")
    - **piecountry.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintpiecountry.png "piecountry.js")
    - **piecountry.js Part 2**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintpiecountrypart2.png "piecountry.js Part 2")
    - **sendemail.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintsendemailjs.png "sendemail.js")
    - **totalcharts.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshinttotalcharts.png "totalcharts.js")
    - **worldstats.js**

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/jshintworldstats.png "worldstats.js")

- [Autoprefixer CSS Online](https://autoprefixer.github.io/) - used to parse CSS and add vendor prefixes. This is not a test as such but allows for cross browser CSS capability. The header below has been placed at the top of the [style.css](https://github.com/Readri205/MS2_Project/blob/master/assets/css/style.css) file.

    ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/autoprefixercssheader.png "Autoprefixer Header for Vendor Prefixes")

## API Fail Message Test

The website makes use of a number of API calls as described in the main README.md. If an API request fails to be returned the user will receive an error message telling the user of the error and to ask them to contact us to let us know. This function was tested on a 'local' domain that precludes the API being called. This returned the following message;

  ![alt text](https://readri205.github.io/MS2_Project/assets/images/testscreenshots/apifail10050.jpg "API Fail Message to User")

## Peer Code Review (Slack Channel)

The website was uploaded to the Peer Code Review Slack Channel designed to receive direct inputs from other developers. This provides useful third party feedback on the website;

- @Dante **Dante Healy** for continuous feedback on the site usability and design, and for testing the EmailJS service with success;
- @Eamonn **Eamonn Smythe** for feedback and suggestion to include a margin around the maps to assist page scrolling on mobile devices and for testing the EmailJS service with success; and
- @Jimlynx **Jim Morel** for his review and positive feedback on the site.

## Numerical Validation Testing

The website makes use of [World Bank Database](https://databank.worldbank.org/home.aspx) API's as described in the [README.md](https://github.com/Readri205/MS2_Project/blob/master/README.md). In particular, those API's relevant to **Land Size, Population and GDP**. Adjustments have been made to reflect the more appropriate figures for the Africa continent analysis. The totals for each 'Series Code' (Land Size = AG.LND.TOTL.K2, GDP = NY.GDP.MKTP.CD, Population = SP.POP.TOTL) have been downloaded into excel files and relevant adjustments made.

- The land sizes for Sudan and South Sudan are not included in the World Bank Database and so are adjusted and **confirmed** in the [landbyregion.xlsx](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/landbyregion.xlsx) excel sheet (image below). Note that [Sudan](https://en.wikipedia.org/wiki/Sudan) (1,886,068 sq. kms) and [South Sudan](https://en.wikipedia.org/wiki/South_Sudan) (619,745 sq. kms) Land Sizes are sourced from [Wikipedia](https://www.wikipedia.org/)
- The land size for Africa from the World Bank is adjusted to move the 6 countries in the Middle East and North Africa sector are also **confirmed** using the same excel file (image below).

    ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/landbyregion10050.jpg "Land Size By Region")

- The Population and GDP sectors for the World Regions and Africa are also **confirmed** in the [gdppopworldadj.xlsx](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/gdppopworldadj.xlsx) excel file (Image below).

    ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/gdppopworldadj10050.jpg "Population and GDP Adjustments")

- To **confirm** the Africa country data, the following files are uploaded providing the **Land Size** by Country, **Population** by Country **times series from 1970 to 2019** and **GDP** by Country **time series from 1970 to 2019**. Note that the images below only show 2019 data in the time series. Please view the excel files for the full time series.

  - [Land size by Country](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/landareasqkm.xlsx)

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/landbycountry10050.jpg "Land Size by Country")
  - [Population by Country](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/popularindicators.xlsx)

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/popbycountry10050.jpg "Population by Country")
  - [GDP by Country](https://github.com/Readri205/MS2_Project/blob/master/assets/documents/excelfiles/popularindicators.xlsx)

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/gdpbycountry10050.jpg "GDP by Country")

- Lists of countries in all of the World Bank Database Sectors. Note that the list for 'Africa' and 'Middle East' are adjusted to account for the 6 countries (Algeria, Egypt, Morrocco, Libya, Djibouti and Tunisia) from the World Bank Database 'Sub-Saharan Africa' and 'Middle East & North Africa' economic sectors.
  - **Africa**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/africa1050.jpg "Africa")
  - **Middle East**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/middleeast10050.jpg "Middle East")
  - **Latin America & Caribbean**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/latinamericacaribbean10050.jpg "Latin America & Caribbean")
  - **North America**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/northamerica10050.jpg "North America")
  - **East Asia & Pacific**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/eastasiapacific10050.jpg "East Asia & Pacific")
  - **Europe and Central Asia**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/europecentralasia10050.jpg "Europe & Central Asia")
  - **South Asia**

      ![alt text](https://readri205.github.io/MS2_Project/assets/documents/excelfiles/southasia10050.jpg "South Asia")

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
