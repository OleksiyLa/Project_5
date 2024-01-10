# Super Pizza

Superpizza, our online delivery store in Tralee, offers a seamless user experience, designed for easy navigation. Customers can explore our diverse range of pizzas, select their preferred size, and personalize it by adding extra toppings. They also have the convenience of leaving testimonials to share their experiences.

Our platform includes a secure online payment system and provides an option to track order status from the moment an order is placed until it reaches your doorstep. The intuitive design extends to our workers and administrators, granting them the ability to efficiently manage orders, approve or remove testimonials, and effortlessly modify the store's products such as pizzas and toppings.

![Pizza menu page](./README/website/pizza_list_page.png)

<br>

## Planning & Development

### Target Audience

  - Busy Professionals: Individuals who lack time to cook and prefer the convenience of ordering food online.
  - Families: Parents looking for quick meal solutions or a treat for their children without leaving home.
  - Students: Those living on campus or in nearby areas who enjoy the ease of online ordering for gatherings or individual meals.
  - Food Enthusiasts: People who appreciate customization and quality ingredients in their pizzas.
  - Tech-Savvy Users: Those comfortable with online platforms and seeking a streamlined, user-friendly ordering experience.
  - Local Community Members: Individuals supporting local businesses and seeking easy access to delicious, freshly made pizzas in their area.

### App Objectives

  - User Convenience: Simplify the pizza ordering process for customers, ensuring a seamless and user-friendly interface.
  - Customization: Allow customers to personalize their orders by choosing pizza size, toppings.
  - Efficient Order Management: Enable workers and administrators to efficiently manage orders, ensuring timely processing and delivery.
  - Enhanced Customer Experience: Provide a platform for customers to leave testimonials and feedback, fostering a sense of engagement and trust.
  - Secure Payment Processing: Implement a reliable and secure online payment system to facilitate smooth transactions.
  - Order Tracking: Offer customers the ability to track their orders from placement to delivery, enhancing transparency and reliability.
  - Scalability: Build a platform that can adapt and scale with the growing business needs, accommodating potential expansions or modifications to the menu or services.
  - Marketing and Analytics: Incorporate features to gather data on customer preferences and behavior, aiding in targeted marketing efforts and service improvements.

### Features to Implement

  - Convenient Real-Time Tracking System: Allow users to track their orders in real-time, providing updates from acceptance to delivery stages.
  - Order Management for Workers: A dashboard for workers to view all active new orders and update their status from 'new' to 'done' upon completion.
  - Online Payment System: Integrate a secure online payment gateway for seamless transactions within the app.
  - Registration and Login: Enable users to create accounts and log in to access personalized features and order history.
  - Pizza List Page with Filters: Present a comprehensive list of available pizzas with filter options for easy browsing.
  - Pizza Details and Customization: Offer a detailed view of each pizza with customization options, including the ability to change size, add extra toppings.
  - Add to Bag Functionality: Allow users to add selected items to their shopping bag for a streamlined ordering process.
  - Profile Page for Registered Users: Provide a dedicated space for registered users to manage their information and view past orders.
  - Testimonials Submission: Enable customers to write testimonials to share their experiences with Superpizza.
  - Testimonials Management for Admins: Admins can review, approve and delete testimonials submitted by customers to maintain the integrity of displayed reviews.
  - Store Product Management for Admins: Grant admins the capability to manage products in the store, including adding, editing, or deleting pizzas and toppings from the menu.
  - Responsive Design: Ensure the app is responsive across various devices and screen sizes.

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

  - Verified admin privileges within the admin panel, including editing/deleting products and testimonials.
  - Ensured that under product cards (e.g., pizzas, toppings), admins can access links to edit or delete them.
  - Verified admin access to approving or deleting testimonials.

#### Form Validation

  - Validated Add Pizza form.

![Add Pizza form](./README/tests/manual_testing/forms/add_pizza.png)

  - Validated Edit Pizza form.

![Edit Pizza form](./README/tests/manual_testing/forms/edit_pizza.png)

  - Validated Add Topping form.

![Add Topping form](./README/tests/manual_testing/forms/add_topping.png)

  - Validated Edit Topping form.

![Edit Topping form](./README/tests/manual_testing/forms/edit_topping.png)

  - Validated Login form.

![Login](./README/tests/manual_testing/forms/login.png)

  - Validated Registration form.

![Registration](./README/tests/manual_testing/forms/register.png)

  - Validated Profile form.

![Profile form](./README/tests/manual_testing/forms/profile.png)

  - Validated Checkout form.

![Checkout form](./README/tests/manual_testing/forms/checkout.png)

  - Validated Provide Testimonial form.

![Provide Testimonial form](./README/tests/manual_testing/forms/testimonial.png)

  - Validated Track Order form.

![Track Order form](./README/tests/manual_testing/forms/order_tracker.png)

#### Crud

  - Verified that admins can successfully add new pizzas and toppings to the system.

![CRUD](./README/tests/manual_testing/crud/added_pizza.png)
![CRUD](./README/tests/manual_testing/crud/added_pizza_pickles.png)

  - Verified that admins can successfully update pizza or topping.

![CRUD](./README/tests/manual_testing/crud/edit_pickles.png)

  - Verified that admins can successfully delete pizza or topping.

![CRUD](./README/tests/manual_testing/crud/delete_from_pizza_list.png)
![CRUD](./README/tests/manual_testing/crud/delete_toppping.png)

  - Confirmed that images associated with pizzas or toppings created and deleted in Cloudinary.
  - Ensured the ability for users to create testimonials and submit them successfully.
  - Validated admin functionality to approve submitted testimonials.

