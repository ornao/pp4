
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
- Be able to check availibility and pricing information for desired dates 
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

My user stories were catagorized into epics and sub-divided into individuals tasks; details of which can be found on my [kanban board](https://github.com/users/ornao/projects/5). User stories were also ranked using MoSCoW prioritisation and were each given a sprint which gave me a timeframe to complete the majority of the tasks outlined in the user story. I did not sumbit speciific dates for each sprint as this was my first time undertaking a project like and I was unsure how long individual tasks would take me to complete. Hence, I included must have for an MVP in my first sprint and cataegorised the rest of te user stories accordingly in later sprints.

### Users

#### MUST HAVE 

1. As a user, I want to easily navigate through the site to access all features and information about my possible stay.
2. As a user, I want to compare different accomodation types available so that I can make an informed decision of which accomodation best suits my needs. 
3. As a user, I want to register for an account on the website so I can access restricted user areas of wesbite i.e viewing my bookings 
4. As a returning user, I want to easily login to my account on the website to view my bookings and access full site functionality
5. As a user, I want to create a booking by selecting a date and accomodation-type for my stay
6. As a user, I want to review my booking so that I can remind myself of the date and accomadation type I have booked 
7. As a user, I want to update my booking so that I can choose another available time and/or accomodation type. My previous details should be present on this form so I know what I am changing details from. 
8. As a user, I can delete my booking so that I can cancel my reservation for my stay 
9. As a user, I want to be able to easily logout of my account so that my bookings are secure once again
10. As a user, I want a confirm delete page to display so i do not accidently click delete booking by accident.
11. As a first time user, I should immediatley understand the purpose of the website from the home page so my time is not wasted 
12. As an unregistered user, I have access to accomodation types, reviews and ratings information so I can make an informed decision on whether I should make an account to book a stay. 
13. As a user, i want to my bookings information to be secure so no other users have access to it. 

#### SHOULD HAVE 

14. As a user, I want to check the availability and pricing information for my desired dates
15. As a user, I want to see previous customer reviews and ratings of the different accomodation types
16. As a user I can view the lastest testimonials first when I click on testimonials so that I can directly access the most up-to-date reviews available on the website.
17. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed 
18.. As a user, I would like to read reviews of only people that stayed in the accomodation
18. As a user I have access to contact information so I can contact the site owners with any questions, queries, or special requests. Future development will include a form whereby customers can contact owners directly from site rather than having to email, phone separately. 
19. As a registered user I want to be able to be notified if I do something wrong while complete a booking form before I submit it so there are no complications with my booked stay. 
20. As a user, an error page will display with a navigation link back home that tells me something has gone wrong with website but I have a way back to the website.



#### COULD HAVE 

21. As a user, i want to be able to see an interactive map of where the campsite is 
22. As a registered user, I can reset my password so that I can regain access to my account if I forget my password.
23. As a user, I can signup to the site using one of my social media accounts to allow for an even more seemless registration.
24. As a logged in user, I can like people's reviews so that I can show i agree with their comments aboyt their stay. 

#### WON'T HAVE 

25. As a registered user, I can be contacted directly by site owners on wesbite ad receive replies and noticications of these relies through the wesbite through messaging services.
26. As a user i want to have real-time weather reports for days of my stay available when booking 

### Admin/Site Owner

#### MUST HAVE 

27. As an admin, I can log in and access the back end of the site
28. As an admin, I can manually add a booking so that I can accomodate bookings lodged through phone or email  
29. As an admin, I can accept or reject bookings so that we avoid double bookings 
30. As a site owner, I want site to be fully responisve and acessible 
31. As a site owner, i want all user entered data to be validated to reduce errors on database
32. As a site owner, I want only logged in users to view details of their bookings 
33. As a site owner, I want every site visitor to be able to view the accomodation types no offer and reviews of these accomodations
 
#### SHOULD HAVE 

34. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day
35. As a site owner, I want the customers to have a means of communicating with me on website to inform me of their experinece of site vs any queries about their future stay



## Design

### Theme

A [bootstrap template Yummy](https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/) was used for this project. I also utitilised another [bootstrap template Admin](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/) for the login/logout and forms of the site. Iadapted and pulled aspects of the code for the website and changed CSS elements to better represent my vision for the glamping wesbite.

### Colour 

I enjoyed the primary colours from the Yummy bootstrap theme (as mentioned above) and hence only changed the colours slightly from the original. I opted to replace the primary red color with a magenta pink shade that complemented the visuals of my pictures. This subtle adjustment helped unify the elements of my website, creating a cohesive and visually appealing experience for visitors.

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687450655/glamping/docs/colours_website.png" alt="colours of wesbite">

### Wireframes 

Included are the screenshots created prior to development. As you can see, the finished wesbite looks slighly different but the core fucntion of each page remains the same. 

<details><summary> Home page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/home_page_wireframe_mzjg9q.png" alt="home page wireframe">
</details>

<details><summary> Accommodation page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950338/glamping/docs/accommodation_page_wireframe_mrzg1a.png" alt="accomodation page wireframe">
</details>

<details><summary> Testimonials page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950339/glamping/docs/testimonials_page_wireframes_svu8rr.png" alt="testimonials page wireframe">
</details>

<details><summary> Create bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/book_page_wireframes_uh0brr.png" alt="create booking page wireframe">
</details>

<details><summary> View bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687951678/glamping/docs/viewbookings_page_wireframes_c0rdr2.png" alt="view booking page wireframe">
</details>

<details><summary> Edit bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950683/glamping/docs/editingbooking_page_wireframes_dm6bv4.png" alt="edit booking page wireframe">
</details>

<details><summary> Delete bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950684/glamping/docs/deletebooking_page_wireframes_ve5j4m.png" alt="delete booking page wireframe">
</details>

<details><summary> Login page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/login_page_wireframes_yk9ayf.png" alt="login page wireframe">
</details>

<details><summary> Signup page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950338/glamping/docs/signup_page_wireframes_yhbpqg.png" alt="signup page wireframe">
</details>

<details><summary> Logout page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/logout_page_wireframes_iiey7o.png" alt="logout page wireframe">
</details>

<details><summary> Error page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687952095/glamping/docs/error_page_wireframes_koxnjy.png" alt="error page wireframe">
</details>

<details><summary> Contact page screenshot</summary>
- While i did not complete a contact page as part of this project, it is something I aim to achieve in future iterations of the project. 
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687952831/glamping/docs/contact_page_wireframes_ab8awm.png" alt="contact page wireframe">
</details>


## Structure 

The wesbite consists of number of pages. The mains pages as seen on the navigation bar are:

- Home 
<details><summary> Home page screenshot</summary>

<img src="" alt="home page">
</details>

- Accomodation
<details><summary> Accomodation page screenshot</summary>

<img src="" alt="accommodation page">
</details>

- Testimonials 
<details><summary> Testimonials page screenshot</summary>

<img src="" alt="testimonials page">
</details>

- Log in /Register /Log Out
<details><summary> Log in /Register /Log Out page screenshots</summary>

<img src="" alt="login page">

<img src="" alt="signup page">

<img src="" alt="logout page">
</details>


- Book 
<details><summary> Book page screenshot</summary>

<img src="" alt="book page">
</details>

User need to Log In to view these page: 
- View Bookings 
<details><summary> View bookings page screenshot</summary>

<img src="" alt="book page">
</details>
- Edit Bookings 
<details><summary> Edit bookings page screenshot</summary>

<img src="" alt="edit bookings page">
</details>
- Delete Bookings
<details><summary> Delete bookings page screenshot</summary>

<img src="" alt="edit bookings page">
</details>

### Database

3 custom models were created for this project - accomodation, bookings and testimonials. My bookings model supports full CRUD functionality while accomodation and tesimonials currently only pull from database. User model was provided for by django allauth. In future iterations, I would like to create an availbility model to allow user to check if their desired accomodation is available for their desired dates. I would also like to include a contact model in future development so users have ability to directly contact site owner on site without having to ring or email seperately. I would also like to add more CRUD functionality to testimonials model so users can submit their own testimonials. 

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

<details><summary> Database schema screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687959226/glamping/docs/database_schema_rfiwao.png" alt="database schema scrennshot">
</details>

### Future models 

#### Contact model

This will contain:
- contact_form_id: AutoField (PK)
- user_id: ForeignKey
- first_name: CharField()
- last_name: CharField()
- email: EmailField()
- booking_id: ForeignKey (optional)
- content: TextField()
- date_submitted: DateField()
- image: ImageField(optional)

#### Availability model
NEED TO CHECK!!!!
This will contain:
- accommodation_name: ForeignKey
- check_in_date: ForeignKey
- check_out_date: ForeignKey
- available?
- length_of_stay: DurationField()
- num_guests: IntegerField()
- total_price: DecimalField(price_per_night x length_of_stay)

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
- [dbdiagram](https://dbdiagram.io/home)
- [Fake Irish number generator](https://fakenumber.org/ireland)
- [Irish dictonary](https://www.focloir.ie/) - to check spelling for fake address I made up 


##### Back to [top](#table-of-contents)

## Validation

### HTML - [Validator](https://validator.w3.org/)

The W3S HTML validator checks the HTML through the webpage url. This is because the validator does not recognise the django template language when HTML input directly into validator. 


<details><summary> Home page screenshot</summary>
- This checks base.html and index.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889359/glamping/docs/home_html_validator_cl0mu2.png" alt="home page html validation check">
</details>

<details><summary> Accommodation page screenshot</summary>
- This checks base.html and accomodation.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889261/glamping/docs/accomodation_html_validator_cayv4c.png" alt="accomodation page html validation check">
</details>

<details><summary> Testimonials page screenshot</summary>
- This checks base.html and testimonials.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889276/glamping/docs/testimonials_html_validator_p98e6o.png" alt="testimonials page html validation check">
</details>

<details><summary> Log In page screenshot</summary>
- This checks base.html and account/login.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902571/glamping/docs/login_html_validator_prlam4.png" alt="login page html validation check">
</details>

<details><summary> Register page screenshot</summary>
- This checks base.html and accounts/signup.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902571/glamping/docs/signup_html_validator_m4ctuw.png" alt="signup page html validation check">
</details>

<details><summary> Log Out page screenshot</summary>
- This checks base.html and account/logout.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902920/glamping/docs/logout_html_validator_bgc04l.png" alt="logout page html validation check">
</details>


<details><summary> View your Bookings page screenshot</summary>
- This checks base.html and read_bookings.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/read_bookings_html_validator_bfzmpe.png" alt="view bookings page html validation check">
</details>

<details><summary> Book page screenshot</summary>
- This checks base.html and create_bookings.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/create_bookings_html_validator_xvsnqd.png" alt="book page html validation check">
</details>

<details><summary> Edit Bookings page screenshot</summary>
- This checks base.html and edit_bookings.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/edit_bookings_html_validator_cnekpe.png" alt="edit bookings page html validation check">
</details>

<details><summary> Delete Bookings page screenshot</summary>
- This checks base.html and confirm_delete.html
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/delete_bookings_html_validator_asg3f5.png" alt="confirm delete page html validation check">
</details>

### CSS - [Jigsaw](https://jigsaw.w3.org/css-validator/)

### Javascript - [JSHint](https://jshint.com/)

### Python - [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)

### Accessibility - [WAVE](https://wave.webaim.org/report)

<details><summary> Home page screenshot</summary>
<img src="" alt="home page accessibility check">
</details>

<details><summary> Accommodation page screenshot</summary>
<img src="" alt="accomodation page accessibility check">
</details>

<details><summary> Testimonials page screenshot</summary>
<img src="" alt="testimonials page accessibility check">
</details>

<details><summary> Log In page screenshot</summary>
<img src="" alt="login page accessibility check">
</details>

<details><summary> Register page screenshot</summary>
<img src="" alt="signup page accessibility check">
</details>

<details><summary> Log Out page screenshot</summary>
<img src="" alt="logout page accessibility check">
</details>


<details><summary> View your Bookings page screenshot</summary>
<img src="" alt="view bookings page accessibility check">
</details>

<details><summary> Book page screenshot</summary>
<img src="" alt="create bookings page accessibility check">
</details>

<details><summary> Edit Bookings page screenshot</summary>
<img src="" alt="edit bookings page accessibility check">
</details>

<details><summary> Delete Bookings page screenshot</summary>
<img src="" alt="delete bookings page accessibility check">
</details>

### Performance - Lighthouse


## Testing

### Manually testing user stories 

1. As a user, I want to easily navigate through the site to access all features and information about my possible stay.

LOGGED OUT USER: 
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Home' tab in the nav bar | Home page will display | Works as expected |
Click on the 'Accommodation' tab in the nav bar | Accomodation page will display | Works as expected |
Click on the 'Testimonials' tab in the nav bar | Testimonials page will display | Works as expected |
Click on the 'Log In' tab in the nav bar | Log In page will display | Works as expected |
Click on the 'Register' tab in the nav bar | Home page will display | Works as expected |
Click on the 'Book' tab in the nav bar | Create bookings page will display | Works as expected |


<details><summary> Home navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246507/glamping/docs/user%20stories%20testing/home_nav_testing_s90nba.png" alt="home navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688245101/glamping/docs/user%20stories%20testing/home_nav_display_deel3j.png" alt="home navigation testing display">
</details>

<details><summary> Accomodation navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246030/glamping/docs/user%20stories%20testing/accomodation_nav_testing_dne3kd.png" alt="accomodation navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/accomodation_nav_display_bh5hxa.png" alt="accomodation navigation testing display">
</details>

<details><summary> Testimonials navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246026/glamping/docs/user%20stories%20testing/testimonials_nav_testing_f6ho2m.png" alt="testimonials navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/testimonials_nav_display_px3rvj.png" alt="testimonails navigation testing display">
</details>

<details><summary> Log In navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246021/glamping/docs/user%20stories%20testing/login_nav_testing1_ddqnoy.png" alt="log In navigation testing1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688247605/glamping/docs/user%20stories%20testing/login_nav_testing2_vz1gqb.png" alt="log In navigation testing2">
<img src="" alt="log In navigation testing3">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688244998/glamping/docs/user%20stories%20testing/login_nav_display_edrbnk.png" alt="log In navigation testing display">

<details><summary> Register navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246023/glamping/docs/user%20stories%20testing/register_nav_testing_cnrfmy.png" alt="register navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242573/glamping/docs/user%20stories%20testing/register_nav_display_y2zprs.png" alt="register navigation testing display">
</details>

<details><summary> Book navigation testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246506/glamping/docs/user%20stories%20testing/book_nav_testing_lpmsuq.png" alt="book navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242575/glamping/docs/user%20stories%20testing/book_nav_display_gt2ofy.png" alt="book navigation testing display">
</details>

LOOGED IN USER: 
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |

<details><summary> View your Bookings navigation testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688248135/glamping/docs/user%20stories%20testing/viewbooking_nav_testing_lt07dw.png" alt="view bookings navigation testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688247777/glamping/docs/user%20stories%20testing/viewbooking_nav_display_ui8pgh.png" alt="view bookings navigation testing display">
</details>


2. As a user, I want to compare different accomodation types available so that I can make an informed decision of which accomodation best suits my needs. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

3. As a user, I want to register for an account on the website so I can access restricted user areas of wesbite i.e viewing my bookings 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

4. As a returning user, I want to easily login to my account on the website to view my bookings and access full site functionality

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

5. As a user, I want to create a booking by selecting a date and accomodation-type for my stay

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

6. As a user, I want to review my booking so that I can remind myself of the date and accomadation type I have booked 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

7. As a user, I want to update my booking so that I can choose another available time and/or accomodation type. My previous details should be present on this form so I know what I am changing details from. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

8. As a user, I can delete my booking so that I can cancel my reservation for my stay 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

9. As a user, I want to be able to easily logout of my account so that my bookings are secure once again

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

10. As a user, I want a confirm delete page to display so i do not accidently click delete booking by accident.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

11. As a first time user, I should immediatley understand the purpose of the website from the home page so my time is not wasted 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

12. As an unregistered user, I have access to accomodation types, reviews and ratings information so I can make an informed decision on whether I should make an account to book a stay. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |

13. As a user, i want to my bookings information to be secure so no other users have access to it. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
something | something happens | Works as expected |








## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| When less than 3 bookings per user, bookings column appears squished into corner. This also appeared in confirm delete page.  | Removed d-flex of div of that section, this helped the display especially on larger screen sies. See [commit f7f98f4](https://github.com/ornao/pp4/commit/f7f98f448f9b3acc02061d16bfcfd2c2aa364f1e) and [commit 73f7ce1](https://github.com/ornao/pp4/commit/73f7ce1b1454e38038d58ad69283d78494a3d0d7) for further details. |
| | |
<details><summary> Before </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242350/1bugfixbefore_yicrjb.png" alt="bug fix before">
</details>
<details><summary> After </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242350/1bugfixafter_s2u5x3.png" alt="bug fix after1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242350/1bugfixafter2_bl9ehw.png" alt="bug fix after2">
</details>


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
- [Fix empty link logo error in WAVE](https://stackoverflow.com/questions/32631180/link-contain-no-text-showing-error-in-wave-accessibility-evaluation-tool)

Django Documentation:
- [the use of CreateView, UpdateView and DeleteView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
- [adding flash success messages to class based view](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)
- [remove html tags appearing to template](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)

W3Schools: 
- [remove html tags appearing to template](https://www.w3schools.com/django/ref_filters_striptags.php)