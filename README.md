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

#### Auth

  - Workers have access to additional links, such as 'Orders,' allowing them to view and modify the status of active orders.

#### Pizza List Page

  - The Pizza List page has been tested on all screen sizes and the page is displayed correctly.
  - The pizza is filtered correctly by selecting the right criteria. Users can filter by multiple values.
  - Users also have the option to search for pizza by title or description.
  - The size buttons on the pizza card change the price of the pizza correctly.
  - Pizza is visually changing when size changes.
  - Add to Bag' button adds the pizza to your bag, and a message confirming the addition appears below the bag icon.
  - Clicking on the pizza image redirects to the details page for that specific pizza.

#### Pizza Details Page
  - The pizza details page displays correctly on screens of all sizes.
  - The pizza details page displays the correct pizza image, name, description, price.
  - The selected toppings under the pizza are visually highlighted and written in the pizza description, while the price is accurately updated.
  - A maximum of seven toppings can be selected.
  - The prices of both toppings and pizza change based on the selected size.
  - The price of the pizza increases accurately with each added topping.
  - The "Add to Bag" button adds the pizza to the bag and a message confirming the addition appears below the bag icon.

#### Bag Page

  - The bag page displays correctly on screens of all sizes.
  - The bag page displays the pizza cards that have been added to the bag.
  - If there are no items in the bag, only a button is displayed that redirects to the pizza page.
  - The card displays essential information such as the pizza name, extra toppings, pizza size, price, quantity, and pizza image.
  - Just above the pizza cards, it shows the number of items added to the bag, while next to the checkout button, it displays the grand total price, pizza price, and delivery cost.
  - The quantity of pizza can be changed by clicking the decrement or increment buttons, adjusting one pizza with each click. The price and quantity change accordingly.
  - Clicking on the 'remove' button removes the entire card, regardless of the number of pizzas, and the price is updated accordingly.
  - The "Checkout" button redirects to the checkout page.

#### Checkout Page
  - The checkout page displays correctly on screens of all sizes.
  - To place an order, users need to complete the form on the checkout page and make the payment by filling in their card details in the provided form.
  - If an incorrect value is entered into the payment field, it will be dynamically highlighted below the field.
  - After a successful payment, the user is redirected to the checkout success page.

#### Checkout Success Page
  - On the checkout success page, users receive details about the order, including the order number.
  - Additionally, there's a button that redirects to the order progress tracking page, showing the journey from order acceptance to delivery.

#### Tracking System

#### Profiles

#### Testimonials

#### About Page
  
  - The About page has been tested on all screen sizes and the page is displayed correctly.

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