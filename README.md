# Meade Product App

![Meade Farm Logo](/static/images/meade_farm_logo.png)

## Contents

1. [Project Inception](#project-inception)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies](#technologies)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Project Inception

At time of writing, I am currently employed by Meade Farm Group, a fresh goods processor based in the Republic of Ireland, servicing the retail food sector, supplying fresh goods to the likes of Lidl and Aldi amongst others. Due to the rapidly changing and dynamic industry the company competes in, we often take on new products or lines at short notice. The pace at which new products/lines are introduced by the commercial team often means that information is often lost in translation between departments which can lead to the members of staff more directly involved in the processing of the new product/line lack the required information (barcodes, specs, varieties etc.) to process the product correctly. This can lead to produce being sent to customers that does not meet it's requirements and, sometimes, to rejections which negatively impacts customer trust and satisfaction in the company. It also leaves employees/departments left in the dark disgruntled and frustrated.

To solve this it was decided that a formal, structured system for logging new products/lines being undertaken was required to reduce eliminate this miscommunication deficit. Having developed other bespoke, locally-hosted applications for the company through the use of php, mysql and xampp, I decided that this project was suitable to test my ability with Flask, MongoDB and Heroku.

## UX

### Project Goals

The goal of this project is to create an application that enforces a well-defined procedure when new products/lines are started by the company. This procedure will ensure all stakeholders in the production process are aware of all the information relevant to the product and are not left in the dark. This will be facilitated in the appliaction through a portal (interface) which allows the user to see all the information for new products that are starting. Any new products/lines will be added to the system, starting with the commercial team who will fill out the details of the product that they are aware of, notifications will then be sent to the other departments (Packaging, Quality Control) who will fill out their details for the new product. Once after all departments have signed off on the product in the application will production on it will commence.

### User Goals

### User Stories

### Site Owner Goals

* As a site owner, I want the application to be easy to navigate and controls to feel intuitive.
* As a site owner, I want the database structure to be consistent, easy to maintain and allow for new parameters to be added to the acquisition process easily.
* As a site owner, I want the users to be easily able to see the new products and all the relevant information for them. (data browser)
* As a site owner, I want the process behind the acquisition of new products/lines to be well-defined within the application to allow for clarity and ease-of-mind for all stakeholders in the process.
* As a site owner, I want the process to be agreed upon by all stakeholders prior to development and for the process to be enforced.
* As a site owner, I want every stage in the process to result in notificaitions being sent to the relevant stakeholders to inform them of changes or information that they need to add.

### User Requirements and Expectations

#### Requirements

* **Login/Register system to add new users** - Each user entry should have a corresponding department and role so that only users of the relevant role/department to the new product can add the product information at that point in the process. Will also allow notifications to be sent to the relevant roles/departments when each step in the process advances.
* **Forms to fill out details of new products/lines** - Forms will be different for each stage of the process and may differ in details required depending on department. New product form will require basic details of product. When sent to packaging department it will have different fields that they need to fill out etc.
* **Table/Browser for users to fiew new products** - A data browser of some description where users can view/add/change the details of new products.
* **Staging Process for new products** - When a new product is added it starts at a certain stage, when one department it advances to the next stage, then the next department fills out their details and it then advances to the next stage etc until reaches *Completed* stage.
* **Email Notification System** - A facility that will notify the relevant departments of new products that have been added and ask for them to input their details before it can be advanced to the next stage.

#### Expectations

* **Clear and Intuitive Navigation**
* **Consistent and Visually Appealling Design/Colour Scheme**
* **Transparent and Easily Understandable Data Structure**

### Design Choices

### Wireframing

### Data Structure

## Features

### Existing Features

### Future Potential Features

## Technologies Used

### Languages

* [HTML5](https://devdocs.io/html/)
* [CSS3](https://devdocs.io/css/)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python 3.9](https://www.python.org/)

### Frameworks/Libraries/Tools

* [Heroku](https://www.heroku.com/)
* [MongoDB](https://www.mongodb.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [jQuery - JavaScript](https://jquery.com/)
* [Flask - Python](https://flask.palletsprojects.com/en/1.1.x/)
* [Materialize v1 - CSS](https://materializecss.com/)
* [emailJS](https://www.emailjs.com/)

## Testing

## Deployment

## Credits

https://jinja.palletsprojects.com/en/3.0.x/templates/#comparisons
https://jinja.palletsprojects.com/en/3.0.x/templates/#comments
https://stackoverflow.com/questions/11947325/how-to-test-for-a-list-in-jinja2