
## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Theme](#theme)
      - [Wireframes](#wireframes)
    - [Structure](#structure)
      - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Bugs](#bugs)
  - [Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


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
2. As a user, I want to compare different accomodation types available 
3. As a user, I want to register for an account on the website 
4. As a returning user, I want to login to my account on the website 
5. As a user, I want to create a booking by selecting a date and accomodation-type for my stay
6. As a user, I want to review my booking so that I can remind myself of the date and accomadation type I have booked 
7. As a user, I want to update my booking so that I can choose another available time and/or accomodation type
8. As a user, I can delete my booking so that I can cancel my reservation for my stay 
9. As a user, I want to be able to logout of my account 

#### SHOULD HAVE 

10. As a user, I want to check the availability and pricing information for my desired dates
11. As a user, I want to see previous customer reviews and ratings of the different accomodation types
12. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed 
13. As a user, I would like to read reviews of only people that stayed in the accomodation


#### COULD HAVE 

14. As a user, I want a means of contacting the site owner with any questions, queries, or special requests 
15. As a user, i want to be able to see an interactive map of where the campsite is 


#### WON'T HAVE 

16. As a user i want to have real-time weather reports for days of my stay available when booking 

### Admin/Site Owner

#### MUST HAVE 

17. As an admin, I can log in and access the back end of the site
18. As an admin, I can manually add a booking so that I can accomodate bookings lodged through phone or email  
19. As a site owner, I want the customers to have a means of communicating with me on website
20. As a site owner, I want site to be fully responisve and acessible 
21. As a site owner, i want all user entered data to be validated to reduce errors on database
22. As a site owner, I want only logged in users to view details of their bookings 

#### SHOULD HAVE 

23. As an admin, I can accept or reject bookings so that we avoid double bookings 
24. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day

#### COULD HAVE 
25. As a site owner, 

## Design

### Theme

A [bootstrap template Yummy](https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/) was used for this project. I also utitilised another [bootstrap template Admin](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/) for the login/logout and forms of the site. Iadapted and pulled aspects of the code for the website and changed CSS elements to better represent my vision for the glamping wesbite.

### Colour 

I enjoyed the primary colours from the Yummy bootstrap theme (as mentioned above) and hence only changed the colours slightly from the original. I opted to replace the primary red color with a magenta pink shade that complemented the visuals of my pictures. This subtle adjustment helped unify the elements of my website, creating a cohesive and visually appealing experience for visitors.

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687450655/glamping/docs/colours_website.png" alt="colours of wesbite">

### Wireframes 

<img src="" alt ="">
<img src="" alt ="">
<img src="" alt ="">
<img src="" alt ="">
<img src="" alt ="">

## Structure 

The wesbite consists of number of pages. The mains pages as seen on the navigation bar are:
- Home 
- Accomodation
- Testimonials 
- Log in /Register /Log Out
- Contact 
- Book 
- View Bookings 

### Database

A number of models were created for this project 

#### User model (allauth)
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
- content: TextField()
- date_created: DateField()
- image: ImageField(optional)
- likes: user model

### Contact model
This contains: 
- contact_id: AutoField (PK)
- first_name: CharField()
- last_name: CharField()
- email: EmailField()
- text_body: TextField()

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Summernote](https://summernote.org/)


##### Back to [top](#table-of-contents)

## Validation

### HTML - [Validator](https://validator.w3.org/)

### CSS - [Jigsaw](https://jigsaw.w3.org/css-validator/)

### Javascript - [JSHint](https://jshint.com/)

### Python - [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)

### Accessibility - [WAVE](https://wave.webaim.org/report)

### Performance - Lighthouse


## Testing

### Manually testing user stories 


1. As a user, I want to easily navigate through the site to access all features and information about my possible stay.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

2. As a user, I want to compare different accomodation types available 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

3. As a user, I want to register for an account on the website 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

4. As a returning user, I want to login to my account on the website 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

5. As a user, I want to create a booking by selecting a date and accomodation-type for my stay

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

6. As a user, I want to review my booking so that I can remind myself of the date and accomadation type I have booked 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details> 

7. As a user, I want to update my booking so that I can choose another available time and/or accomodation type

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

8. As a user, I can delete my booking so that I can cancel my reservation for my stay 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

9. As a user, I want to be able to logout of my account 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

10. As a user, I want to check the availability and pricing information for my desired dates

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

11. As a user, I want to see previous customer reviews and ratings of the different accomodation types

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

12. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

13. As a user, I would like to read reviews of only people that stayed in the accomodation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>


14. As a user, I want a means of contacting the site owner with any questions, queries, or special requests 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

15. As a user, i want to be able to see an interactive map of where the campsite is 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>




17. As an admin, I can log in and access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

18. As an admin, I can manually add a booking so that I can accomodate bookings lodged through phone or email  

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

19. As a site owner, I want the customers to have a means of communicating with me on website

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

20. As a site owner, I want site to be fully responisve and acessible 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

21. As a site owner, i want all user entered data to be validated to reduce errors on database

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

22. As a site owner, I want only logged in users to view details of their bookings 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

23. As an admin, I can accept or reject bookings so that we avoid double bookings 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>

24. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |


<details><summary>Screenshot</summary>
<img src="">
</details>


## Bugs


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


### Credits 

#### Photos


- [Accomodations images courtesy of Podumna Glamping Village](https://podumnavillage.ie/)
- Photo by <a href="https://unsplash.com/@captainhouque?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alex Houque</a> on <a href="https://unsplash.com/photos/Twke63oNYM0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>Hero image on home page
- Photo by <a href="https://unsplash.com/@ashleighjoyphotography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ashleigh Joy Photography</a> on <a href="https://unsplash.com/photos/BdEgT847nk0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>: Photo of boaton create bookings page
  
#### Code 
StackOverflow:
- [adding max and min validators to rating on rating field](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- [adding success message to deleteview class](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)

Django Documentation:
- [the use of CreateView, UpdateView and DeleteView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
- [adding flash success messages to class based view](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)
