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
