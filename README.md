# **Djangos Restaurant**

# [Click here to see deployed project](https://djangos-restaurant.herokuapp.com/) 

Djangos Restaurant is a full-stack framwork project built using Django, Python, HTML, CSS and Javascript. The website is built for the purpose of Djangos restaurant goers being able to access the website to see the menu and sign in to be able to book tabels at the restaurant, read and manage their bookings. 


![Responsive image of Djangos Restaurant website](https://res.cloudinary.com/wickster/image/upload/v1667150103/am_i_reponsive_hmau9x.png)

___

## **Strategy** ##
___
The target audience for Djangos Restaurant are:
- restaurant goers.
- 25 - 40 year olds.
- People with organised social lives.
- People who like to see the details of meals they have booked.
- People who have different dietry requirements such as Vegetarians and Vegans.

Djangos restaurant are suited towards these target audiences because the website provides the user with easy navigation, so that anyone who uses a computer should be able to navigate around the website. It also provides the user with an easy way to manage their bookings, where they can access the information simply and edit without difficulty. It also provides users with up to date menus so that they can plan easily. The age group is also suited towards customers who would like to use their phone in order to manage their booking. The website provides a site that is responsive to groups who would like to manage all this on their phones.
___
### User Stories
You can see my user stories through the link here.
### [Click here to see my User Stories](https://github.com/users/Josh-Wickens/projects/2/views/1) 
___
## **Scope** ##

The website will contain the folowing features:
- A navbar which will navigate the website from home page to pages which you can only access when signed in.
- A home page with a brief description of the restaurant and pictures.
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
## Databases

There are 3 databases made from models. 

- Menu - This contains all the items on the food menu. This can be edited by the admin so that if a dish is taken off the menu then if they just remove from the database, this will then be removed from the website.

- Table - This contains all the customer tables in the restaurant. This can be managed by the admin so that if the amount of tables increases then they can add them to the database or alternatively reduce the amount of tables.

- Bookings - This contains all the bookings made by website users. This contains all the details of the bookings and can be managed by the admin to assign tables (from other database) to bookings. The User must be logged in to make a booking, so User is registered to the booking through the foreign key.

![Image of model planning](https://res.cloudinary.com/wickster/image/upload/v1667159239/models_vi0z5g.png)
___

## Wireframes

My wireframes was done using Justinmind. These are the pages and the original designs. They have since changed, but the simplification and limited text can be seen through the original wireframes.

### nav bar pages
![Image of wireframe login page](https://res.cloudinary.com/wickster/image/upload/v1667160304/wireframe-1_b6lbj3.png)

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
- The nav bar provides the user with a way of navigating the website. Identifying which pages are clickable is made clear to the user with the change of colour when hovered. The nav bar stays at the top of the website so that no matter which page they are on, it will always be the first object in view. Nav bar also contains the website logo which is also clickable to access the home page. The nav bar has also been given a darker colour so that it stands out over the lighter background so that users can easily identify where the nav bar is when entering anypage. If the user isn't logged in, then the my bookings page will be replaced with a log in and register option in the nav bar. This prevents the user from accessing a blank my bookings page as bookings can only be made by users who are logged in. If the user is logged in, then the login and register pages are replaced by my bookings and log out navbar options.

![Image of nav bar](https://res.cloudinary.com/wickster/image/upload/v1667162614/navbar-ss_tzg6fi.png)

### Carousel

- The carousel provides the user with an instant look as to what Djangos Restaurant looks like. The carousel automatically switches between 3 images. The carousel has been given a golden border to make it stand out further to the user against the light background. 

### Description

- There is a small description/info on the home page so that the user can instantly find out what this website is for and who it is for. It provides anyone if they are already users, never been to the restaurant, google searchers etc. with information regarding djangos so that they can make an instant decision as to whether or not to carry on browsing the website.

### Footer

- The footer provides contact information to the site user. The contact number and email address can be found in the footer. The email address is clickable so that the user can instantly contact the restaurant by just clicking/pressing the email address. This makes it user friendly and prevents the user from making a mistake when entering the email address of the restaurant when writing an email. There is also a link to my github so that they can see who owns the copyright to the website and to direct website users who are looking for who created the website. Location details have also been stated on the footer so that all contact details are together in one place for the user.

![Image of nav bar](https://res.cloudinary.com/wickster/image/upload/v1667164049/footer_ss_g2evko.png)


## Menu Page

- The menu page has been filled through using a SQL database which stores the different dishes which are on the menu. The user can go on this page to find out what the restaurant has on the menu at the moment. The admin can update the menu whenever they want using the admin login. If a dish has run out or they no longer want to sell an unpopular dish then the admin can just delete that dish from the menu database and the website menu page will be updated. The menu page will only contain the menu and brief key to vegan and vegetarian choices. Keeping it to the point is part of my main goals of the website, so just having the menu on their is key to my design for the user.


![Image of menu](https://res.cloudinary.com/wickster/image/upload/v1667164220/menu_page_ss_pkl2g4.png)

## Book Table Page

- The book table page contains a form for the logged in user to be able to book a table at Djangos Restaurant. The form provides the user with a way to register names and contact numbers for the booking. As the table could be booked for business purposes etc. The user can decide what to the name the booking rather than name it after the individual. Contact details for the booking are also needed for the user so that there is contact details in case anything is wrong with the booking. 07 is defaulted on the phonenumber field to give the user a hint to use a mobile number for contact details, but it is not limited to as a home number can also be used. A calendar widget has been introduced so that users can have a more user friendly way of selecting the date for the booking. The widget will produce a mini calander which will allow the user to see the days of the month and which days of the week they are. The check in time is also set to a choice option by the hour so that the user can choose the time instead of having to key it in using a keyboard where typing mistakes can be made. The book button will then figure out if the form is valid or not for saving, if the form is not valid, then it will provide the error to the user so that they can correct it. If the form is valid, then the book button will confirm the booking and redirect the user to the my bookings page so that they can then see that their booking is confirmed and in their bookings list.

![Image of book a table page](https://res.cloudinary.com/wickster/image/upload/v1667166710/booktable_ss_f1wfdk.png)

## My Bookings Page

- The my booking page provides the user with an organised way of seeing their bookings. All bookings have been ordered in date order so that their earliest booking will be the 1st booking in the table so that they can prepare in order of booking dates. 
- Amend booking button has also been provided so that user can update or amend their booking. This provides the user a way of changing any details of their booking, if that be change of date, time, people etc. The amend button will redirect the user to the edit booking page and prepopulate the form with their current booking details so that the form is prefilled and they can just update the section they want to update rather than it all again, this is so that the amend form is more user friendly and provide a better experience for the user.
- The user also has the ability to delete/cancel their booking. If the user can no longer attend their booking, then they access their booking through the my bookings page and select the delete button. The button will at first open a model and ask the user if they are sure they want to delete the booking in case they had clicked on the button by accident and didn't want to loose their booking. 

![Image of my bookings page](https://res.cloudinary.com/wickster/image/upload/v1667167632/mybooking_ss_csmoy8.png)


![Image of are you sure you want to delete model](https://res.cloudinary.com/wickster/image/upload/v1667167632/cancel_model_z5kshm.png)

## Log in, out & Register Page

### Log in
- The log in page has been kept simple for the user to read. It provides a brief explanation as to why the user would like to log in (to be able to book tables and view their bookings). A username field and password field are the only inputs needed on the form to keep things simple and easy for the user to log in. If the the login credentials are incorrect, then a message will pop up on the form to inform the user that something is incorrect.

![Image of my bookings page](https://res.cloudinary.com/wickster/image/upload/v1667168488/login_ss_ampjqy.png)

- Log out give the user a chance to change their mind before logging out as this could have been a mistake. If they have logged out, then the user will be notified by a message.

- The register page has been kept simple for the user to register an account. They will only need to provide a username and password to create an account. Contact details are required for making bookings, so contact details are not needed at this point of interaction with the website. 







