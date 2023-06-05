
## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Structure](#structure)
      - [Database](#database)
      - [Wireframes](#wireframes)

### About

This glamping website provides a user-friendly platform to experience a unique camping destination in the beautiful Irish countryside. This site aims to be visually immersive, featuring a user-friendly booking system and showcasing customer testimonials through display of ratings and reviews.

<hr>

### User Goals
- Be able to check availibity and pricing information for desired dates 
- Easily book and secure preferred accomodation type for desired dates 
- Gain insight of expected experience by reading reviews and ratings from previous guests 
- Able to easily contact the site owner with any questions, queries, or special requests 


### Site Owner Goals
- Aim to attract and engage potentional customers with appealing visuals and user-friendly features
- Provide a seamless booking process to drive bookings and generate revenue to the camspite 
- Build trust and credibility of potentential guests by displaying campsite reviews, ratings and testimonials from previous customers 
- Offer a means of communication between customers and site owner to ensure satisfactory customer support experience 

<hr>


## User Experience

### Target Audience

- Outdoors enthusiasts who seek and appreciate experiences in natural settings 
- Couples on a romantic getaway looking for a intimate and scenic experience 
- Tourists looking for a distinct and memorable experience in the Irish countryside
- Individuals in search of a retreat where they can relax, unwind and become rejuvenated through the power of mindfulness in idyllic natural settings  


### User Requirements and Expectations
- Intuitive naviagtion and seamless booking process 
- Visually appealing design incorporating high-quality images to illustrate the expected glamping experience 
- Fully responsive and acessible across different screen sizes and devices 
- Secure authorisation 

##### Back to [top](#table-of-contents)<hr>

## User Stories

I utilitied the agile MoSCoW prioritisation method while planning the user stories for this project. This aided the created of a MVP from the beginning and lends itself to be of an iterative development style. 

### Users

#### MUST HAVE 

1. As a user, I want to easily navigate through the site to access all features and information about my possible stay.
3. As a user, I want to compare different accomodation types available 
6. As a user, I want to register for an account on the website 
7. As a returning user, I want to login to my account on the website 
8. As a user, I want to create a booking by selecting a date and accomodation-type for my stay
9. As a user, I want to review my booking so that I can remind myself of the date and accomadation type I have booked 
10. As a user, I want to update my booking so that I can choose another available time and/or accomodation type
11. As a user, I can delete my booking so that I can cancel my reservation for my stay 
13. As a user, I want to be able to logout of my account 

#### SHOULD HAVE 

2. As a user, I want to check the availability and pricing information for my desired dates
4. As a user, I want to see previous customer reviews and ratings of the different accomodation types
12. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed 
14. As a user, I would like to read reviews of only people that stayed in the accomodation


#### COULD HAVE 

5. As a user, I want a means of contacting the site owner with any questions, queries, or special requests 
As a user, i want to be able to see an interactive map of where the campsite is 


#### WON'T HAVE 

As a user i want to have real-time weather reports for days of my stay available when booking 

### Admin/Authorised User

#### MUST HAVE 

1. As an admin, I can log in and access the back end of the site
2. As an admin, I can manually add a booking so that I can accomodate bookings lodged through phone or email  

#### SHOULD HAVE 

3. As an admin, I can accept or reject bookings so that we avoid double bookings 
4. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day

#### COULD HAVE 

### Site Owner  

#### MUST HAVE 

As a site owner, I want the customers to have a means of communicating with me on website
As a site owner, I want site to be fully responisve and acessible 
As a site owner, i want all user entered data to be validated to reduce errors on database
As a site owner, I want only logged in users to view details of their bookings 


#### SHOULD HAVE 

#### COULD HAVE 

## Structure 

### Database

A number of models were created for this project 

#### User model
This contains:
- user_id: AutoField (PK)
- first_name: CharField()
- last_name: CharField()
- email: EmailField()
- password: CharField()
- is_superuser: BooleanField()

#### Accomodation model
This contains:
- accommodation_id: AutoField (PK)
- name: CharField()
- capacity: IntegerField()
- description: TextField()
- price_per_night: DecimalField()
- availibility: BooleanField() if available for booking dates

### Bookings model
This contains:
- booking_id: AutoField (PK)
- accommodation_id: ForeignKey
- user_id: ForeignKey
- check_in_date: DateField()
- check_out_date: DateField()
- length_of_stay: DurationField()
- num_guests: IntegerField()
- total_price: DecimalField()

### Testimonials model
This contains:
- testimonial_id: AutoField (PK)
- user_id: ForeignKey
- accommodation_id: ForeignKey
- rating: IntegerField()
- comment: TextField()
- date_created: DateField()
- image: ImageField(optional)

### Contact model
This contains: 
- contact_id: AutoField (PK)
- first_name: CharField()
- last_name: CharField()
- email: EmailField()
- text_body: TextField()

### Wireframes 


## Deployment (Heroku)

1. Login to heroku accound and navigate to the dashboard 
2. Click "New" on upper right hand side of screen 
3. In dropdown of "New" button, click first option "Create new app"
4. In "Create new app" screen, type in a unique name for your app and choose the region closest to you
*insert image here*
5. Click "Create app" 
6. You will be brought to deployment tab, from here naviagte to settings tab
7. Press "Reveal config vars" and add DATABASE_URL, SECRET_KEY and their values to KEY, VALUE fields
*insert image here*
8. Also add PORT, 8000 to KEY, VALUE fields in config vars to help with deployment 
9. Also add CLOUDINARY_URL and url of your API Environment variable to KEY, VALUE fields 
10. Add temporary DISABLE_COLLECTSTATIC, 1 KEY, VALUE pairs to allow skeleton project to run as project currenlty without statics fields (this will be removed at later stage)
11. In ALLOWED_HOSTS in settings.py file, type in project name url so project can run - in my case "glamping2023.herokuapp.com" 
12. Next you need to create a Procfile so heroku knows how to run the project - in my case add "web: gunicorn glamping.wsg" to file
13. In heroku, navigate to deploy tab of project and click github as deployment method 
14. Search for repository to connect github to heroku and press connect button beside correct repository
*insert image here*
14. Then scroll down to bottom of page and click on deploy branch (can clcik on build log to see deployment progress)
*insert image here*
15. Once build is finsihed, the build log will tell you 
*insert image here*
16. From here, press open app in top right hand of screen to see if deployment successful 
should open to this page if deployment succesful:
insert image here*

### Trouble-shooting
17. My first deploment was not successful 
*insert image here"
18. in the error message it said to check using "heroku logs --tail" butvi kept getting this message:
*insert message here*
19. I went to download the heroku cli because it was not already downleoaded in my ide 
*insert image here*
20. "curl https://cli-assets.heroku.com/install.sh | sh" - i used this command in my terminal as first command i used failed  ("brew tap heroku/brew && brew install heroku") because "heroku-node" failed to download
*insert image here*
21. i checked install by using this command "heroku --version", these are before and after images of the command working:
*insert images here*
22. heroku login but ip mismatch page displayed when tried to login 
*insert image here*
23. heroku login -i but *insert image here* but have to use api key found in accound setting to login rather than password, solution [slackoverflow] (https://stackoverflow.com/questions/68105084/not-able-login-to-heroku-account-from-command-line) 
24. finally try run "heroku logs --tail", i still get an error message 
*insert image here*
25. find solution on [slack overlow post] (https://stackoverflow.com/questions/51815542/heroku-missing-required-flag-a)
26. finally detailed application errors are display in terminal and I can look at wwhy my application is not deploying 