![CRUD](./README/tests/manual_testing/crud/testimonial_to_approve.png)
![CRUD](./README/tests/manual_testing/crud/testimonial_approved.png)

  - Confirmed that admins can delete testimonials as needed.

![CRUD](./README/tests/manual_testing/crud/testimonial_delete_modal.png)

  - Verified that users can add pizzas to their shopping bag successfully.

![CRUD](./README/tests/manual_testing/crud/added_to_bag.png)

  - Tested the removal of pizzas from the bag to ensure functionality.

![CRUD](./README/tests/manual_testing/crud/updated_bag.png)

  - Confirmed that users can modify the quantity of pizzas in their bag and that these changes reflect accurately.

![CRUD](./README/tests/manual_testing/crud/removed_bag.png)

  - Validated the ability for users to add toppings to their pizzas.

#### Price

  - Confirmed that the price of a pizza changes correctly based on the selected size (30cm, 35cm, 40cm).

![Price](./README/tests/manual_testing/price/pizza_small.png)
![Price](./README/tests/manual_testing/price/pizza_large.png)

  - Validated that the price of extra toppings adjusts according to the size of the pizza.

![Price](./README/tests/manual_testing/price/toppings_price_small.png)
![Price](./README/tests/manual_testing/price/toppings_price_large.png)

  - Verified that adding extra toppings increases the pizza's price by the respective cost of each topping.

![Price](./README/tests/manual_testing/price/pizza_large_toppings.png)

  - Ensured that the delivery cost is correctly applied or omitted based on the total price of pizzas in the order.

![Price](./README/tests/manual_testing/price/pizza_1.png)

  - Confirmed that the grand total price changes accurately based on the quantity of pizzas added to the shopping bag.

![Price](./README/tests/manual_testing/price/pizza_5.png)

  - Checked that all applicable adjustments (size, toppings, delivery cost) reflect in the final calculated total.

![Price](./README/tests/manual_testing/price/total_deliverycost.png)

#### Payment

  - Verified that items added to the shopping bag correctly transfer to the checkout page.
  - Ensured the displayed prices in the checkout match those in the shopping bag.
  - Validated the input of card details for payment.
  - Confirmed that the price taken during the payment process matches the total displayed during checkout.

![Payment](./README/tests/manual_testing/payment/checkout.png)

  - Validated successful payment events in the Stripe dashboard.

![Payment](./README/tests/manual_testing/payment/events.png)

  - Tested and verified webhook functionality to ensure it works as expected.

![Payment](./README/tests/manual_testing/payment/webhooks.png)

  - Checked that users receive an order confirmation email after successful payment and completion of the checkout process.

![Payment](./README/tests/manual_testing/payment/email.png)

  - Confirmed that users are redirected to a "Checkout Success" page after completing the payment. Validated that this page displays relevant order details such as items purchased, total cost, and delivery information.

![Payment](./README/tests/manual_testing/payment/success.png)

#### Profiles
  - Ensured that the details entered in the profile form are pre-filled in the checkout form for user convenience.

![Profiles](./README/tests/manual_testing/profile/order_history.png)
![Profiles](./README/tests/manual_testing/profile/checkout.png)

  - Confirmed that the orders in the profile are displayed in chronological order, with the most recent order at the top.
  - Tested the functionality to view detailed information for each order upon clicking.

![Profiles](./README/tests/manual_testing/profile/details.png)

  - Verified that for active orders, a track order button is displayed within the order details.
  - Ensured the functionality of the track order button to provide real-time status updates for the user.

#### Tracking System

  - Confirmed that when a customer purchases a pizza, an active order is created for tracking purposes.
  - Tested the functionality to display the order's status progression (pending, accepted, cooking, preparing, delivering, delivered) on the customer's screen via a progress bar.
  - Ensured that status changes made by workers or admins are instantly reflected on the customer's progress bar interface.
  - Verified that workers or admins can view new orders as they are created.
  - Tested the functionality for workers or admins to change the order status (e.g., from accepted to cooking, preparing, delivering).
  - Ensured that order status changes can only progress sequentially from one stage to the next until reaching the "Done" status.
  - Validated the functionality of the "Archive" button for completed orders, making them inactive and invisible to both workers and customers.

<details><summary>Tracking System</summary>

  ![Tracking](./README/tests/manual_testing/tracking/pending.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_new_full.png)
  ![Tracking](./README/tests/manual_testing/tracking/accepted.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_verified.png)
  ![Tracking](./README/tests/manual_testing/tracking/cooking.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_cooking.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_preparing.png)
  ![Tracking](./README/tests/manual_testing/tracking/preparing.png)
  ![Tracking](./README/tests/manual_testing/tracking/delivery.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_delivering.png)
  ![Tracking](./README/tests/manual_testing/tracking/delivered.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_done.png)
  ![Tracking](./README/tests/manual_testing/tracking/order_archived.png)
  ![Tracking](./README/tests/manual_testing/tracking/not_found.png)

</details>

#### Responsiveness

  - Verified the website's responsiveness on different screen sizes (e.g., mobile, tablet, desktop).
  - Confirmed that content layout and elements adjust appropriately to fit various screen resolutions.
  - Checked the readability of text, clarity of images, and accessibility of navigation menus on all screen sizes.
  - Ensured that buttons, links, and interactive elements are easily clickable and usable across different devices.
  - Validated that the design maintains visual consistency and integrity across all screen sizes.
  - Confirmed that images, fonts, and overall aesthetics are consistent and appealing irrespective of the screen dimensions.

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