# Meade Product App

![Site Showcase](/static/images/responsiveness.png)

## Contents

1. [Project Inception](#project-inception)
2. [UX](#ux)
3. [Application Logic](#application-logic)
4. [Features](#features)
5. [Technologies](#technologies-used)
6. [Testing](#testing)
7. [Running Locally](#running-locally)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Project Inception

[Deployed Site](http://meade-product-app.herokuapp.com/)

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

## Application Logic

The business logic that underpins the application is bespoke and while the interactions that a user can make are immediately evident to the user upon login, I feel the need to explain the logic in a bit more detail so that a non-Meade Farm employee will understand the reasoning behind it.

### Users

When a user registers, they are required to select a *role* and *department*. A *role* is their job within the company, e.g. *Commercial* is responsible for buying/selling produce, *Production* is responsible for the physical *production* of the product, etc. A *department* is the sub division of the company the employee works under, e.g. *Fruit* deal with *fruit* products, *Vegetables* deal with *vegetable* products, etc.

We have a number of *roles* that a user can be in terms of the application process who have distinct access/information they have to submit during the new product development process. *Commercial* is one of these roles. In Meade Farm Group, a commercial employee has a specific *department* that they work under, *Fruit, Vegetables, Potatoes etc*, as such when a new *commercial* user is registering they must select their department. This will determine what products they can create, ie, they are restricted to being able to create products for their *department*.

All *roles* excluding *commercial* are **not** specific to a single *department*, hence why there is the *All* department, signifying users whose *role* responsibilities are over multiple or *all* departments.

### Customers

We have a variety of customers, *Aldi, Lidl, Iceland, Dunnes Stores etc*, that we supply produce for. When a new product is created, the specification and information required for the product depends on the *customer* and also the *department* that the product falls under.

This is why we have a *form_fields* collection that stores the form details for each *customer/department* combination. These are then built using a jinja macro.

### Product Creation

As you will have seen in the process flow diagram above, the first step in the new product development workflow occurs when a member of the *commercial* team obtains a new contract for a product line. Once they have the details of this contract, they will create a new product in the application.

Because *Commercial* users belong to a specific *department* they are not prompted to select a department when creating a new product. They simply have to select the *customer* the product is for so the application can fetch the relevant form field list for the *customer/department* combination.

*Admin* users are not *department* specific, so when they are creating a new product they must select the *department* that the product is for.

*Commercial* and *Admin* users are the only users with the ability to create new products. No other users have the authority or ability to start a new product.

### Product Updating/Adding Details

![Allowed Edit](/static/images/allowed-edit.png)

Once a new product is created, a notification email is sent to users in the same *department* as the product and to all users in the *All* department. The product is also given the status of *Pending - Awaiting Many*.

Only users from the product's *department* or the *All department* can edit/add details for a product. As you can see above The current user is a *Fruit* user and so besides the *View Product* button on products that have a different department to theirs they see a *Not Allowed* button, meaning they cannot edit it. For products that they are in the same *department* of they can add details relevant to their *role*.

*Users* who are a member of the *All* department can add their *role* details to any product.

When adding details/editing a product, a user can only edit/add details relevant to their *role*, i.e, a *Commercial* user can edit *commercial* details but cannot add *operations* details, likewise a *Packaging* user can add/edit *packaging* details but cannot add/edit *commercial* or *technical* details etc.

If the details for the product already exist they are displayed in the fields and will be updated when the form is submitted.

*Admin* users can add details for all *roles* and for any *department*.

### Sign Off/Moved To Completed

![Outstanding Products Highlight](/static/images/outstanding-highlight.png)

When a product is updated or details are added for a product, the application checks which roles still have to submit details. If the number of outstanding *roles* to submit details is two or less it will concatenate the *role* names together for the status to show *Pending - Awaiting role1, role2* as you can see in the example above. If a product is awaiting only *Packaging* and *Technical* information, the status will be updated to *Pending - Awaiting Packaging, Technical*. If greater than two *roles* have two submit details for the product, it's status will remain *Pending - Awaiting Many*.

When all information for the product has been submitted, the product's status changes to *Pending - Awaiting Commercial Sign Off*. At this point, instead of seeing an *Add Details* button beside the *View Product* button in the *Upcoming Products/My Tasks* tables, *Commercial* and *Admin* users will instead see a *Sign Off* button which will direct them to the sign off template where they can submit a digital signature to confirm the product is production ready. At this point, the product's status is changed to *Completed - Production Ready* and moves to the *Confirmed* table.

![Sign Off](/static/images/signoff.png)

If the product is still pending then users can still go in and edit the product, however, once the product has been signed off and confirmed, no edits can be made.

### Deleting Products

![Delete Access](/static/images/delete-access.png)

A product can be deleted via the *Product View*, the button will be at the bottom of the page. A product can only be deleted by a *Commercial* user from the same department as the product or by and *Admin*.

![Delete Confirm](/static/images/delete-confirm.png)

The user will be prompted for confirmation before a product is deleted.

### Table Logic

There are three different product table views in the application, I will now explain the purpose and logic of each.

#### Upcoming Products

![Upcoming Products](/static/images/upcoming_products_demo.png)

The upcoming products table view shows two tables, one for *Confirmed - Production Ready* products and another for all *Pending* products. The tables show all upcoming products regardless of department or customer or status. They are ordered by ascending start date.

*Confirmed* products remain in the table until their start date has passed. *Confirmed* products with a start date less than a week in the future will be highlighted green.

All *Pending* products are visible in the *Pending Approval* section, regardless of their start date or even if the date has passed. If the start date is less than a week away or has passed, a pending product will be highlighted red, if the start date is less than two weeks away it will be highlighted yellow.

The purpose of this section is to highlight what products require attention and what is happening around the factory.

#### All Products

![All Products](/static/images/all-products.png)

The all products view shows all products, not filtered by department or customer or status, ordered by *Product Name*. Users can go here to view products that no longer appear in the upcoming products table because their start date has passed and the product was *Confirmed*.

#### My Tasks

![My Tasks](/static/images/my-tasks-demo.png)

The my tasks view shows all products that require details for the logged in users *role*/*department*. It shows only products which do not have details that can be submitted by the logged in user.

*Admins* will see all pending products, *Commercial* users will see products that are awaiting sign off.

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

## Running Locally

To run this project locally you will first need to set up a database for all the data for this project. The database for this project is a MongoDB created using Mongo Atlas.

To create a database similar to the one used in this project:

1. Navigate to [MongoDB](https://www.mongodb.com/)
2. *Sign In* or *Create an Account*
3. Create a new project folder.
![Mongo Create Project](/static/images/mongo-create-project.png)
4. On the next page click *Create Project*
5. In the project folder, click the *Build a Cluster* button
![Cluster Build](/static/images/cluster-build.png)
6. Choose the FREE *Shared Cluster* option and choose the region closest to yours.
7. Once created and the cluster has finished provisioning, click on the *collections* button
8. Once there, click the *Add My Own Data* button.
![Add Data](/static/images/add-data.png)
9. In the new window, enter a name for your new database and use one of the collection names from the collections I described [above](#data-structure).
![DB Setup](/static/images/test-db.png)
10. Once you have created your database and collection, use the *Insert Document* button to insert an entry into the collection. I have provided examples above of the datastructure for each collection.
11. Click the *plus* icon beside your database name in the left hand column to create another collection.
![Create Collection](/static/images/collection.png)
12. Repeat steps, 9-12 until you have created all required collections for this project. I would encourage you to have at least one document in each collection.
13. Next, we need to configure network access and database access for your newly created database.
14. Under the *Security* heading in the left hand side navigation, click the *Network Access* tab
15. When there, click the *Add IP Address* button.
![Network Access](/static/images/network-access.png)
16. In the window that pops up click the *Allow Access From Anywhere* button and then click the *Confirm* button.
17. Next, click on the *Database Access* tab under the *Security* section.
![Database Access](/static/images/database-access.png)
18. Make sure the *Password* authentication method is selected.
19. In the *Password Authentication* form, create a new user name for the database and either type a password of your choosing or use the *Autogenerate Secure Password* button to generate the password for you.
20. Make a note of both the user name and password before going further, you will need these credentials to connect to your database from the application.
21. Ensure the *Database User Privileges* is set to *Read and write to any database*
22. Click *Create User*

Once you have completed the above steps, use the steps below to clone the repo and set up the project to run on your machine.

1. Open an empty window in the text editor of your choice.
![Visual Studio Code](/static/images/vs-code-window.png)
2. Your text editor should have an option similar to *Clone Git Repository*. Click on that button.
3. Copy and Paste the following link in the field that opens after clicking that button. [GitHub Repo Link](https://github.com/Summersby95/meade-product-app.git)
![Clone Repo](/static/images/clone-repo.png)
4. Select a folder on your computer to download the cloned repository.
5. Once downloaded, open the project folder in your editor
![Project Folder](/static/images/project-folder.png)
6. Open a new terminal in your editor.
7. Type the following command into the terminal.

```python
pip install -r requirements.txt
```

![Pip Install](/static/images/pip-install.png)
8. Once that is done, type the following command into the terminal

```python
pytest
```

At this stage, you should see a the following in your terminal:

![pytest 1](/static/images/pytest1.png)

This is informing us that we haven't created our *env.py* file and so it cannot verify our connection or collection structure is configured properly.
9. We now need to create our *env.py* file. In the base directory of the folder create a new file called *env.py*.
10. Copy and Paste the following example *env.py* code into the file.

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "abc123")
os.environ.setdefault("MONGO_URI", "mongotesturi")
os.environ.setdefault("MONGO_DBNAME", "testdb")
os.environ.setdefault("EMAIL_LOGIN", "test@gmail.com")
os.environ.setdefault("EMAIL_PASS", "abc123")
```

![env.py example](/static/images/env.png)
11. You do not need to change the IP or PORT environment variables. The first one that we need to change is the *SECRET_KEY*.
12. Head over to [RandomKeygen](https://randomkeygen.com/) and grab a *Fort Knox* password and replace the *SECRET_KEY* value of *abc123* with the password you have grabbed.
13. Next, we need to get our *MONGO_URI* from our created cluster.
14. Open your MongoDB web client, click on the *Clusters* tab, and click on the *Connect* button on the cluster you created your database in.
![Connect Cluster](/static/images/connect-cluster.png)
15. In the pop up window, click *Connect your application*.
16. In the *Driver* dropdown on the next window, select *Python* and for *Version* select *3.6 or later*
17. Copy the MongoURI connection string and paste it in the *env.py* file to replace the *mongotesturi* string in the example above.
![MongoURI](/static/images/mongo-uri.png)
18. Replace the *root* part of the connection string with the username that you chose for your database access user.
19. Replace the ```<password>``` part of the connection string with the password you chose for your database user.
20. Replace the *myFirstDatabase* with the name you chose for your database.
21. Replace the *MONGO_DBNAME* value of *testdb* with the same database name.
22. Back in the terminal of your editor, run the ```pytest``` command again.
23. If all is working as it should be you should see something similar to below.
![pytest2](/static/images/pytest2.png)
24. You can ignore the warnings from the test, if there are no errors in the terminal this means the connection is valid and you have set up your database correctly
25. If you receive any errors in the terminal, please read the error carefully and traceback through the steps above to resolve it. Ensure you have followed all the steps outlined above.
26. Next, you will need to create a Gmail accout to act as the sending email address for the application.
27. The email address must be a Gmail account. The emails can be sent to any email address domain but the sending email address domain to be stored in the environment variables must be a Gmail account.
28. Once you have created the account, navigate to the [Account Security](https://myaccount.google.com/security) of your account and enable *Less secure app access*. This setting is required for the *smtp* email function.
![Email Access](/static/images/email-access.png)
29. Once this is done, replace the *EMAIL_LOGIN* and *EMAIL_PASS* environment variables with your new email address and password respectively.
30. If all is working correctly, simply type ```py app.py``` into the terminal and the server will start.
31. Navigate to ```localhost:5000``` to open the app and enjoy. Change the *5000* to the appropriate port if you specified a different port in your environment variables.

## Deployment

This project was deployed using [Heroku](https://www.heroku.com/). You can follow the following steps to deploy your project to Heroku. The following steps assume that you have created the database as described above and have your *env.py* file created and populated.

1. Create a Heroku account and login.
2. Click the *New* button up the top right of the screen and select *Create New App*
3. Choose an app name and region for the application deployment.
![New App](/static/images/new-app.png)
4. Click *Create App*
5. Under the *Deploy* tab in the *Deployment Method* section click *Connect To GitHub*
6. Login to your *GitHub* account if you aren't already
7. Search for the name of the repo that you have created for this application.
![Repo Connected](/static/images/repo-connected.png)
8. Once selected, connect the repo to the application
9. Once done, navigate to the *Settings* tab in the application.
10. In the *Config Vars* section, click *Reveal Config Vars*
11. For each of the enviroment variables in your *env.py* file, add a new *KEY, VALUE*
![Config Vars](/static/images/config-vars.png)
12. Once done, navigate back to the *Deploy* tab, in the *Automatic Deploys* section, select the branch of the repo that you want to deploy and click the *Enable Automatic Deploys* button
![Automatic Deploys](/static/images/automatic-deploys.png)
13. This should trigger a deployment to initiate.
14. Navigate to the *Overview* tab.
15. In the *Latest Activity* section, you should see the newest build in progress.
![Activity Feed](/static/images/activity.png)
16. Once the build has finished it should have succeeded. If it failed, click the *View build log* button and attempt to resolve the errors.
17. If the build succeeded, click the *Open App* button at the top right of the page and you should be able to view your newly deployed application.

## Credits

You can find links to all of the libraries and frameworks I used in the [Technologies Used](#technologies-used) section.

### Helpful Links/Tutorials

* [Jinja Comparisons](https://jinja.palletsprojects.com/en/3.0.x/templates/#comparisons)
* [Jinja Comments](https://jinja.palletsprojects.com/en/3.0.x/templates/#comments)
* [StackOverflow Jinja Test](https://stackoverflow.com/questions/11947325/how-to-test-for-a-list-in-jinja2)
* [Signature Pad](https://github.com/szimek/signature_pad)
* [Quotable API](https://github.com/lukePeavey/quotable)
* [Largest Contentful Paint (LCP)](https://web.dev/lcp/)
* [pytest](https://docs.pytest.org/en/6.2.x/)
* [RegExr](https://regexr.com/)

### Special Thanks

* Caleb Mbakwe, my mentor, whose advice, mentorship and guidance was invaluable on this project.
* My manager, Stephen Boylan and colleague, Pawel Puszer for their support, feedback and for picking up the IT slacked when I was too busy focusing on this.
* Tim Nelson, for his helpful feedback during one of our masterclasses.
* Meade Farm Group, my managers, co-workers and colleagues who gave me the opportunity to work on this project for the company and who told me what they wanted in this application and had faith in me to deliver for them.
* The amazing coding community worldwide whose open-source projects and platforms made this possible (:
