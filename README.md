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

* Have a centralized repository for specification information
* Allow the creation of new products that follows a defined procedure that insures all information is collected from the various departments
* Ability to change details for the product after submission
* Email notifications/reminders of new products and upcoming products that require attention
* Different form fields/structure depending on the customer/department to meet customer spec requirements
* Easy to use navigation/intuitive design
* Product specification information is easy to read/find

### User Stories

* As a quality manager, I often find it difficult to find/gather all relevant product information when new products/lines start because different departments that are responsible for different aspects of the product development don't communicate the information effectively. This leads to frustration on my teams part and leads to difficulties when inspecting produce as we aren't sure what we need to be checking for. A centralized/structured application that simplifies this process of information gathering and stores the information would be of great benefit to me and my team.
* As a production manager, when a new product is due to be started I need to know a lot of different details about the product before I can start production on it. This information can include packaging details, quality information, product specification information and so on. This information is often maintained by different departments which makes gathering all the information troublesome and time consuming and can lead to mistakes when information isn't communicated effectively or assumptions are made. This miscommunication ultimately degrades customer confidence/satisfaction when we send produce that doesn't meet the required specification. We need a structured setup that makes this process easier for all parties. As my work often involves me walking around large warehouses and not at my desk, I need the information to be easily accessible on a mobile device so that I can access the information on the go.
* As a commercial buyer I need the interface to be quick and easy to use and tell me what information I need to supply depending on the customer. I also need it to inform the other relevant departments when I create a new product.

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

