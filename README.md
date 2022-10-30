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
- Bookings - This contains all the bookings made by website users. This contains all the details of the bookings and can be managed by the admin to assign tables (from other database) to bookings.
