# Super Pizza

## Planning & Development

### Target Audience

### App Objectives

### Features to Implement

### Wireframes

<details><summary>Pizza Page</summary>

  ![Mobile wireframe](./README/wireframes/pizza_list/mobile.png)
  ![Ipad wireframe](./README/wireframes/pizza_list/tablet.png)
  ![Desktop wireframe](./README/wireframes/pizza_list/desktop.png)

</details>

<details><summary>Pizza Details Page</summary>

  ![Mobile wireframe](./README/wireframes/pizza_details/mobile.png)
  ![Ipad wireframe](./README/wireframes/pizza_details/tablet.png)
  ![Desktop wireframe](./README/wireframes/pizza_details/desktop.png)

</details>

<details><summary>Pizza Tracker Page</summary>

  ![Mobile wireframe](./README/wireframes/pizza_tracker/mobile.png)
  ![Desktop wireframe](./README/wireframes/pizza_tracker/desktop.png)

</details>

<details><summary>Pizza Order Page</summary>

  ![Mobile wireframe](./README/wireframes/pizza_order/mobile.png)
  ![Desktop wireframe](./README/wireframes/pizza_order/desktop.png)

</details>

<details><summary>Pizza Order Details Page</summary>

  ![Mobile wireframe](./README/wireframes/pizza_order_details/mobile.png)
  ![Desktop wireframe](./README/wireframes/pizza_order_details/desktop.png)

</details>

<details><summary>Profile and Order History Pages</summary>

  ![Profile wireframe](./README/wireframes/pizza_profile/profile.png)
  ![Order History wireframe](./README/wireframes/pizza_profile/order_history.png)

</details>

<details><summary>Pizza Basket Page</summary>

  ![Desktop wireframe](./README/wireframes/pizza_basket/desktop.png)

</details>

### Database Schema

![Database Schema](./README/db/schema.png)

### Colors

### Fonts

### Technologies

### Agile

## Marketing

### SEO

### Keywords

### Social Media


![Facebook mockup](./README/facebook/mockup.png)

