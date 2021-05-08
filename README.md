# Meade Product App

![Meade Farm Logo](/assets/images/meade_farm_logo.png)

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
