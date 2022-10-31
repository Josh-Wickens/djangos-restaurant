# **Djangos Restaurant**

# [Click here to see deployed project](https://djangos-restaurant.herokuapp.com/) 

Djangos Restaurant is a full-stack framework project built using Django, Bootstrap, Python, HTML, CSS and Javascript. The website is built for the purpose of Djangos restaurant goers being able to access the website to see the menu and sign in to be able to book tables at the restaurant, read, edit and delete their bookings. 


![Responsive image of Djangos Restaurant website](https://res.cloudinary.com/wickster/image/upload/v1667150103/am_i_reponsive_hmau9x.png)

___

## **Strategy** ##
___
The target audience for Djangos Restaurant are:
- restaurant goers.
- 25 - 40 year olds.
- People with organised social lives.
- People who like to see the details of meals they have booked.
- People who have specific dietry requirements such as Vegetarians and Vegans.

### User Goals
- Navigate the website
- Set up a log in to register as a user.
- Make a reservation for a certain time and date at the restaurant.
- See all their reservations in an organised manner.
- Amend bookings that have been made by the user.
- Cancel bookings made by the user.

### Site Owners Goals
- Amend bookings through the admin if situations arise where the user can't (e.g. User calls the restaurant). 
- Edit the menu in the database.
- Search through bookings to organise how busy restaurant will be.


### requirements
- Easy navigation
- Minimal text to highlight features rather than reading.
- Easy to read, edit and delete bookings for user.
- Organised view of bookings

### Expectations
- When clicking on links, expect the page to open in a separate browser.
- All navigation links work.
- Once a booking has been made, I can see the details of that booking in a secure area.
- Bookings can't be made unless logged in.
- Only the logged in user can see their own bookings.


Djangos restaurant is suited towards these target audiences because the website provides the user with easy navigation, so that anyone who uses a computer should be able to navigate around the website. It also provides the user with an easy way to manage their bookings, where they can access the information simply and edit without difficulty. It also provides users with up to date menus so that they can plan easily. The age group is also suited towards customers who would like to use their phone in order to manage their booking. The website provides a site that is responsive to groups who would like to manage all this on their phones and on the go rather than only being able to book when setting time aside.
___
### User Stories - Agile Tools
You can see my user stories through the link below.
### [Click here to see my User Stories](https://github.com/users/Josh-Wickens/projects/2/views/1) 
![Image of User Stories](https://res.cloudinary.com/wickster/image/upload/v1667181416/agile_working_ss_of9c5t.png)

___
## **Scope** ##

The website will contain the folowing features:
- A navbar which will navigate the website from home page to pages which you can only access when signed in.
- A home page with a brief description of the restaurant and contains pictures.
- A menu page which contains an up to date menu which will be updated through a database.
- A booking page which will allow the user to make a reservation at the restaurant pending on availability.
- A manage booking page which will provide the user with a table of all their bookings which are due at the restaurant.
- A registration page for new users to register to the website so that they can make bookings.
- A login page for registered users to login so that they can make bookings or manage bookings which they have already made.
- A footer with contact details and location.  

## **Structure** ##
___

The website has been made with little text as to not deter the user away from what the main use of the website is for. The website has been made with the main functionality of a booking system rather than information regarding the website.

- Home page and menu for information
- Book Table to make bookings
- My Bookings to manage already made bookings.
___
## Surface

I chose a background that would be associated with a restaurant. The bright table with bread gives the website a restaurant/food kind of vibe. To go with the light background, a darker colour was chosen for text, navbar and footer so that they would stand out more on the background. Bootstraps dark class was selected for navbar and footer as this was perfect for the colour scheme I wanted. 
___
## Databases

There are 3 databases made from models. 

- Menu - This contains all the items on the food menu. This can be edited by the admin so that if a dish is taken off the menu then if they just remove from the database, this will then be removed from the website.

- Table - This contains all the customer tables in the restaurant. This can be managed by the admin so that if the amount of tables increases then they can add them to the database or alternatively reduce the amount of tables.

- Bookings - This contains all the bookings made by website users. This contains all the details of the bookings and can be managed by the admin to assign tables (from other database) to bookings. The User must be logged in to make a booking, so User is registered to the booking through the foreign key. The admin can also create bookings if customers have booked over the phone or by email.

see image below for Model planning. 

![Image of model planning](https://res.cloudinary.com/wickster/image/upload/v1667159239/models_vi0z5g.png)
___

## Wireframes

My wireframes was done using Justinmind. These are the pages and the original designs. They have since changed, but the simplification and limited text can be seen through the original wireframes.

### Nav Bar Pages
![Image of wireframe Navbar](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-1_b6lbj3.png)

### Log in
![Image of wireframe login page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-login_vngc75.png)



### Register
![Image of wireframe register page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-register_zyxn7l.png)




### Home
![Image of wireframe home page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-home_rtlncv.png)




### Menu
![Image of wireframe Menu page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-menu_vq4gxg.png)

### Book Table
![Image of wireframe Book Table page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-book_sn1xpa.png)

### My Bookings
![Image of wireframe my bookings page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-mybooking_vw1khe.png)

___
## **Features & CRUD** 

___

## Home Page

### Background Picture

- Background picture was selected to give the user an automatic feel that they were on a restaurant site as you can clearly identify the table with bread and plant on it. It also give the website a brighter and lighter look/feel to it for the user.

### Nav Bar
- The nav bar provides the user with a way of navigating the website. Identifying which pages are clickable is made clear to the user with the change of colour when hovered. The nav bar stays at the top of the website so that no matter which page they are on, it will always be the first element in view. Nav bar also contains the website logo which is also clickable to access the home page. The nav bar has also been given a darker colour so that it stands out over the lighter background so that users can easily identify where the nav bar is when entering any page. If the user isn't logged in, then the my bookings page will be replaced with a log in and register option in the nav bar. This prevents the user from accessing a blank my bookings page as bookings can only be made by users who are logged in. If the user is logged in, then the login and register pages are replaced by my bookings and log out navbar options.

![Image of nav bar](https://res.cloudinary.com/wickster/image/upload/v1667162614/navbar-ss_tzg6fi.png)

### Carousel

- The carousel provides the user with an instant look as to what Djangos Restaurant looks like. The carousel automatically switches between 3 images. The carousel has been given a golden border to make it stand out further to the user against the light background. 

### Description

- There is a small description/info on the home page so that the user can instantly find out what this website is for and who it is for. It provides anyone if they are already users, never been to the restaurant, google searchers etc. with information regarding djangos so that they can make an instant decision as to whether or not to carry on browsing the website.

### Footer

- The footer provides contact information to the site user. The contact number and email address can be found in the footer. The email address is clickable so that the user can instantly contact the restaurant by just clicking/pressing the email address. This makes it user friendly and prevents the user from making a mistake when entering the email address of the restaurant when writing an email. There is also a link to my github so that they can see who owns the copyright to the website and to direct website users who are looking for who created the website. Location details have also been stated on the footer so that all contact details are together in one place for the user.

![Image of footer](https://res.cloudinary.com/wickster/image/upload/v1667164049/footer_ss_g2evko.png)


## Menu Page

- The menu page has been populated through using an SQL database which stores the different dishes which are on the menu. The user can go on this page to find out what the restaurant has on the menu at the moment. The admin can update the menu whenever they want using the admin login. If a dish has run out or they no longer want to sell an unpopular dish then the admin can just delete that dish from the menu database and the website menu page will be updated. The menu page will only contain the menu and brief key to vegan and vegetarian choices. Keeping it to the point is part of my main goals of the website, so just having the menu on there is key to my design for the user.


![Image of menu](https://res.cloudinary.com/wickster/image/upload/v1667164220/menu_page_ss_pkl2g4.png)

## Book Table Page

- The book table page contains a form for the logged in user to be able to book a table at Djangos Restaurant. The form provides the user with a way to register names and contact numbers for the booking. As the table could be booked for business purposes etc. The user can decide what to name the booking rather than name it after the individual. Contact details for the booking are also needed for the user so that there is contact details provided to the restaurant in case anything is wrong with the booking. 07 is defaulted on the phonenumber field to give the user a hint to use a mobile number for contact details, but it is not limited to as a home number can also be used. A calendar widget has been introduced so that users can have a more user friendly way of selecting the date for the booking. The widget will produce a mini calander which will allow the user to see the days of the month and which days of the week they are. The check in time is also set to a choice option by the hour so that the user can choose the time instead of having to key it in using a keyboard where typing mistakes can be made. The book button will then figure out if the form is valid or not for saving, if the form is not valid, then it will provide the error to the user so that they can correct it. If the form is valid, then the book button will confirm the booking and redirect the user to the my bookings page so that they can then see that their booking is confirmed and in their bookings list. A message will also appear at the top to inform the user that their booking has been confirmed.

![Image of book a table page](https://res.cloudinary.com/wickster/image/upload/v1667166710/booktable_ss_f1wfdk.png)

## My Bookings Page

- The my booking page provides the user with an organised way of seeing their bookings. All bookings have been ordered in date order so that their earliest booking will be the 1st booking in the table so that they can prepare in order of booking dates. 
- Amend booking button has also been provided so that user can update or amend their booking. This provides the user a way of changing any details of their booking, if that be change of date, time, people etc. The amend button will redirect the user to the edit booking page and prepopulate the form with their current booking details so that the form is prefilled and they can just update the section they want to update rather than it all again, this is so that the amend form is more user friendly and provide a better experience for the user. If the user has successfully amended a booking, they will be redirected to the mybookings page where they can see the updated booking. A message will also appear at the top of the page to confirm their booking.
- The user also has the ability to delete/cancel their booking. If the user can no longer attend their booking, then they access their booking through the my bookings page and select the delete button. The button will at first open a model and ask the user if they are sure they want to delete the booking in case they had clicked on the button by accident and didn't want to loose their booking. 
- A function has been set in place so that any expired bookings would be deleted. Expired bookings would be set once the date of the booking has passed. This would save the user having to delete old bookings themselves whenever they have attended a booking. This will make their booking system more user friendly to stay on top of as well as manage.

![Image of my bookings page](https://res.cloudinary.com/wickster/image/upload/v1667167632/mybooking_ss_csmoy8.png)


![Image of are you sure you want to delete model](https://res.cloudinary.com/wickster/image/upload/v1667167632/cancel_model_z5kshm.png)

## Log in, out & Register Page

### Log in
- The log in page has been kept simple for the user to read. It provides a brief explanation as to why the user would like to log in (to be able to book tables and view their bookings). A username field and password field are the only inputs needed on the form to keep things simple and easy for the user to log in. If the the login credentials are incorrect, then a message will pop up on the form to inform the user that something is incorrect.

![Image of my login page](https://res.cloudinary.com/wickster/image/upload/v1667168488/login_ss_ampjqy.png)

- Log out give the user a chance to change their mind before logging out as this could have been a mistake. If they have logged out, then the user will be notified by a message.

- The register page has been kept simple for the user to register an account. They will only need to provide a username and password to create an account. Contact details are required for making bookings, so contact details are not needed at this point of interaction with the website. 

___
## Future Features

- Live chat with the restaurant to discuss details regarding bookings or logins etc.
- Seating plan so that customers using the booking system could also pick which table they would like to sit at based on location.
- Pre-order meals so that they can select what they want in advance and so that they can order items before they are taken off the menu.
- If multiple restaurants in the chain, then can select restaurant from location.
- An app so that Users could open an app to manage their bookings rather than have to go on the website.

___
## Technologies Used

### Languages & Frameworks
- HTML, CSS, JavaScript, Python - Languages used.
- Django - Framework used for project.
- Bootstrap - Used for design and responsive design.
- allauth - for restricted access.
- GitHub - Used to store project.
- Heroku - Used to deploy application.
- Cloudinary - To store images.
- PostgreSQL - To store model data.
- Justinmind - For wireframes and design.
- https://favicon.io/favicon-generator/ - For design of favicon

___

## Responsive Design

- I have changed the carousel on the homepage that once the screensize is below 600px that the carousel will be replaced with a static image as the carousel did not look as appealing on a smaller screen. 

- Bootstrap has been used to make divs responsive to smaller screen sizes.

- Bootstrap has been added to the table on my bookings so that a scrolling bar will be added once the screen size is smaller instead of squeezing the data. 

- The nav bar has been replaced with a drop down icon once screen size is smaller so that nav bar items aren't squished when using something like a phone device to access the website. This will make it more user friendly as the user can just open the drop down when they want to access another page on the website.

![Image of my responsive design navbar](https://res.cloudinary.com/wickster/image/upload/v1667170823/navbar_dropdown_lvylxe.png)


## Testing

I have used a combination of manual testing and automated testing. 

- Email link on homepage opens up an email app once clicked and prepopulates the email address.

- GitHub link in footer also opens on a new page when clicked.

- I have tried deleting, amending and adding items to the menu database. This in turn updates the webpage with the new or updated items.

- I have tested the booking form with multiple invalid entries. I have tested using an email without a @ sign. This throws an error and prevents the user from submitting the form.

- The restaurant holds 10 tables for reservations, I have tried testing to see if more than 10 bookings can be made for the same time and date. An error is raised if the amount of bookings is full for that date and time.

![Image of Restaurant full error](https://res.cloudinary.com/wickster/image/upload/v1667174129/full_ss_gp9cyo.png)


- I have tested trying to input a date that is in the past. This throws and error and informs the user that they cannot select a date in the past.

- I have tried to make a booking when not logged in. If the user isn't authenticated, then the form will be replaced with an option to login or register and inform the user they must be logged to make a booking. 

- I have tried leaving the name blank. This provides an error and prevents the form submitting.

- I have tested trying number of guests that is 0 or below and 5 or higher. This throws and error and inform the user that they need to submit a number between 1 and 4.

![Image of guest amount error](https://res.cloudinary.com/wickster/image/upload/v1667172158/guests_ss_yhyofg.png)

- I have logged in as another user and can't see or access anyone else's bookings.

- I have logged in as admin and tested that a user is linked to each individual booking. 

- I have passed my code through the W3C Markup Validation Service for HTML & W3C CSS Validation Service & Jshint for Javascript. All successfully passed with 0 errors.
___

## Epics

USER STORY - Set Up Home Page

- Testing has been done. The URL for the homepage works and the user can access the home page.

USER STORY: Create Menu Page

- Testing has been done and the URL for the menu page works, the user can access the page and view the information displayed on the page. The admin can edit the information on the menu by editing the database.

USER STORY: Set up Admin

- Admin has been set up as the superuser and can access and update information in the SQL database where the data for bookings, menu items, tables and users is stored.

USER STORY: Add Menu Dishes to Database

- Menu dishes have been added to the database by admin. This is now viewable to the user on the menu page and editable for the admin.

USER STORY: Register to Log in

- Registration page has been set up so that user can register for an account. The user can set up the username and password and create a user.

USER STORY: Log in

- Tests have been done to see that once registered if the user then uses those credentials that they can login. The login has been successful and a user can now log on to the website.

USER STORY: Book a Table

- Tests have been made to book a table. Form has been submitted and accessed the database through the admin and can see that the booking has been confirmed and is showing in the database.

USER STORY: Manage Booking Page

- The user once signed in can access the my bookings page and access the bookings that they have made previously. Testing has been done and the user can see only bookings that the user has made and nobody else's bookings.

USER STORY: Amend Booking

- The user can access their bookings from the my bookings page, click the amend button and change data from their previously booked reservations. Testing has been done and the original booking has been amended and a new one hasn't been made. This is confirmed by the booking reference number not changing.

USER STORY: Cancel Booking

- The user can cancel a booking that has previously been made. A model will pop up to confirm booking in case the cancel button has been selected accidentily. Testing has been done and once confirmed, the booking has been deleted from the database.

USER STORY: Create Authorization

- Pages which should only be accessible by users who are logged in have been hidden from non logged in users. This has been tested by logging out and trying to access the my bookings page (which should not be accessible unless logged in). When not logged in the user cannot make a booking or access the my bookings page.

___

## Bugs & Fixes

- When trying to do an if statement on my menu page. I had a bug which was preventing the if from checking the statement of checking if the vegan boolean was true or not. This was resolved by taking away the quotation marks as this was trying to imply the string True rather than the booleon value.

![Image of my bug on if statement for boolean field](https://res.cloudinary.com/wickster/image/upload/v1667174556/string_bug_v9hxvf.png)

- Trying to set the date field was having a problem with the date order and would often cause a valadation error as the date order would be incorrect. I resolved this bug by adding a calendar widget in the form.py instead so that the user could click the date rather than figure out the input.

- Had a bug where the form was supposed to figure out if the restaurant was full on a selected day and time. It was causing a bug to prevent the port from opening. I figured out that an error had been made that i was looking to see if the amount of bookings was the same as well as the same or more. I resolved it by getting rid of the ==. This meant it would now just check if it was the same or higher.

![Image of my bug on amount of bookings](https://res.cloudinary.com/wickster/image/upload/v1667175190/full_bug_qfmnsb.png)

- When trying to change a booking status to expired through python logic. I managed to change the status on the html for the user but this was not changing on the database. I added in some code that would change the status then save the new status on the database before adding the code to delete if status = expired.

- After some friends had tested my website. 2 of them said that when they registered that they received an error 500. I have ran extensive tests since then and could not reproduce the error. They said this happened when registering. I have tested this on desktop as well as mobile and still could not reproduce this error. All other users were able to register successfully. I have ran through this with Tutor Support and they also were able to register successfully. 

___


## Deployment

### Deploying to GitHub

- Using the Codeinstitute template - click the use this template button.
- create a repository name.
- click the create repository from template to create it.
- click GitPod button.
- to commit any change use: git add . to add files to staging area. git commit -m "commit message" commits changes to local repository. git push pushes commits to GitHub repository.

### Deploying to Heroku
- go to https://www.heroku.com/
- Create a new app and select a region.
- go to add ons to add Heroky Postgres.
- go to settings tab.
- In the Settings tab, click on Reveal Config Vars and set the following variables:
SECRET_KEY - to be set to your chosen key
CLOUDINARY_URL - to be set to your Cloudinary API environment variable.
- Connect your Heroku app to your GitHub Repository: click on depoy and select GitHub-Connect to GitHub. Search for GitHub Repository name, then connect.
- Then deploy branch by going to the deploy tab and scrolling down to the deploy branch button and clicking the button.
- once deployment is complete, you can then open app. 

### Everything was followed using the Code Institute deployment cheatsheet

[Django Deployment Cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

___

## Credits

### Websites

- https://stackoverflow.com/
- https://www.w3schools.com/
- https://django-filter.readthedocs.io/en/stable/guide/usage.html
- https://docs.djangoproject.com/
- TimeField choices - https://stackoverflow.com/questions/51164326/how-can-i-add-choices-to-a-timefield-in-a-django-form
- Responsive design tables in bootstrap - https://stackoverflow.com/questions/51164326/how-can-i-add-choices-to-a-timefield-in-a-django-form#
- Navbar & Footers with bootstrap - https://mdbootstrap.com/


### Font recomendation
https://inkbotdesign.com/font-combinations/ & https://www.fontpair.co/all

### All images are from Pexels.com 
https://www.pexels.com/photo/person-holding-bowl-2403392/

### Bootstrap Model is based from tutorialpublic.com 
https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=delete-confirmation-modal

### Bootstrap Carousel 
https://getbootstrap.com/docs/4.5/components/carousel/

### Youtube Help

Django Tutorials:

- https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj#
- https://www.youtube.com/playlist?list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT
- https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc



### GitHub Help

https://codeinstitute.net/student-projects/


### Tutor Support