*Go back to the [top](#super-pizza)*

## Features

### Existing Features

### Features to Implement

*Go back to the [top](#super-pizza)*

## Testing

### Manual Testing

#### Authentication

  - Verified the functionality of the registration form, ensuring all required fields are present and functional.

![Sign Up Form](./README/tests/manual_testing/authentication/register.png)

  - Validated the form's behavior when submitting incomplete or erroneous data (e.g., missing fields, invalid email format).
  - Tested the form's responsiveness across various devices to ensure usability.
  - Checked that successful registration results in the creation of a user account.

  - Verified that users receive confirmation emails.

![Sign Up Form](./README/tests/manual_testing/authentication/email_confirmation.png)

  - Tested the login functionality to authenticate registered users.

![Sign Up Form](./README/tests/manual_testing/authentication/login.png)

  - Verified that incorrect login credentials trigger appropriate error messages.
  - Tested the "Forgot Password" feature to confirm its functionality in allowing users to reset their passwords.

#### Authorization

  - Authenticated User
    - Confirmed that authenticated users can access and manage their profiles.
    - Validated the functionality to view order history and edit personal details for checkout.
    - Verified that authenticated users with at least one order can write testimonials.
    - Ensured testimonial submission is restricted until the user meets the minimum order requirement.

![Authenticated User](./README/tests/manual_testing/authorization/pizza_list_authenticated.png)

  - Worker
    - Tested the additional "Orders" navigation link accessible to workers.

![Worker](./README/tests/manual_testing/authorization/worker.png)

  - Admin
    - Validated additional profile dropdown menu options available to admins.
    - Confirmed functionality to add pizzas, toppings, and provide testimonials from the admin profile.
    - Checked access to the admin panel through the designated navigation link.

<details><summary>Admin Authorization</summary>

  ![Admin](./README/tests/manual_testing/authorization/admin_nav_dropdown.png)
  ![Admin](./README/tests/manual_testing/authorization/add_pizza.png)
  ![Admin](./README/tests/manual_testing/authorization/approve_testimonial.png)
  ![Admin](./README/tests/manual_testing/authorization/edit_topping_form.png)
  ![Admin](./README/tests/manual_testing/authorization/pizza_list_admin.png)

</details>

![Admin Nav and Profile Dropdown](./README/tests/manual_testing/authorization/admin_nav_dropdown.png)

    - Verified admin privileges within the admin panel, including editing/deleting products and testimonials.
    - Ensured that under product cards (e.g., pizzas, toppings), admins can access links to edit or delete them.
    - Verified admin access to approving or deleting testimonials.

#### Form Validation

  - Validated Add Pizza form.

![Add Pizza form](./README/tests/manual_testing/forms/)

  - Validated Edit Pizza form.
  - Validated Add Topping form.
  - Validated Edit Topping form.
  - Validated Login form.
  - Validated Registration form.
  - Validated Profile form.
  - Validated Checkout form.
  - Validated Provide Testimonial form.
  - Validated Track Order form.

#### Crud

#### Price

#### Bag

#### Checkout

#### Tracking System

#### Profiles

#### Testimonials

#### UX

#### Responsiveness

#### Navbar

  - The navbar has been tested on all pages and all links are working correctly.
  - The navbar has been tested on all screen sizes and the links are displayed correctly.
  - The selected page link is highlighted in the navbar.
  - The dropdown menu has been tested on all screen sizes and the menu works correctly.
  - The burger appears on small screens and the menu is displayed when the burger is clicked.
  - The links in the burger menu have been tested and all links are working correctly.
  - Authenticated users can view and access their profiles from the dropdown menu located under the profile icon.
  - Workers can see and have access to Orders link.
  - Admins can see and have access to Orders and Admin links. From the dropdown menu of the profile icon, the admin has additional options to add pizza, add toppings, and provide testimonials.

#### Footer

  - The footer appears on all pages.
  - The footer is displayed correctly on all screen sizes.
  - The footer links have been tested and all links are working correctly.
  - The MailChimp subscription form has been tested and the form works correctly.
  - The information like "Opening Hours", "Our Location" and "Contact Us" is displayed correctly.

![Footer](./README/tests/manual_testing/footer/footer.png)

### HTML Validation

  - All HTML files have been validated using the W3C HTML Validator, with no errors or warnings found.

<details><summary>Login, Sign Up</summary>

  ![W3C HTML Validation](./README/tests/validation/html/login.png)
  ![W3C HTML Validation](./README/tests/validation/html/register.png)

</details>

<details><summary>Pizza List, Pizza Detail, Add and Edit Products Forms</summary>

  ![W3C HTML Validation](./README/tests/validation/html/add_pizza.png)
  ![W3C HTML Validation](./README/tests/validation/html/add_topping.png)
  ![W3C HTML Validation](./README/tests/validation/html/edit_pizza.png)
  ![W3C HTML Validation](./README/tests/validation/html/edit_topping.png)
  ![W3C HTML Validation](./README/tests/validation/html/products_pizza_details.png)
  ![W3C HTML Validation](./README/tests/validation/html/products_pizza_list.pngg)

</details>

<details><summary>Shopping Bag, Checkout, Checkout Success, Profile</summary>

  ![W3C HTML Validation](./README/tests/validation/html/bag.png)
  ![W3C HTML Validation](./README/tests/validation/html/checkout.png)
  ![W3C HTML Validation](./README/tests/validation/html/checkout_success.png)
  ![W3C HTML Validation](./README/tests/validation/html/profile.png)

</details>

<details><summary>About, Testimonials, Provide Testimonials</summary>

  ![W3C HTML Validation](./README/tests/validation/html/about.png)
  ![W3C HTML Validation](./README/tests/validation/html/add_testimonials.png)
  ![W3C HTML Validation](./README/tests/validation/html/testimonials.png)

</details>

<details><summary>Order Status Management, Tracker, Tracker Progress Bar</summary>

  ![W3C HTML Validation](./README/tests/validation/html/orders_status_management.png)
  ![W3C HTML Validation](./README/tests/validation/html/tracker.png)
  ![W3C HTML Validation](./README/tests/validation/html/tracker_bar.png)

</details>

### CSS Validation

  - The CSS code has been validated using the W3C CSS Validator (Jigsaw), and no errors were found.

<details><summary>Order Status Management, Tracker, Tracker Progress Bar</summary>

  ![W3C CSS Validation](./README/tests/validation/css/base.png)
  ![W3C CSS Validation](./README/tests/validation/css/checkout.png)
  ![W3C CSS Validation](./README/tests/validation/CSS/profiles.png)
  ![W3C CSS Validation](./README/tests/validation/css/testimonials.png)

</details>

### JavaScript Validation

  - The JavaScript file has been validated using the JSHint JavaScript Validator, and no errors were detected."

<details><summary>Validated bag.js, checkout_stripe.js, products_pizza_detail, products_pizza_list.png, static_index.js files</summary>

  ![JS Hint Validation](./README/tests/validation/js/bag_bag.png)
  ![JS Hint Validation](./README/tests/validation/js/checkout_stripe.png)
  ![JS Hint Validation](./README/tests/validation/js/producs_pizza_detail.png)
  ![JS Hint Validation](./README/tests/validation/js/products_pizza_list.png)
  ![JS Hint Validation](./README/tests/validation/js/static_index.png)

</details>

### Python Validation

  - The Python PEP8 validation tests were performed to assess the adherence of the application's Python code to the PEP8 style guide and no errors were detected.

<details><summary>Validated python files from about app</summary>

  ![PEP8 Validation](./README/tests/validation/python/about_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/about_view.png)

</details>

<details><summary>Validated python files from bag app</summary>

  ![PEP8 Validation](./README/tests/validation/python/bag_context.png)
  ![PEP8 Validation](./README/tests/validation/python/bag_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/bag_view.png)

</details>

<details><summary>Validated python files from checkout app</summary>

  ![PEP8 Validation](./README/tests/validation/python/checkout_admin.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_apps.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_forms.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_models.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_signals.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_view.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_webhook.png)
  ![PEP8 Validation](./README/tests/validation/python/checkout_webhook_handler.png)

</details>

<details><summary>Validated python files from order_status_management app</summary>

  ![PEP8 Validation](./README/tests/validation/python/order_status_management_models.png)
  ![PEP8 Validation](./README/tests/validation/python/order_status_management_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/order_status_management_views.png)

</details>

<details><summary>Validated python files from order_tracker app</summary>

  ![PEP8 Validation](./README/tests/validation/python/order_tracker_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/order_tracker_views.png)
  ![PEP8 Validation](./README/tests/validation/python/order_tracker_forms.png)

</details>

<details><summary>Validated python files from products app</summary>

  ![PEP8 Validation](./README/tests/validation/python/products_forms.png)
  ![PEP8 Validation](./README/tests/validation/python/products_models.png)
  ![PEP8 Validation](./README/tests/validation/python/products_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/products_utils.png)
  ![PEP8 Validation](./README/tests/validation/python/products_views.png)
  ![PEP8 Validation](./README/tests/validation/python/products_widget.png)

</details>

<details><summary>Validated python files from profiles app</summary>

  ![PEP8 Validation](./README/tests/validation/python/profiles_forms.png)
  ![PEP8 Validation](./README/tests/validation/python/profiles_models.png)
  ![PEP8 Validation](./README/tests/validation/python/profiles_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/profiles_views.png)

</details>

<details><summary>Validated python files from superpizza app</summary>

  ![PEP8 Validation](./README/tests/validation/python/superpizza_urls.png)
  ![PEP8 Validation](./README/tests/validation/python/superpizza_views.png)

</details>

<details><summary>Validated python files from testimonial app</summary>

  ![PEP8 Validation](./README/tests/validation/python/testimonial_forms.png)
  ![PEP8 Validation](./README/tests/validation/python/testimonial_models.png)
  ![PEP8 Validation](./README/tests/validation/python/testimonial_views.png)
  ![PEP8 Validation](./README/tests/validation/python/testimonial_urls.png)

</details>

<details><summary>Validated python files from users app</summary>

  ![PEP8 Validation](./README/tests/validation/python/users_context_processors.png)

</details>

### LightHouse

### User Stories Testing

### Bugs

*Go back to the [top](#super-pizza)*

## Deployment

## Credits

## Acknowledgements