For the design of the website, I wanted the user interface to be simple, formal and minimalistic with icons to help visually convey to the user the meaning behind a section. The main purpose of the site is to display information about upcoming products and store product specification information. I considered the [Materialize CSS](https://materializecss.com/) and [Bootstrap](https://getbootstrap.com/) frameworks for this. Having used Bootstrap for my first two milestone projects, I felt that I should try my hands with Materialize to challenge myself. It also had the added benefit of having an icon library without the need to use [Font Awesome](https://fontawesome.com/). The responsive tables, grid layout, great inputs and easy to use colour classes were very useful.

![Upcoming Products View](/static/images/upcoming_products_view.png)

#### Colours

When considering what colours to use for the site I was concious of the fact that the site was for professional industry use and so should prioritize cleanly displaying information to the user above any artistic considerations. I felt a plain white background for the main body of the page was appropriate and black text. For the navigation section I wanted to display the company logo and as such I felt the colour of the navbar should match that. Given the green colour of the company logo I sought to match that and so used the [color classes](https://materializecss.com/color.html) in Materialize and settled on a *green accent-3* colour. For the colours of the buttons I wanted to use similar colours so I chose *green accent-3* again and *blue accent-3*.

#### Fonts

Due to the professional nature of the site I wanted the font to be clean and easily legible. I felt the default Materialize font was perfect for this.

### Process Flow

The process flow diagram below was created using [Creately](https://creately.com/).

![Process Flow](/static/images/process_flow.png)

Understanding the process of new product acquisition was key to understanding and building an application that could solve the miscommunication problem evident in the workflow.

After sitting down with stakeholders from the different departments in the company we agreed on the above process flow that the application should enforce on the new product acquisition process.

#### Process Flow Steps

1. A member of the commercial team obtains a contract for a new product/line with a customer.
2. The commercial team member creates a new product in the application and fills in all the information they have for the product at that point in time.
3. This sends out notifications to all other relevant teams and departments to inform them of the new product.
4. Other team members can log into the application and review the information submitted so far.
5. They can then submit the information that they are responsible for to the application.
6. This sends out another notification, notifying the relevant team members that a product has been updated.
7. Once all departments have submitted their required information for the product, the commercial team can sign off on the product as *Production Ready*

### Wireframing

For wireframing, I used [Balsamiq](https://balsamiq.com/). The site required a multiple page setup to handle the various forms/views that the application required. I felt that the site should focus purely on the information relevant to that page and not cluttered with excess distracting elements that would make the site bloated and unintuitive.

#### Upcoming Products View

![Upcoming Products View](/static/images/upcoming_products_wireframe.png)

The upcoming products view is the default route for the application and displays all new products that are due to be started in the coming weeks/months. The products are divided into two categories, one for *Confirmed* products which are production ready and one for products that are *Pending* further information from other departments. The distinction between the two is important and highlights to the users which products are ready and which are not, the icons also assist with that. The two tables display the base details for the product, the name, division, customer, status, start date and created by attributes of the product.

The navbar shows relevant links for the user and wraps to become a side nav on mobile. In the wireframes you can see that on mobile views I had initially thought to keep the horizontal nature of the tables while simply removing some of the less important attributes from the table so that it could fit on a mobile screen. This proved difficult to implement in practice however and I instead used the [Materialize Responsive Table class](https://materializecss.com/table.html) which converts the table to vertical headers and horizontally scrollable on mobile.

#### Create Product View

![Create Product View](/static/images/create_product_wireframe.png)

The *Create Product* view is the view that the commercial team would see when they go to create a new product. It is a simple form template but the fields would adapt, depending on the customer the product is for, as different customers have different specification details for their products. The form fields would appear in two columns on desktop and wrap to a single column on mobile. Once the product is added, the user will be redirected to the *Upcoming Products* view with an alert message informing them that the product was successfully added. The form would contain a variety of elements including *multiselects* and *datepickers*.

#### My Tasks View

![My Tasks View](/static/images/tasks_wireframe.png)

The *My Tasks* view displays the upcoming products which have not had details added by the current users department. As I will describe later in the *Data Strucure* section, each user has a department *(Fruit, Vegetables, Potatoes, etc.)* and a role *(Commercial, Packaging, Operations, Production)*. If an upcoming product does not have that role's information then it will be displayed here for the user so they can see what products they have to add information for.

### Data Structure

This project required the use of a [MongoDB](https://www.mongodb.com/) non-relational database which I felt suited this project particularly well as it allowed for different objects/documents to have different attributes to another which was a requirement for the products which could have different attributes depending on the customer/department that the product was for. This structure would have been difficult to design with a traditional SQL relational database. I did, however, use some *relational* database techniques to reduce the need for maintenance going forward. These included creating tables for customers, departments and other select options which would have been repetitive to store as options arrays for each form field list. This meant that I didn't have to hard-code options for selects and so on.

#### One-To-Many Collections

##### Customers/Departments/Roles

I wanted to reduce the need for future maintenance as much as reasonably possible. To accomplish this I made collections for customers as opposed to hard-coding them in selects. These attributes would be used in the *products/users/form_fields* tables to refer to the customers/departments/roles information.

###### Customer Example

```javascript
{
    "_id":{
        "$oid":"609e74726a5c9078cdd4433b"
        },
    "customer_name":"Aldi"
} 
```

###### Role Example

```javascript
{
    "_id":{
        "$oid":"609e3bc9234196db4a0429e0"
        },
    "role_name":"Commercial"
}
```

###### Department Example

```javascript
{
    "_id":{
        "$oid":"609d5fa37140c981d74d658b"
    },
    "department_name":"Fruit"
}
```

##### Option Tables

For selects/multiselects with a lot of options and that are used frequently across forms, such as *origins*, *varieties* and *defects*, it didn't make sense to create arrays with the same options repeated multiple times for different form fields. This would have made them difficult to maintain if a new origin or variety was added. As such, I felt it was necessary to create collections for them and join them to the select/multiselect field entry with the collection name.

The collections use the same attribute *name* to refer to the actual option name which made it easier to build the options array when creating the options array for the forms.

###### Origin Example

```javascript
{
    "_id":{
        "$oid":"609ea9576a5c9078cdd44343"
    },
    "name":"Ireland"
}
```

###### Variety Example

```javascript
{
    "_id":{
        "$oid":"609ea9a46a5c9078cdd44348"
    },
    "name":"Pink Lady"
}
```

###### Defect Example

```javascript
{
    "_id":{
        "$oid":"60a76b96a0a944d77be9b8bd"
    },
    "name":"Rots"
}
```

#### User Collection

When creating a template for a user object I realized I would need several attributes. The first attribute I needed was a *username* which the user could use to log in as well as be stored in a session variable to use later to query for different user attributes. I also needed a first and last name for the users to be used in the *Created By*/*Added By* fields in the product information collection. I felt this was preferable to just storing the users *username* as it might be difficult to decipher someones real name from simply a *username*. I also needed to store user's email addresses so that I could use them to send emails to about new products being created. I also needed to store a hash of the users password to secure the log in.

I also needed a *department* and *role* for each user. These attributes would be used to determine the user's level of access and ability to create/add information for a product. For instance, a *Fruit* buyer cannot create a *Vegetable* product and a *Commercial* user cannot add *Packaging* information etc. There are roles, however, *(Packagaing, Operations)* that do not have a specific department, so I created a department *All* to refer to these users. I also needed to create an *Admin* role that was capable of editing all information.

##### User Example

```javascript
{
    "_id":{
        "$oid":"609e4194439f6ab11e2e742b"
    },
    "username":"jamessummersby",
    "f_name":"James",
    "l_name":"Summersby",
    "email":"jamessummersby@meadefarm.ie",
    "password":"pbkdf2:sha256:123456$1234EXAMPLEHASH567890",
    "department":"Fruit",
    "role":"Commercial"
}
```

#### Form Fields Collection

Because each customer and, sometimes, each department uses has different specification requirements, it was a requirement that all product detail forms had unique fields depending on the department/customer.

There were a couple of options for how to manage this. One solution could've been to create unique form html templates for each department/customer combination. This would have worked but would have been difficult to maintain if specifications changed or if a new customer or department was added. A developer would have to manually go in and create a new route and template for the new customer/department combination and validate that the form submitted correctly with the appropriate fields.

I didn't want the application to have this burden and instead decided to store the fields required for each customer/department combination in a collection.

##### Form Field Example

```javascript
{
    "_id":{
        "$oid":"609e93516a5c9078cdd44341"
    },
    "customer":"Aldi",
    "department":"Fruit",
    "commercial_details":[
        {
            "field_name":"product_name",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"start_date",
            "field_type":"date"
        },
        {
            "field_name":"case_count",
            "field_type":"input",
            "input_type":"number"
        },
        {
            "field_name":"weight_per_unit",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"approved_origins",
            "field_type":"multiselect",
            "options_type":"table",
            "table_name":"origins"
        },
        {
            "field_name":"approved_varieties",
            "field_type":"multiselect",
            "options_type":"table",
            "table_name":"varieties"
        },
        {
            "field_name":"product_code",
            "field_type":"input",
            "input_type":"number"
        },{
            "field_name":"date_coding",
            "field_type":"input",
            "input_type":"text"
        }
    ],
    "packaging_details":[
        {
            "field_name":"packaging_type",
            "field_type":"input","input_type":"text"
        },
        {
            "field_name":"packaging_grade",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"dimensions",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"recyclable",
            "field_type":"select",
            "options_type":"options",
            "options":["Yes","No"]
        },
        {
            "field_name":"biodegradable",
            "field_type":"select",
            "options_type":"options",
            "options":["Yes","No"]
        },
        {
            "field_name":"inner_pack_details",
            "field_type":"multiselect",
            "options_type":"table",
            "table_name":"pack_info"
        }
    ],
    "operations_details":[
        {
            "field_name":"storage_temperature",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"shelf_life_display",
            "field_type":"select",
            "options_type":"options",
            "options":["Use By","Best Before","Best Before End"]
        },
        {
            "field_name":"applicable_defects",
            "field_type":"multiselect",
            "options_type":"table",
            "table_name":"defects"
        },
        {
            "field_name":"specific_packing_information",
            "field_type":"textarea"
        },
        {
            "field_name":"known_allergen",
            "field_type":"select",
            "options_type":"options",
            "options":["Yes","No"]
        }
    ],
    "production_details":[
        {
            "field_name":"declared_weight",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"tare_weight",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"min_weight",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"target_weight",
            "field_type":"input",
            "input_type":"text"
        },
        {
            "field_name":"max_weight",
            "field_type":"input",
            "input_type":"text"
        }
    ]
}
```

Let's have a look at this example in a bit more detail.

```javascript
"customer":"Aldi",
"department":"Fruit",
```

The customer and department attributes, naturally, tell us which *customer* and *department* these fields are for.

```javascript
"commercial_details":[...],
"packaging_details":[...],
"operations_details":[...],
...
```

The above arrays refer to the ***role*** *(Commercial, Production etc)* that the array's details refer to, ie, the *commercial_details* array contains the fields that the **Commercial** team over the product must complete, the *packaging_details* array contains the fields that the **Packaging** team must complete for the product etc.

```javascript
{
    "field_name":"product_name",
    "field_type":"input",
    "input_type":"text"
}
```

The above example shows a field, every field has a *field_name* which is used for the elements **name** and **id** when the element is built by the app. The *field_type* specifies what type of element the field is, *input, select, multiselect, date*. The *field_type* will determine what other attributes the field will have. Because this element is an input, we also specify an *input_type* which states whether the input is a *text* or *number* input.

```javascript
{
    "field_name":"start_date",
    "field_type":"date"
}
```

The above example shows a *date input* example. We don't need any other attributes for the this input so that input field is complete.

```javascript
{
    "field_name":"approved_origins",
    "field_type":"multiselect",
    "options_type":"table",
    "table_name":"origins"
}
```

The above example shows an example of a *multiselect* element. It contains the standard *field_name* and *field_type* however we also need to know what the **options** are for the multiselect. We could simply create an options array here with all the origins but as described earlier in the *One-To-Many* collections section, because *approved_origins* is likely to be needed by multiple customer/department combinations and because it is a long list that is likely to be updated/changed we want to instead put the *origins* list in it's own collection. But we still need to tell the field where to get it's **options** list from. Hence, we give the field an attribute of *options_type* which is equal, in this instance, to *table* which the application in turn interprets that it needs to find the list of options for this field from a collection (table). We then also have to specify the *(collection)* ***table_name*** which tells the application to build the options for this element from the **origins** collection.

```javascript
{
    "field_name":"known_allergen",
    "field_type":"select",
    "options_type":"options",
    "options":["Yes","No"]
}
```

The above example shows a *select* element. Like the *multiselect* element we looked at earlier, it has an *options_type* attribute to define where the *select*'s options should come from. However, in this instance we aren't building the options from a collection, instead we are expicitly stating the options in the field object, defined by the *options_type* of **options**. We then have an **options** array containing all the options we want to appear in the select field, in this case the options will be ***Yes*** and ***No***.

#### Products Collection

For the *products* collection, we have base details which are common to each product. These include the *product name, department, customer, status, start date, created by* and *created on*. These are necessary for every product regardless of customer or department. All this information is supplied by the *commercial* team when they create a new product and so we keep this information at the base level of the product as opposed to putting it in a *commercial* object on the product. This made most sense to me when designing the data structure.

I initially considered removing the product header information altogether and simply keeping all details as attributes of an object of the role of the team that submitted the details like this:

```javascript
{
    "_id":{
        "$oid":"someid"
    },
    "commercial":[
        "product_name":"Bananas",
        "department":"Fruit",
        "customer":"Aldi",
        ...
    ],
    "packaging":{...},
    "production":{...},
    "operations":{...}
}
```

I considered this approach initially because I needed to have some way to check what departments had submitted their information for the product and what ones were still outstanding.

However, I felt this would look confusing for someone looking at the collection and make it awkward to use when simply trying to get the base details for a product.

I instead went for a structure where all the *commercial* details for the product are considered base details of the product and all other role *(Packaging, Production, Operations)* information is stored as objects on the product. This looks like this:

```javascript
{
    "_id":{
        "$oid":"someid"
    },
    "product_name":"Bananas",
    "department":"Fruit",
    "customer":"Aldi",
    ...,
    "packaging":{...},
    "production":{...},
    "operations":{...}
}
```

This does have it's trade-offs however, primarily when it comes to ease of access when displaying/editing the information in a product view as to iterate over it properly we have to check what the type of each attribute is.

##### Product Example

```javascript
{
    "_id":{
        "$oid":"60a3d0939e9ff14ca5411ac0"
    },
    "product_name":"Loose Lemons",
    "department":"Fruit",
    "customer":"Aldi",
    "status":"Pending - Awaiting Packaging",
    "start_date":{
        "$date":"2021-06-24T00:00:00.000Z"
    },
    "created_by":"James Summersby",
    "created_on":{
        "$date":"2021-05-18T15:34:59.785Z"
    },
    "case_count":"10",
    "weight_per_unit":"200g",
    "approved_origins":["Ireland"],
    "approved_varieties":["Rooster","Hylander"],
    "product_code":"84526",
    "date_coding":"1-8 Days",
    "operations":{
        "storage_temperature":"3 degrees",
        "shelf_life_display":"Best Before",
        "applicable_defects":["Rots","Skin Defects"],
        "known_allergen":"Yes"
    },
    "production":{
        "added_by":"Production Test",
        "date_added":{
            "$date":"2021-05-21T10:43:28.605Z"
        },
        "declared_weight":"750g",
        "tare_weight":"50g",
        "min_weight":"800g",
        "target_weight":"800g",
        "max_weight":"850g"
    },
    "packaging":{
        "packaging_type":"na",
        "packaging_grade":"na",
        "dimensions":"na",
        "recyclable":"Yes",
        "biodegradable":"Yes",
        "inner_pack_details":["Machine No."]
    }
}
```

As you can see in the above example we have base details for the product stored at the same level as the *_id* of the product and then we store all other team information in objects of the team *(Packaging, Operations, Production)*. You can also see that the attributes have the same name as the *field_name* from the element that was created for the field.

You can see a few objects are arrays which means that their fields were *multiselects*.

## Features

### Existing Features

* Create Product functionality
* Login/Register functionality
* Upcoming Products view
* Email Notifications
* Product details view
* Forms that generate fields depending on the customer/department
* Users can submit the details pertinent to their department only
* Structured/well defined new product development process
* Printable pdf with custom style rules
* Staged progress for product completion that ensures all information is captured
* Digital signature sign off
* Admin functionality to edit all fields
* Intuitive design and easy to understand and use
* User verification that ensures only users with the correct roles/permissions can access/edit content
* My tasks view where users can see their tasks easily
* Daily quotes API that shows inspirational quotes to users

### Future Potential Features

* Image upload capabilities
* Integration with our ERP (Enterprise Resource Planner)
* Allow reactivation of products that are completion but have been made in active
* Allow users to add own Varieties/Origins
* Add more Unit tests
* Allow users to create own forms for customers/departments
* Serverside scripting to automatically send updates when product start dates are approaching

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
* [Balsamiq](https://balsamiq.com/)
* [Creately](https://creately.com/)
* [pytest](https://docs.pytest.org/en/6.2.x/)
* [Signature Pad](https://github.com/szimek/signature_pad)

## Testing

For Testing information regarding this project please see the [TESTING.md](/TESTING.md) file.

## Deployment

The database for this project is a MongoDB created using Mongo Atlas.

To create a database similar to this one:

1. Navigate to [MongoDB](https://www.mongodb.com/)
2. *Sign In* or *Create an Account*
3. Create a new project folder.
![Mongo Create Project](/static/images/mongo-create-project.png)
4. On the next page click *Create Project*
5. In the project folder, click the *Build a Cluster* button
![Cluster Build](/static/images/cluster-build.png)
6. Choose the FREE *Shared Cluster* option and choose the region closest to yours.
7. Once created, 

This project was deployed using [Heroku](https://www.heroku.com/)

## Credits

### Helpful Links/Tutorials

[Jinja Comparisons](https://jinja.palletsprojects.com/en/3.0.x/templates/#comparisons)
[Jinja Comments](https://jinja.palletsprojects.com/en/3.0.x/templates/#comments)
[StackOverflow Jinja Test](https://stackoverflow.com/questions/11947325/how-to-test-for-a-list-in-jinja2)
[Signature Pad](https://github.com/szimek/signature_pad)
[Quotable API](https://github.com/lukePeavey/quotable)
