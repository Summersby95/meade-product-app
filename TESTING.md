# Testing

## Bugs

* Invalid bson ObjectId's
  * Fix: Add checks to see if *ObjectId* is valid before passing to Mongo query, add redirect and flash message if not valid.
* Materialize tables not fitting correctly on smaller screen sizes
  * Fix: Add *responsive-table* class to tables so that they change to horizontally scrollable tables on smaller screen sizes
* Non Commercial/Admin users allowed to edit commercial details/create products
  * Fix: add checks to verify user role prior to allowing product creations
* Multiple tables/view products/forms on different views using similar code
  * Fix: refactor jinja template building into macro functions for detail views/table views/form builders
* Admin not able to edit all details due to poor form building logic
  * Fix: rewrite add product details logic
* Date/Time objects appearing as raw date time in views
  * Fix: create datetime to string conversion function
* Users able to submit invalid responses in form elements
  * Fix: add regex pattern and title attributes to the form structure in mongodb which then are applied through the form builder macro to provide input validation.
* HTML validator giving warning saying section lacks heading
  * Fix: section was for flash messages, add check to verify there is messages before creating the section element

## Validator Testing

### HTML Validator Testing

I used the [Nu HTML Checker](https://validator.w3.org/nu/) for HTML validation and received a few errors initially. These included:

* No *alt* attributes on images. **Fix:** Add *alt* attributes to images.
* *Section* element missing heading. **Fix:** The section in question was the *flashes* section so I wrapped the section in an if statement to check for messages before creating the element.

Apart from that, I didn't receive any errors or warnings.

![HTML Validated](/static/images/html-validation.png)

### CSS Validator Testing

I used the [W3C Jigsaw CSS Validation Service](http://jigsaw.w3.org/css-validator/) for CSS validation. I received one error and a number of warnings however they were all pertained to the *Materialize CSS* stylesheets and so I was unable to repair them.

I did not receive any errors with my own CSS style sheets.

![CSS Validation](/static/images/css-validation.png)

### Javascript Validator Testing

I used [JSHint](jshint.com) for JavaScript validation testing, I also used the JSHint extension in VS Code during development.

I did not receive any errors from JSHint regarding my JS files.

### Python Validator Testing

I used the [Pylint](https://pypi.org/project/pylint/) and [pycodestyle](https://pypi.org/project/pycodestyle/) packages as linters during development to ensure my python code was PEP8 compliant.

There are only two outstanding warnings from pycodestyle for my *env.py* (not in this repo) for the MongoURI and a hashed passcode that are too long but I left as they were as they are environment variables.

## Lighthouse Testing

Using the Chrome Dev Tools, I was able to use the *Lighthouse Report* generator which highlighted a number of issues.

* Site should have *meta* description. **Fix:** Add *meta* description to base template.
* Largest Contentful Paint > 4.5 seconds on home page. **Fix:** Remove some of the images in the card section. I tried resizing the image on the home page to load faster but it proved difficult to bring down the time. In the end I removed a detailed, colourful picture in favour of a simpler, smaller size image that would load faster. I felt I had to do this as the LCP score was severely hampering my performance score on this page.
* Images should have *alt* attributes. **Fix:** Add *alt* attributes to images.

### Lighthouse Scores

#### Home Page

![Home Page Lighthouse Score](/static/images/home-lighthouse.png)

#### Upcoming Products Page

![Upcoming Products Lighthouse Score](/static/images/table-lighthouse.png)

The orange *87* score for *Best Practices* was due to a *Does not use HTTPS* notice which I was unable to resolve due to the nature of the deployment on Heroku.

![Best Practices Score](/static/images/heroku-score.png)

#### Form Pages

![Form Lighthouse Score](/static/images/form-lighthouse.png)

Unfortunately, due to large form fields and lots of elements and options, the performance score for the *Create Product* page was poor and the work required to make any substantial improvement to the score by potentially splitting the information into multiple forms was too big a task to fix given the time constraints.

One of the accessibility issues was poor contrast ratios between text and the underlying elements. I fixed this by changing the color of the nav and footer elements.

The Best Practices score was impacted by the same reasons as outlined above.

#### My Tasks Page

![My Tasks Lighthouse Score](/static/images/tasks-lighthouse.png)

## Feature Testing

### Create Product

![Create Product](/static/images/create-product.png)

Users can create products according to customer/department specifications.

### Login/Register

![Register](/static/images/register.png)

Users can login/register with their credentials.

### Upcoming Products View

![Upcoming Products Demo](/static/images/upcoming_products_demo.png)

Users can easily view upcoming products, divided into confirmed and pending approval, they can add their details, view the product and sign off on the product.

### Email Notifications

![Email Notifications](/static/images/email-notifications.png)

Email notifications are sent to users to notify them of new products being created/updated.

### Product Details View

![Product Details](/static/images/product-view.png)

Users can view all submitted details for the product.

### Customer/Department Specific Forms

![Form Data Structure](/static/images/form-structure.png)

The form data structure allows inputs to be generated from the Mongo BSON Objects so that forms can be created and updated with ease rather than new views/templates having to be created.

### Structured New Product Development Process

![Development Process](/static/images/process_flow.png)

The structured process means that every department is allowed an input before a product is signed off for production.

### Printable PDF with custom style rules

[PDF Example](/static/misc/product_details.pdf)

![Print Example](/static/images/print.png)

Printable product details mean that the product details can be printed off easily and given to operatives who need the information.

### Digital Signature Sign Off

![Sign Off](/static/images/signoff.png)

A digital signoff canvas element allows users to sign off before a product is designated as production ready.

### Admin Functionality

![Admin Functionality](/static/images/admin.png)

Admin logins allow admins to go in and make edits on any products when other users are unable to.

### My Tasks View

![My Tasks](/static/images/my-tasks.png)

The my tasks view allows users to easily see what products require their attention. It provides an inspirational quote to increase motivation and productivity!

