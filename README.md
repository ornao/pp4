
**Developer: Orna Reynolds**

<img src = "https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688635530/glamping/docs/amiresponsive_igvf0l.jpg" alt="am i responsive">

💻 [Visit live website](https://glamping2023.herokuapp.com/){:target="_blank"}

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
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


### About

This glamping website provides a user-friendly platform to experience a unique camping destination in the beautiful Irish countryside. This site aims to be visually immersive, featuring a user-friendly booking system and showcasing customer testimonials through a display of ratings and reviews.

<hr>

### User Goals
- Be able to check availability and pricing information for desired dates 
- Easily book and secure preferred accommodation type for desired dates 
- Gain insight of expected experience by reading reviews and ratings from previous guests 
- Able to easily contact the site owner with any questions, queries, or special requests 

### Site Owner Goals
- Aim to attract and engage potential customers with appealing visuals and user-friendly features
- Provide a seamless booking process to drive bookings and generate revenue to the campsite 
- Build trust and credibility of potential guests by displaying campsite reviews, ratings and testimonials from previous customers 
- Offer a means of communication between customers and site owner to ensure satisfactory customer support experience 

<hr>

## User Experience

### Target Audience

- Outdoors enthusiasts who seek and appreciate experiences in natural settings 
- Couples on a romantic getaway looking for an intimate and scenic experience 
- Tourists looking for a distinct and memorable experience in the Irish countryside
- Individuals in search of a retreat where they can relax, unwind and become rejuvenated through the power of mindfulness in idyllic natural settings  

### User Requirements and Expectations
- Intuitive navigation and seamless booking process 
- Visually appealing design incorporating high-quality images to illustrate the expected glamping experience 
- Fully responsive and accessible across different screen sizes and devices 
- Secure authorisation 

##### Back to [top](#table-of-contents)<hr>

## User Stories

I utilised the agile MoSCoW prioritisation method while planning the user stories for this project. This aided the created of a MVP from the beginning and lends itself to be of an iterative development style. 

My user stories were categorised into epics and sub-divided into individuals tasks/acceptance criteria; details of which can be found on my [kanban board](https://github.com/users/ornao/projects/5). User stories were also ranked using MoSCoW prioritisation and were each given a sprint which gave me a timeframe to complete the majority of the tasks outlined in the user story. I did not submit specific dates for each sprint as this was my first time undertaking a project like and I was unsure how long individual tasks would take me to complete. I also generally had varying times each evening around work, however I generally gave myself a week and a half times for each sprint. Hence, I included must have for an MVP in my first sprint and categorised the rest of te user stories accordingly in later sprints.

**Epics** | **Explanation** | **Relevenat user story** |
------------ | ------------ | ------------ |
UX | User has a good experience interacting with the wesbite | 1, 11,  |
CRUD | User can create, read(view), update and delete elemnts of the website | 5, 6, 7, 8, 10,  |
AUTHORISATION | User has ability to accessand be denied to restricted areas of website | 3, 4, 9, 13, 22, 23, 32, | 
INFORMATION DISPLAY | User has access to all necessary information website can provide | 2, 12, 14, 15, 16, 33 |
ADMIN ACCESS | Site owner/admin had access to backend and can manipulate and maintain website data from here | 27, 28, |
ENHANCED UX | Extra feautures enhance the minimum viable product created | 17, 18, 21, 24, 25, 26, 30 |
ERROR HANDLING | Website provides explanation and resolutions for most errors | 19, 20, 31, |

Acceptance criteria/tasks and milstone included in details of kanban board. 

### Users

#### MUST HAVE 

1. As a user, I want to easily navigate through the site to access all features and information about my possible stay [Kanban board user story link](https://github.com/ornao/pp4/issues/1)
2. As a user, I want to compare different accommodation types available so that I can make an informed decision of which accommodation best suits my needs [Kanban board user story link](https://github.com/ornao/pp4/issues/2)
3. As a user, I want to register for an account on the website so I can access restricted user areas of wesbite i.e viewing my bookings [Kanban board user story link](https://github.com/ornao/pp4/issues/3)
4. As a returning user, I want to easily login to my account on the website to view my bookings and access full site functionality [Kanban board user story link](https://github.com/ornao/pp4/issues/4)
5. As a user, I want to create a booking by selecting a date and accomomdation-type for my stay [Kanban board user story link](https://github.com/ornao/pp4/issues/5)
6. As a user, I want to review my booking so that I can remind myself of the date and accommodation type I have booked [Kanban board user story link](https://github.com/ornao/pp4/issues/6)
7. As a user, I want to update my booking so that I can choose another available time and/or accommodation type. My previous details should be present on this form so I know what I am changing details from [Kanban board user story link](https://github.com/ornao/pp4/issues/7)
8. As a user, I can delete my booking so that I can cancel my reservation for my stay [Kanban board user story link](https://github.com/ornao/pp4/issues/8)
9. As a user, I want to be able to easily logout of my account so that my bookings are secure once again [Kanban board user story link](https://github.com/ornao/pp4/issues/9)
10. As a user, I want a confirm delete page to display so i do not accidently click delete booking by accident [Kanban board user story link](https://github.com/ornao/pp4/issues/16)
11. As a first time user, I should immediately understand the purpose of the website from the home page so my time is not wasted [Kanban board user story link](https://github.com/ornao/pp4/issues/17)
12. As an unregistered user, I have access to accommodation types, reviews and ratings information so I can make an informed decision on whether I should make an account to book a stay [Kanban board user story link](https://github.com/ornao/pp4/issues/18)
13. As a user, I want my bookings information to be secure so no other users have access to it [Kanban board user story link](https://github.com/ornao/pp4/issues/19)

#### SHOULD HAVE 

14. As a user, I want to check the availability and pricing information for my desired dates [Kanban board user story link](https://github.com/ornao/pp4/issues/20)
15. As a user, I want to see previous customer reviews and ratings of the different accommodation types [Kanban board user story link](https://github.com/ornao/pp4/issues/14)
16. As a user I can view the latest testimonials first when I click on testimonials so that I can directly access the most up-to-date reviews available on the website [Kanban board user story link](https://github.com/ornao/pp4/issues/21)
17. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed [Kanban board user story link](https://github.com/ornao/pp4/issues/15)
18. As a user I have access to contact information so I can contact the site owners with any questions, queries, or special requests. Be able to contact site owner through site.  [Kanban board user story link](https://github.com/ornao/pp4/issues/23)
19. As a registered user I want to be able to be notified if I do something wrong while complete a booking form before I submit it so there are no complications with my booked stay [Kanban board user story link](https://github.com/ornao/pp4/issues/24)
20. As a user, an error page will display with a navigation link back home that tells me something has gone wrong with website but I have a way back to the website [Kanban board user story link](https://github.com/ornao/pp4/issues/25)


#### COULD HAVE 

21. As a user, I want to be able to see an interactive map of where the campsite is [Kanban board user story link](https://github.com/ornao/pp4/issues/26)
22. As a registered user, I can reset my password so that I can regain access to my account if I forget my password [Kanban board user story link](https://github.com/ornao/pp4/issues/27)
23. As a user, I can signup to the site using one of my social media accounts to allow for an even more seamless registration [Kanban board user story link](https://github.com/ornao/pp4/issues/28)
24. As a logged in user, I can like people's reviews so that I can show i agree with their comments about their stay [Kanban board user story link](https://github.com/ornao/pp4/issues/29)

#### WON'T HAVE 

25. As a registered user, I can be contacted directly by site owners on the website and receive replies and notifications of these replies through the website through messaging services [Kanban board user story link]()
26. As a user i want to have real-time weather reports for days of my stay available when booking [Kanban board user story link](https://github.com/ornao/pp4/issues/31)

### Admin/Site Owner

#### MUST HAVE 

27. As an admin, I can log in and access the back end of the site [Kanban board user story link](https://github.com/ornao/pp4/issues/10)
28. As an admin, I can manually add a booking so that I can accommodate bookings lodged through phone or email [Kanban board user story link](https://github.com/ornao/pp4/issues/11)
30. As a site owner, I want site the to be fully responsive and accessible [Kanban board user story link](https://github.com/ornao/pp4/issues/12)
31. As a site owner, i want all user entered data to be validated to reduce errors on database [Kanban board user story link](https://github.com/ornao/pp4/issues/32)
32. As a site owner, I want only logged in users to view details of their bookings [Kanban board user story link](https://github.com/ornao/pp4/issues/33)
33. As a site owner, I want every site visitor to be able to view the accommodation types on offer and reviews of these accommodations [Kanban board user story link](https://github.com/ornao/pp4/issues/34)
 
#### SHOULD HAVE 

34. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day [Kanban board user story link](https://github.com/ornao/pp4/issues/36)

#### Could have 

35. As a site owner, I want the customers to have a means of communicating with me on website to inform me of their experience of site vs any queries about their future stay [Kanban board user story link](https://github.com/ornao/pp4/issues/35)

<hr>

## Design

### Theme

A [bootstrap template Yummy](https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/) was used for this project. I also utilised another [bootstrap template Admin](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/) for the login/logout and forms of the site. I adapted and pulled aspects of the code for the website and changed CSS elements to better represent my vision for the glamping website.

### Colour 

I enjoyed the primary colours from the Yummy bootstrap theme (as mentioned above) and hence only changed the colours slightly from the original. I opted to replace the primary red colour with a magenta pink shade that complemented the visuals of my pictures. This subtle adjustment helped unify the elements of my website, creating a cohesive and visually appealing experience for visitors.

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687450655/glamping/docs/colours_website.png" alt="colours of wesbite">

<hr>

### Wireframes 

Included are the screenshots created prior to development. As you can see, the finished website looks slightly different but the core function of each page remains the same. 

<details><summary> Home page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/wireframes/home_page_wireframe_mzjg9q.png" alt="home page wireframe">
</details>

<details><summary> Accommodation page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950338/glamping/docs/wireframes/accommodation_page_wireframe_mrzg1a.png" alt="accomodation page wireframe">
</details>

<details><summary> Testimonials page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950339/glamping/docs/wireframes/testimonials_page_wireframes_svu8rr.png" alt="testimonials page wireframe">
</details>

<details><summary> Create bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/wireframes/book_page_wireframes_uh0brr.png" alt="create booking page wireframe">
</details>

<details><summary> View bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687951678/glamping/docs/wireframes/viewbookings_page_wireframes_c0rdr2.png" alt="view booking page wireframe">
</details>

<details><summary> Edit bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950683/glamping/docs/wireframes/editingbooking_page_wireframes_dm6bv4.png" alt="edit booking page wireframe">
</details>

<details><summary> Delete bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950684/glamping/docs/wireframes/deletebooking_page_wireframes_ve5j4m.png" alt="delete booking page wireframe">
</details>

<details><summary> Login page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/wireframes/login_page_wireframes_yk9ayf.png" alt="login page wireframe">
</details>

<details><summary> Signup page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950338/glamping/docs/wireframes/signup_page_wireframes_yhbpqg.png" alt="signup page wireframe">
</details>

<details><summary> Logout page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687950337/glamping/docs/wireframes/logout_page_wireframes_iiey7o.png" alt="logout page wireframe">
</details>

<details><summary> Error page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687952095/glamping/docs/wireframes/error_page_wireframes_koxnjy.png" alt="error page wireframe">
</details>

<details><summary> Contact page screenshot</summary>
- While i did not complete a contact page as part of this project, it is something I aim to achieve in future iterations of the project. 
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687952831/glamping/docs/wireframes/contact_page_wireframes_ab8awm.png" alt="contact page wireframe">
</details>

<hr>

## Structure 

The website consists of number of pages 7 pages when the user was not logged in and 11 pages when user was logged in. (Error pages 400, 404, 403 and 500 are counted as 1 page in this counting of pages stated above).

- Home 
<details><summary> Home page screenshots(2)</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593718/glamping/docs/wireframes/homepage_user_not_loggedin_lnxts4.png" alt="home page">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593721/glamping/docs/wireframes/homepage_user_loggedin_fgxk0f.png" alt="home page user logged in">
</details>
<br>

- Accommodation
<details><summary> Accommodation page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593711/glamping/docs/wireframes/accomodation_page_tlivm4.png" alt="accommodation page">
</details>
<br>

- Testimonials 
<details><summary> Testimonials page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593709/glamping/docs/wireframes/testimonials_page_wtmt5u.png" alt="testimonials page">
</details>
<br>

- Log in /Register /Log Out
<details><summary> Log in /Register /Log Out page screenshots(3)</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593709/glamping/docs/wireframes/login_page_kcmzap.png" alt="login page">

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593709/glamping/docs/wireframes/signup_page_pxxscw.png" alt="signup page">

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688594151/glamping/docs/wireframes/logout_page_grs3fw.png" alt="logout page">
</details>
<br>

- Book 
<details><summary> Book page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688594156/glamping/docs/wireframes/create_booking_page_ruvnk1.png" alt="book page">
</details>
<br>

- Error page (404)
- Could not test display of 403, 400 and 500 page errors through manual testing, however as 404 page displays and the same code is used for other error codes I do assume they will also display when called (my fingers are crossed). 
<details><summary> Error page (404) screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688595408/glamping/docs/wireframes/404_page_x0csbu.png" alt="error page">
</details>
<br>

User need to Log In to view these page: 
- View Bookings 

<details><summary> View bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593711/glamping/docs/wireframes/viewyourbookings_page_cugggm.png" alt="view bookings page">
</details>
<br>

- Edit Bookings 
<details><summary> Edit bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593714/glamping/docs/wireframes/edityourbookings_page_gkjaqp.png" alt="edit bookings page">
</details>
<br>

- Delete Bookings

<details><summary> Delete bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688593711/glamping/docs/wireframes/confirm_delete_bookings_page_oujywz.png" alt="delete bookings page">
</details>
<br>

<hr>

### Database

3 custom models were created for this project - accommodation, bookings and testimonials. My bookings model supports full CRUD functionality while accommodation and testimonials currently only pull from database. User model was provided for by django allauth. In future iterations, I would like to create an availability function in booking model to allow user to check if their desired accommodation is available for their desired dates. I would also like to include a contact model in future development so users have ability to directly contact site owner on site without having to ring or email separately.. I would also like to add more CRUD functionality to testimonials model so users can submit their own testimonials and 'like' different users reviews. 

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
- (price_per_night: DecimalField()) -- To be incorporated as a future feature
- (availibility: BooleanField() if available for booking dates) -- To be incorporated as a future feature

### Bookings model
This contains:
- booking_id: AutoField (PK)
- accommodation_id: ForeignKey
- user_id: ForeignKey
- check_in_date: DateField()
- check_out_date: DateField()
- length_of_stay: DurationField()
- num_guests: IntegerField()
- (total_price: DecimalField()) -- To be incorporated as a future feature

### Testimonials model
This contains:
- testimonial_id: AutoField (PK)
- user_id: ForeignKey
- accommodation_id: ForeignKey
- rating: IntegerField()
- content: TextField()
- date_created: DateField()
- image: ImageField(optional)
- (likes: user model) -- To be incorporated as a future feature

<details><summary> Database schema screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687959226/glamping/docs/database_schema_rfiwao.png" alt="database schema scrennshot">
</details>

<br>

### Future models 
<br>

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

<hr>

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
- [Irish dictionary](https://www.focloir.ie/) - to check spelling for fake address I made up 
- [BeFunky](https://www.befunky.com/)
- [AmIResponsive](https://ui.dev/amiresponsive)


##### Back to [top](#table-of-contents)

<hr>

## Validation

### HTML - [Validator](https://validator.w3.org/)

The W3S HTML validator checks the HTML through the webpage url. This is because the validator does not recognise the django template language when HTML input directly into validator. 

- This checks base.html and index.html
<details><summary> Home page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889359/glamping/docs/validation/home_html_validator_cl0mu2.png" alt="home page html validation check">
</details>
<br>

- This checks base.html and accomodation.html
<details><summary> Accommodation page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889261/glamping/docs/validation/accomodation_html_validator_cayv4c.png" alt="accomodation page html validation check">
</details>
<br>

- This checks base.html and testimonials.html
<details><summary> Testimonials page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687889276/glamping/docs/validation/testimonials_html_validator_p98e6o.png" alt="testimonials page html validation check">
</details>
<br>

- This checks base.html and account/login.html
<details><summary> Log In page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902571/glamping/docs/validation/login_html_validator_prlam4.png" alt="login page html validation check">
</details>
<br>

- This checks base.html and accounts/signup.html
<details><summary> Register page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902571/glamping/docs/validation/signup_html_validator_m4ctuw.png" alt="signup page html validation check">
</details>
<br>

- This checks base.html and account/logout.html
<details><summary> Log Out page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687902920/glamping/docs/validation/logout_html_validator_bgc04l.png" alt="logout page html validation check">
</details>
<br>

- This checks base.html and read_bookings.html
<details><summary> View your Bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/validation/read_bookings_html_validator_bfzmpe.png" alt="view bookings page html validation check">
</details>
<br>

- This checks base.html and create_bookings.html
<details><summary> Book page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/validation/create_bookings_html_validator_xvsnqd.png" alt="book page html validation check">
</details>
<br>

- This checks base.html and edit_bookings.html
<details><summary> Edit Bookings page screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/validation/edit_bookings_html_validator_cnekpe.png" alt="edit bookings page html validation check">
</details>
<br>

- This checks base.html and confirm_delete.html
<details><summary> Delete Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1687903563/glamping/docs/validation/delete_bookings_html_validator_asg3f5.png" alt="confirm delete page html validation check">
</details>
<br>


### CSS - [Jigsaw](https://jigsaw.w3.org/css-validator/)

- style.css was validated by direct inputting of contents of file into website.

<details><summary> style.css validation check screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688413019/glamping/docs/validation/jigsaw_css_validation_xldhzz.png" alt="style.css validation check">
</details>
<br>

### Javascript - [JSHint](https://jshint.com/)
- The js included in this project is from the [bootstrap template Yummy](https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/). I did not adapt this code in anyway hence I did not try to fiddle with it and mess up its functionality by trying to fulfil all the validation checks. I only fixed the issues relating to missing semi-colons.
<details><summary> main.js validation check screenshot</summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688598958/glamping/docs/validation/js_validation_p1qusa.png" alt="main.js validation check">
</details>
<br>

### Python - [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)

<details><summary> Glamping app (main app) validation screenshots(2)</summary>
settings.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/main_settings_x8lcy7.png" alt="settings.py">
urls.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/main_urls_os04io.png" alt="urls.py">

</details>

<details><summary> Bookings app validation screenshots(6)</summary>
admin.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/bookings_admin_i7d5qh.png" alt="admin.py">
forms.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616019/glamping/docs/validation/bookings_forms_bafoau.png" alt="froms.py">
models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688640697/glamping/docs/validation/bookings_models_cdhaja.png" alt="models.py">
test_models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688640697/glamping/docs/validation/bookings_test_models_qgick6.png" alt="test_models.py">
urls.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616019/glamping/docs/validation/bookings_urls_qbeyi3.png" alt="urls.py">
views.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/bookings_views_rujmlu.png" alt="views.py">

</details>

<details><summary> Accomodation app validation screenshots(5)</summary>
admin.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/accomodation_admin_na8mms.png" alt="admin.py">
models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688639671/glamping/docs/validation/accomodation_models_bbjlhv.png" alt="models.py">
test_models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688639671/glamping/docs/validation/accomodation_test_models_jkyact.png" alt="test_models.py">
urls.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616020/glamping/docs/validation/accomodation_url_cundlr.png" alt="urls.py">
views.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616021/glamping/docs/validation/accomodation_view_kyamus.png" alt="views.py">

</details>

<details><summary> Testimonials app validation screenshots(5)</summary>
admin.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/testimonials_admin_uht4xa.png" alt="admin.py">
models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/testimonials_models_n4gi5t.png" alt="models.py">
test_models.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688643654/glamping/docs/validation/testimonials_test_models_aj3ai4.png" alt="test_models.py">
urls.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/testimonials_urls_rlyzlm.png" alt="urls.py">
views.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/testimonials_views_r8wvag.png" alt="views.py">

</details>

<details><summary> Home app validation screenshots(2)</summary>
urls.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/home_urls_jqwydv.png" alt="urls.py">
views.py:
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688616018/glamping/docs/validation/home_views_sgfpp2.png" alt="views.py">

</details>
<br>

### Accessibility - [WAVE](https://wave.webaim.org/report)

<details><summary> Home page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/home_wave_validation_pbtqfy.png" alt="home page accessibility check">
</details>

<details><summary> Accommodation page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/accomodation_wave_validation_wizrl6.png" alt="accomodation page accessibility check">
</details>

<details><summary> Testimonials page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407258/glamping/docs/validation/testimonials_wave_validation_fwld9l.png" alt="testimonials page accessibility check">
</details>

<details><summary> Log In page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/login_wave_validation_gvjxln.png" alt="login page accessibility check">
</details>

<details><summary> Register page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407258/glamping/docs/validation/register_wave_validation_xrqbxw.png" alt="signup page accessibility check">
</details>

<details><summary> Log Out page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/signout_wave_validation_xs1bdx.png" alt="logout page accessibility check">
</details>


<details><summary> View your Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/viewbookings_wave_validation_zksu42.png" alt="view bookings page accessibility check">
</details>

<details><summary> Book page screenshot</summary>
Checked when user was logged in and not logged in 
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407327/glamping/docs/validation/book_wave_validation_notloggedin_g2kfdg.png" alt="create bookings page accessibility check">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688407257/glamping/docs/validation/book_wave_validation_loggedinuser_bdu2js.png" alt="create bookings page accessibility check when user logged in">
</details>

<details><summary> Edit Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688408262/glamping/docs/validation/editbookings_wave_validation_nceqyr.png" alt="edit bookings page accessibility check">
</details>

<details><summary> Delete Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688408261/glamping/docs/validation/deletebookings_wave_validation_kdrbwo.png" alt="delete bookings page accessibility check">
</details>
<br>

### Performance - Lighthouse

<details><summary> Home page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/homepage_desktop_lighthouse_le0d5c.png" alt="home page lighthouse check - desktop">
</details>

<details><summary> Accommodation page screenshot</summary>
<img src="" alt="accomodation page lighthouse check - desktop">
</details>

<details><summary> Testimonials page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/testimonials_desktop_lighthouse_r9gr0j.png" alt="testimonials page lighthouse check- desktop">
</details>

<details><summary> Log In page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/signin_desktop_lighthouse_i4s9jl.png" alt="login page lighthouse check - desktop">
</details>

<details><summary> Register page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/signup_desktop_lighthouse_jvdtq3.png" alt="signup page lighthouse check - desktop">
</details>

<details><summary> Log Out page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/signout_desktop_lighthouse_qzasbb.png" alt="logout page lighthouse check - desktop">
</details>


<details><summary> View your Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/viewbookings_desktop_lighthouse_svmcer.png" alt="view bookings page lighthouse check - desktop">
</details>

<details><summary> Book page screenshot</summary>
Checked when user was logged in and not logged in 
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773235/glamping/docs/validation/createbooking_desktop_lighthouse1_gkzq2e.png" alt="create bookings page lighthouse check">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773236/glamping/docs/validation/createbookings_desktop_lighthouse2_ca23q4.png" alt="create bookings page lighthouse check when user logged in">
</details>

<details><summary> Edit Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773637/glamping/docs/validation/Screenshot_2023-07-08_at_01.46.11_yc44eq.png" alt="edit bookings page lighthouse check">
</details>

<details><summary> Delete Bookings page screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773636/glamping/docs/validation/Screenshot_2023-07-08_at_01.46.42_u1gkbr.png" alt="delete bookings page lighthouse check">
</details>

<details><summary> 404 error page screenshot</summary>
- Page was unable to be tested - image is webp and unused css is removed as much as possible
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688773750/glamping/docs/validation/Screenshot_2023-07-08_at_01.48.56_uzntnu.png" alt="404 error page lighthouse check">
</details>

<br>

## Testing

### Manual testing

1. As a user, I want to easily navigate through the site to access all features and information about my possible stay.

LOGGED OUT USER: 
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Home' tab in the nav bar | Home page will display | Works as expected |
Click on the 'Accommodation' tab in the nav bar | Accommodation page will display | Works as expected |
Click on the 'Testimonials' tab in the nav bar | Testimonials page will display | Works as expected |
Click on the 'Log In' tab in the nav bar | Log in page will display | Works as expected |
Click on the 'Register' tab in the nav bar | Sign up page will display | Works as expected |
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
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688249372/glamping/docs/user%20stories%20testing/login_nav_testing3_fm3wqf.png" alt="log In navigation testing3">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688244998/glamping/docs/user%20stories%20testing/login_nav_display_edrbnk.png" alt="log In navigation testing display">
</details>

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


2. As a user, I want to compare different accommodation types available so that I can make an informed decision of which accommodation best suits my needs. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Accommodation' tab in the nav bar | Accommodation page will display | Works as expected |
Click on the 'Pods' tab in the subnav bar | Pods page will display | Works as expected |
Click on the 'Cabins' tab in the subnav bar | Cabins page will display | Works as expected |


<details><summary> Accommodation sub navigation bar testing screenshots - pods and cabins </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688256785/glamping/docs/user%20stories%20testing/pods_subnav_testing_zqncsl.png" alt="accomodation sub navigation testing - pods">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688256784/glamping/docs/user%20stories%20testing/cabins_subnav_testing_pd2e3e.png" alt="accomodation sub navigation testing display - cabins">
</details>

3. As a user, I want to register for an account on the website so I can access restricted user areas of wesbite i.e viewing my bookings 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Register' tab in the nav bar | Sign up page will display | Works as expected |
Enter username, email and good password correctly twice | User will be logged in | Works as expected |
Forgot to enter username | Error tab message will display, user will have to entered form again | Works as expected |
Forgot to enter email | As email is optional, no error message will display | Works as expected |
Entered weak password | Error tab message will display, user will have to entered form again | Works as expected |
Entered different passwords | Error tab message will display, user will have to entered form again | Works as expected |


<details><summary> Sign up testing screenshots </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688258868/glamping/docs/user%20stories%20testing/forgotusername_signup_testing_ohgzlv.png" alt="forgot username sign up testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688258868/glamping/docs/user%20stories%20testing/password_signup_testing_uvjjps.png" alt="password not strong enough sign up testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688259176/glamping/docs/user%20stories%20testing/username_signup_testing_1_xwfbsf.png" alt="username does not fulfill criteria sign up testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688259446/glamping/docs/user%20stories%20testing/password_signup_testing_u0wtt5.png" alt="password do not match sign up testing">

</details>


4. As a returning user, I want to easily login to my account on the website to view my bookings and access full site functionality

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Log In' tab in the nav bar | Log In page will display | Works as expected |
Click on the 'Log In' tab in the dropdown bar | Log In page will display | Works as expected |
Click on the 'Log In' link in the register page  | Log In page will display | Works as expected |
Click on the 'Log In' tab in the nav bar | Log In page will display | Works as expected |
Click on the 'Log In' link in the booking page | Log In page will display | Works as expected |
On 'Log In' page, type in username and password | User will be signed in and user brought to home page | Works as expected |
On 'Log In' page, type in random username and password | User will be not signed in and error message will display | Works as expected |


<details><summary> Easy Log In testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688261232/glamping/docs/user%20stories%20testing/user_login_testing_fekyuj.png" alt="easy log In testing display logging in user">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688261428/glamping/docs/user%20stories%20testing/user_successful_login_testing_ai42eq.png" alt="easy log In testing display logged in user">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688261580/glamping/docs/user%20stories%20testing/fakeuser_login_testing_djr2ky.png" alt="easy log In testing display logged in fakeuser">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246021/glamping/docs/user%20stories%20testing/login_nav_testing1_ddqnoy.png" alt="easy log In testing 1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688247605/glamping/docs/user%20stories%20testing/login_nav_testing2_vz1gqb.png" alt="easy log In testing2">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688249372/glamping/docs/user%20stories%20testing/login_nav_testing3_fm3wqf.png" alt="easy log In testing3">
</details>


5. As a user, I want to create a booking by selecting a date and accomomdation-type for my stay

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Book' tab in the nav bar | Create bookings page will display | Works as expected |
Click on the 'Log In' link in the booking page | Log In page will display | Works as expected |
On 'Log In' page, type in username and password | User will be signed in and brought to home page | Works as expected |
Click on the 'Book' tab in the nav bar or 'Book your Stay' in hero section of home page | Create bookings page will display | Works as expected |
Type in valid details to each field and press submit | User will be brought to view bookings page where most recent booking will appear first in list and success message will display | Works as expected |

<details><summary> Create booking testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688421449/glamping/docs/user%20stories%20testing/bookingform_testing_beforesubmit_kmfuuu.png" alt="valid details bookings form testing before submit">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688421477/glamping/docs/user%20stories%20testing/bookingform_testing_aftersubmit_rdjdwm.png" alt="valid details bookings form testing after submit">
</details>


6. As a user, I want to review my booking so that I can remind myself of the date and accommodation type I have booked 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |

<details><summary> View your Bookings page display screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688248135/glamping/docs/user%20stories%20testing/viewbooking_nav_testing_lt07dw.png" alt="view bookings page display testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688247777/glamping/docs/user%20stories%20testing/viewbooking_nav_display_ui8pgh.png" alt="view bookings page display testing">
</details>

7. As a user, I want to update my booking so that I can choose another available time and/or accommodation type. My previous details should be present on this form so I know what I am changing details from. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
Choose a booking, click edit button on that booking | Edit bookings page will display | Works as expected |
Change details of booking then press save changes | Read bookings page will display again, success message will display and details of booking will have changed | Works as expected |
Delete field of details of booking then press save changes | Error message will display as field cannot be blank | Works as expected |

<details><summary> Edit bookings page testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423955/glamping/docs/user%20stories%20testing/viewbooking_editingbooking_testing_gbuzq2.png" alt="viewbooking editingbooking testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688424084/glamping/docs/user%20stories%20testing/edit_editpagedisplay1_qfwdrr.png" alt="editpagedisplay1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423920/glamping/docs/user%20stories%20testing/edit_editpagedisplay2_xe2mzj.png" alt="editpagedisplay2">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423931/glamping/docs/user%20stories%20testing/edit_editfieldform_i5q0b9.png" alt="editfieldform">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423899/glamping/docs/user%20stories%20testing/updated_edit_booking_testing_huvqul.png" alt="updated edit booking testing">
</details>


8. As a user, I can delete my booking so that I can cancel my reservation for my stay 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
Choose a booking, click delete button on that booking | Confirm delete page will display | Works as expected |
Press confirm to delete booking | Read bookings page will display again, success message will display and booking will be gone

<details><summary> Delete bookings page testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498798/glamping/docs/user%20stories%20testing/viewbooking_delete_testing_vppliw.png" alt="viewbooking delete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498810/glamping/docs/user%20stories%20testing/confirmdelete_testing_g8obr6.png" alt="confirmdelete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498997/glamping/docs/user%20stories%20testing/delete_successful_testing_h6kzmg.png" alt="delete successful testing">
</details>

9. As a user, I want to be able to easily logout of my account so that my bookings are secure once again

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should click logout in nav bar from any page | Confirm logout should display | Works as expected |
User should click logout in confirm logout display | User should be redirected to home page and login should once again appear in nav bar | Works as expected |

<details><summary> Easy logout testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688502337/glamping/docs/user%20stories%20testing/navigate_to_logout_1_testing_p8izmg.png" alt="navigate to logout 1 testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688502330/glamping/docs/user%20stories%20testing/navigate_to_logout_2_testing_zicklp.png" alt="navigate to logout 2 testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688502321/glamping/docs/user%20stories%20testing/confirm_logout_testing_h1yfow.png" alt="confirm logout testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688502320/glamping/docs/user%20stories%20testing/looged_out_display_testing_1_ayuu3z.png" alt="logged out display testing">
</details>

10. As a user, I want a confirm delete page to display so I do not accidently click delete booking by accident.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
Choose a booking, click delete button on that booking | Confirm delete page will display | Works as expected |
Press confirm to delete booking | Read bookings page will display again, success message will display and booking will be gone

<details><summary> Confirm delete bookings page testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498798/glamping/docs/user%20stories%20testing/viewbooking_delete_testing_vppliw.png" alt="viewbooking delete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498810/glamping/docs/user%20stories%20testing/confirmdelete_testing_g8obr6.png" alt="confirmdelete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498997/glamping/docs/user%20stories%20testing/delete_successful_testing_h6kzmg.png" alt="delete successful testing">
</details>

11. As a first time user, I should immediately understand the purpose of the website from the home page so my time is not wasted 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Launch website | User should be brought to home page where it is immediately evident this is a website for a glamping campsite | Works as expected |

<details><summary> Purpose of website clear testing screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688573228/glamping/docs/user%20stories%20testing/homepage_purpose_testing_1_eytodn.png" alt="home page purpsoe clear testing">
</details>

12. As an unregistered user, I have access to accommodation types, reviews and ratings information so I can make an informed decision on whether I should make an account to book a stay. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Accommodation' tab in the nav bar | Accommodation page will display | Works as expected |
Click on the 'Pods' tab in the subnav bar | Pods page will display | Works as expected |
Click on the 'Cabins' tab in the subnav bar | Cabins page will display | Works as expected |
Click on the 'Testimonials' tab in the nav bar | Testimonials page will display | Works as expected |

<details><summary> Unregistered user navigation testing screenshots - accommodation and testimonials </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246030/glamping/docs/user%20stories%20testing/accomodation_nav_testing_dne3kd.png" alt="accomodation unregistered user testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/accomodation_nav_display_bh5hxa.png" alt="accomodation unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688503760/glamping/docs/user%20stories%20testing/pods_display_testing_qra62o.png" alt="accomodation pods unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688503749/glamping/docs/user%20stories%20testing/cabins_display_testing_vrpjit.png" alt="accomodation cabins unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246026/glamping/docs/user%20stories%20testing/testimonials_nav_testing_f6ho2m.png" alt="testimonials unregistered user testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/testimonials_nav_display_px3rvj.png" alt="testimonails unregistered user testing display">
</details>

13. As a user, I want to my bookings information to be secure so no other users have access to it. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
User should copy url of view bookings page | Link is copied by user | Works as expected |
User should click logout in nav bar from view bookings | Confirm logout should display | Works as expected |
User should click logout in confirm logout display | User should be redirected to home page and login should once again appear in nav bar | Works as expected |
User should then paste copied url of view bookings page to see if still has access | Bookings should not display | Works as expected |
Choose a booking, click edit button on that booking | Edit bookings page will display | Works as expected |
User should copy url of edit bookings page | Link is copied by user | Works as expected |
User should click logout in nav bar from view bookings | Confirm logout should display | Works as expected |
User should click logout in confirm logout display | User should be redirected to home page and login should once again appear in nav bar | Works as expected |
User should then paste copied url of edit bookings page to see if still has access | Editing a booking page should not display | Works as expected |


<details><summary> Secure bookings page testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504879/glamping/docs/user%20stories%20testing/bookings_displayed_before_notloggedout_ttkizu.png" alt="bookings display prior to logout">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504892/glamping/docs/user%20stories%20testing/bookings_notdisplayed_logged_out_judmdt.png" alt="bookings not displaying when logged out">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504884/glamping/docs/user%20stories%20testing/show_iamnot_loogedin_testing_pzysjc.png" alt="show iamnot loggedin testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688505762/glamping/docs/user%20stories%20testing/copyeditlinkuserauthorisation_djjj13.png" alt="edit bookings display prior to logout">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688505775/glamping/docs/user%20stories%20testing/bookingdoesnotdisplaywhenlinkchecked_udcjwt.png" alt="edit bookings display after logout">

</details>

15. As a user, I want to see previous customer reviews and ratings of the different accomodation types

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Testimonials' tab in the nav bar | Testimonials page will display | Works as expected |

<details><summary> Previous customer reviews and ratings page display screenshot</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688507636/glamping/docs/user%20stories%20testing/testimonials_display_1_f24y8k.png" alt="testimonials display testing">

</details>

17. As a user, I want to be notified when the action of creating, editing or deleting my reservation has been confirmed 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'Book' tab in the nav bar or 'Book your Stay' in hero section of home page | Create bookings page will display | Works as expected |
Type in valid details to each field and press submit | User will be brought to view bookings page where most recent booking will appear first in list and success message will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
Choose a booking, click edit button on that booking | Edit bookings page will display | Works as expected |
Change details of booking then press save changes | Read bookings page will display again, success message will display and details of booking will have changed | Works as expected |
Choose a booking, click delete button on that booking | Confirm delete page will display | Works as expected |
Press confirm to delete booking | Read bookings page will display again, success message will display and booking will be gone


<details><summary> Create booking message display testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688421449/glamping/docs/user%20stories%20testing/bookingform_testing_beforesubmit_kmfuuu.png" alt="valid details bookings form testing before submit">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688421477/glamping/docs/user%20stories%20testing/bookingform_testing_aftersubmit_rdjdwm.png" alt="valid details bookings form testing after submit">
</details>

<details><summary> Edit bookings message display testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423955/glamping/docs/user%20stories%20testing/viewbooking_editingbooking_testing_gbuzq2.png" alt="viewbooking editingbooking testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688424084/glamping/docs/user%20stories%20testing/edit_editpagedisplay1_qfwdrr.png" alt="editpagedisplay1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423920/glamping/docs/user%20stories%20testing/edit_editpagedisplay2_xe2mzj.png" alt="editpagedisplay2">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423931/glamping/docs/user%20stories%20testing/edit_editfieldform_i5q0b9.png" alt="editfieldform">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688423899/glamping/docs/user%20stories%20testing/updated_edit_booking_testing_huvqul.png" alt="updated edit booking testing">
</details>

<details><summary> Delete bookings message display testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498798/glamping/docs/user%20stories%20testing/viewbooking_delete_testing_vppliw.png" alt="viewbooking delete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498810/glamping/docs/user%20stories%20testing/confirmdelete_testing_g8obr6.png" alt="confirmdelete testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688498997/glamping/docs/user%20stories%20testing/delete_successful_testing_h6kzmg.png" alt="delete successful testing">
</details>

19. As a registered user I want to be able to be notified if I do something wrong while complete a booking form before I submit it so there are no complications with my booked stay. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'Book' tab in the nav bar or 'Book your Stay' in hero section of home page | Create bookings page will display | Works as expected |
Leave a field blank in form | Error message should display | Works as expected |
Incorrectly add email | Error message should display | Works as expected |
Add check in date for time after check out date | Custom error message should display | Works as expected |
Add incorrect number of guests for accommodation type | Custom error message should display | Works as expected |

<details><summary> Form validation testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/emptyfieldtesting_mlksmv.png" alt="emptyfieldtesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/invalidemailaddresstesting_mwaan5.png" alt="invalidemailaddresstesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/validdatesentrytesting_zzgjp7.png" alt="validdatesentrytesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/maximumgueststesting_wrjyj9.png" alt="maximumgueststesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/properaccomodationtesting_fvon5t.png" alt="properaccomodationtesting">
</details>

20. As a user, an error page will display with a navigation link back home that tells me something has gone wrong with website but I have a way back to the website.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Go to live site url and type in /habsnaj at end of link or something else random| Custom 404 page should display | Works as expected |

<details><summary> Custom error page display testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688583731/glamping/docs/user%20stories%20testing/404pagedisplay_krgn3t.png" alt="404 error page display">
</details>

27. As an admin, I can log in and access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Go to live site url and type in /admin at end of link | Django admin login panel should display | Works as expected |
Type in superuser login details and try to sign in | If created superuser correctly in workspace, superuser/admin should be signed into backend | Works as expected |

<details><summary> Admin login testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688510290/glamping/docs/user%20stories%20testing/admin_login_k1is2w.png" alt="admin login">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688510290/glamping/docs/user%20stories%20testing/admin_loggedin_lzh1fh.png" alt="admin logged in">
</details>

28. As an admin, I can manually add a booking so that I can accommodate bookings lodged through phone or email  

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
login as admin on backend | If created superuser correctly in workspace, superuser/admin should be signed into backend | Works as expected |
Navigate to bookings model| All bookings from all users should display in list | Works as expected |
Click add to manuall add booking| Add bookings form should display | Works as expected |
Add in user details and press save | Booking should be added successfully | Works as expected |

<details><summary> Add booking admin testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688734078/glamping/docs/user%20stories%20testing/add_bookings_admin_testing_izblv8.jpg" alt="add bookings admin testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688734083/glamping/docs/user%20stories%20testing/add_bookings_form_admin_testing_lk6rzu.jpg" alt="add bookings form admin testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688734088/glamping/docs/user%20stories%20testing/booking_admin_sucessful_1_eerwlw.jpg" alt="booking admin successful 1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688734091/glamping/docs/user%20stories%20testing/booking_admin_sucessful_admin_2_k7xedx.jpg" alt="booking admin successful 1">
</details>

30. As a site owner, I want site to be fully responsive and accessible

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Test wesbite on different devices | Website should display with good responsiveness and accessibility on each screen size | Works as expected |

<details><summary> Responsivness screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688584714/glamping/docs/user%20stories%20testing/homepage_testing_smallscreen_gthbop.png" alt="homepage testing smallscreen">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688584713/glamping/docs/user%20stories%20testing/homepage_testing_mediumscreen_ssi6ln.png" alt="homepage testing medium screen1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688584713/glamping/docs/user%20stories%20testing/homepage_testing_mediumscreen2_dmrch2.png" alt="homepage testing medium screen2">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688584714/glamping/docs/user%20stories%20testing/homepage_testing_largescreenx_fluyor.png" alt="homepage testing large screen">
</details>

31. As a site owner, i want all user entered data to be validated to reduce errors on database

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
User clicks on the 'Book' tab in the nav bar or 'Book your Stay' in hero section of home page | Create bookings page will display | Works as expected |
User leaves a field blank in form | Error message should display | Works as expected |
User incorrectly adds email | Error message should display | Works as expected |
User adds check in date for time after check out date | Custom error message should display | Works as expected |
User adds incorrect number of guests for accommodation type | Custom error message should display | Works as expected |

<details><summary> Form validation testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/emptyfieldtesting_mlksmv.png" alt="emptyfieldtesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/invalidemailaddresstesting_mwaan5.png" alt="invalidemailaddresstesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/validdatesentrytesting_zzgjp7.png" alt="validdatesentrytesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/maximumgueststesting_wrjyj9.png" alt="maximumgueststesting">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688574093/glamping/docs/user%20stories%20testing/properaccomodationtesting_fvon5t.png" alt="properaccomodationtesting">
</details>

32. As a site owner, I want only logged in users to view details of their bookings 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User should login | Home page will display | Works as expected |
Click on the 'View your bookings' tab in the nav bar | Read bookings page will display | Works as expected |
User should copy url of view bookings page | Link is copied by user | Works as expected |
User should click logout in nav bar from view bookings | Confirm logout should display | Works as expected |
User should click logout in confirm logout display | User should be redirected to home page and login should once again appear in nav bar | Works as expected |
User should then paste copied url of view bookings page to see if still has access | Bookings should not display | Works as expected |

<details><summary> Secure bookings page testing screenshots</summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504879/glamping/docs/user%20stories%20testing/bookings_displayed_before_notloggedout_ttkizu.png" alt="bookings display prior to logout">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504892/glamping/docs/user%20stories%20testing/bookings_notdisplayed_logged_out_judmdt.png" alt="bookings not displaying when logged out">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688504884/glamping/docs/user%20stories%20testing/show_iamnot_loogedin_testing_pzysjc.png" alt="show iamnot loggedin testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688505762/glamping/docs/user%20stories%20testing/copyeditlinkuserauthorisation_djjj13.png" alt="edit bookings display prior to logout">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688505775/glamping/docs/user%20stories%20testing/bookingdoesnotdisplaywhenlinkchecked_udcjwt.png" alt="edit bookings display after logout">

</details>

33. As a site owner, I want every site visitor to be able to view the accommodation types on offer and reviews of these accommodations

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on the 'Accommodation' tab in the nav bar | Accommodation page will display | Works as expected |
Click on the 'Pods' tab in the subnav bar | Pods page will display | Works as expected |
Click on the 'Cabins' tab in the subnav bar | Cabins page will display | Works as expected |
Click on the 'Testimonials' tab in the nav bar | Testimonials page will display | Works as expected |

<details><summary> Unregistered user navigation testing screenshots - accommodation and testimonials </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246030/glamping/docs/user%20stories%20testing/accomodation_nav_testing_dne3kd.png" alt="accomodation unregistered user testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/accomodation_nav_display_bh5hxa.png" alt="accomodation unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688503760/glamping/docs/user%20stories%20testing/pods_display_testing_qra62o.png" alt="accomodation pods unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688503749/glamping/docs/user%20stories%20testing/cabins_display_testing_vrpjit.png" alt="accomodation cabins unregistered user testing display">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688246026/glamping/docs/user%20stories%20testing/testimonials_nav_testing_f6ho2m.png" alt="testimonials unregistered user testing">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688242574/glamping/docs/user%20stories%20testing/testimonials_nav_display_px3rvj.png" alt="testimonails unregistered user testing display">
</details>
 
34. As an admin, I can filter bookings by date so that I can see what bookings we have for a particular day


## Automated testing

I created 17 automated tests fro this project. I tested 3 models - bookings, testimonials and accomodation. I ran tests in workspace by commenting out datbase url used for production and uncommenting other database url in settings.py file. 

Database url for testing: 

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688735062/glamping/docs/automated%20testing/database_url_testing_pgeftu.png" alt="database url for testing">

Database url for production: 

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688735062/glamping/docs/automated%20testing/database_url_production_fwu2ay.png" alt="database url for production">

<details><summary> All tests for models </summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688735063/glamping/docs/automated%20testing/all_automated_testing_thocut.png" alt="all models automated tests">

</details>

<details><summary> Bookings models </summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688735063/glamping/docs/automated%20testing/bookings_automated_testing_njey0h.png" alt="bookings models automated tests">

</details>

<details><summary> Accommodation models </summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688639727/glamping/docs/automated%20testing/accomodation_automated_testing_bjuzjk.png" alt="accommodation models automated tests">

</details>

<details><summary> Testimonials models </summary>

<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688735062/glamping/docs/automated%20testing/testimonials_automated_testing_oagnqn.png" alt="testimonials models automated tests">

</details>

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
| Error messages where displaying for num_guests and accomodation_name even when criteria were met for form to submit  | Tested what was happening using print statements. Error was thrown as by testing not in statement true was printed even when actual value was selected - hence issue with type not the same. Hence, str(accomodation_name) is the same as ['Honeymoon Pod'] for example  See [commit 76df1ce](https://github.com/ornao/pp4/commit/76df1ce8567c972be503c708ef82b6a969f14334) for further details. |

<details><summary> Before </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688412013/glamping/docs/bugs/honeymoon_error_before_aq3fer.png" alt="bug fix before">
</details>
<details><summary> After </summary>
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688412013/glamping/docs/bugs/honeymoon_error_after_ipu5rh.png" alt="bug fix after1">
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688412014/glamping/docs/bugs/honeymoor_error_success_zi8sie.png" alt="bug fix after2">
</details>

## Future Bug fixes

| **Bug** | **Fix** |
| ------- | ------- |
|Confirm delete submit buttom does not match other buttons of website| check div classes and id to see what is inhibiting styling|


## Future development 
- Future development will include a form whereby customers can contact owners directly from site rather than having to email, phone separately.
- Double bookings are not an immediate threat to tthe booking system of this website as there are a number of pods/cabins of teh same type. The future availibility function will help show user what is available and what is not in due course. 

## Deployment

1. Login to heroku accound and navigate to the dashboard 
2. Click "New" on upper right hand side of screen 
3. In dropdown of "New" button, click first option "Create new app"
4. In "Create new app" screen, type in a unique name for your app and choose the region closest to you
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688765976/glamping/docs/deployment/name_deployment_vuga9e.png" alt="deploymentname">

5. Click "Create app" 
6. You will be brought to deployment tab, from here naviagte to settings tab
7. Press "Reveal config vars" and add DATABASE_URL, SECRET_KEY and their values to KEY, VALUE fields
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688765976/glamping/docs/deployment/config_vars_rq4uj8.png" alt="reveal config vars">

8. Also add PORT, 8000 to KEY, VALUE fields in config vars to help with deployment 
9. Also add CLOUDINARY_URL and url of your API Environment variable to KEY, VALUE fields 
10. Add temporary DISABLE_COLLECTSTATIC, 1 KEY, VALUE pairs to allow skeleton project to run as project currenlty without statics fields (this will be removed at later stage)
11. In ALLOWED_HOSTS in settings.py file, type in project name url so project can run - in my case "glamping2023.herokuapp.com" 
12. Next you need to create a Procfile so heroku knows how to run the project - in my case add "web: gunicorn glamping.wsg" to file
13. In heroku, navigate to deploy tab of project and click github as deployment method 
14. Search for repository to connect github to heroku and press connect button beside correct repository
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688765976/glamping/docs/deployment/connect_repo_o06l81.png" alt="connect repo">

14. Then scroll down to bottom of page and click on deploy branch (can clcik on build log to see deployment progress)
15. Once build is finsihed, the build log will tell you 
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688765976/glamping/docs/deployment/build_finished_deployment_vgpoke.png" alt="build finished deployment">

16. From here, press open app in top right hand of screen to see if deployment successful 
should open to this page if deployment succesful
<img src="https://res.cloudinary.com/dg3ksw7zy/image/upload/v1688765977/glamping/docs/deployment/django_deployment_sucessful_obryq1.png" alt="deployment successful">

### Credits 

#### Photos


- [Accomodations images courtesy of Podumna Glamping Village](https://podumnavillage.ie/)
- Photo by <a href="https://unsplash.com/@captainhouque?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alex Houque</a> on <a href="https://unsplash.com/photos/Twke63oNYM0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>Hero image on home page
- Photo by <a href="https://unsplash.com/@ashleighjoyphotography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ashleigh Joy Photography</a> on <a href="https://unsplash.com/photos/BdEgT847nk0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>: Photo of boaton create bookings page
- Photo by <a href="https://unsplash.com/@fionakiwi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Fiona Jackson</a> on <a href="https://unsplash.com/s/photos/no-access?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/@caleb_woods?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Caleb Woods</a> on <a href="https://unsplash.com/s/photos/hiding?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/pt-br/@dexezekiel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dex Ezekiel</a> on <a href="https://unsplash.com/s/photos/confused?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/@robertharknessart?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Robert Harkness</a> on <a href="https://unsplash.com/s/photos/building-on-fire?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/@bamsnl?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jochen Bams</a> on <a href="https://unsplash.com/s/photos/galway-countryside?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
  
#### Code 
Templates:
- [bootstrap template Yummy](https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/) 
- [bootstrap template Admin](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/)

StackOverflow:
- [adding max and min validators to rating on rating field](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- [adding success message to deleteview class](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)
- [Fix empty link logo error in WAVE](https://stackoverflow.com/questions/32631180/link-contain-no-text-showing-error-in-wave-accessibility-evaluation-tool)
- [date picker input on model form](https://stackoverflow.com/questions/61077802/how-to-use-a-datepicker-in-a-modelform-in-django)
- [date picker simple way](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django)
- [adding multiple errors](https://stackoverflow.com/questions/60298923/what-are-the-differences-between-using-self-add-error-and-raising-a-validation)
- [adding a error pages](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page)

Django Documentation:
- [the use of CreateView, UpdateView and DeleteView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
- [adding flash success messages to class based view](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)
- [remove html tags appearing to template](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
- [widgets](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/)
- [working with forms](https://docs.djangoproject.com/en/4.2/topics/forms/)
- [django allauth documentation](https://django-allauth.readthedocs.io/en/latest/views.html#signup-account-signup)
- [django admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#modeladmin-options)

- [use of reverse lazy](https://www.fullstackpython.com/django-urls-reverse-lazy-examples.html)

W3Schools: 
- [remove html tags appearing to template](https://www.w3schools.com/django/ref_filters_striptags.php)

Youtube:
[datepicker input](https://www.youtube.com/watch?v=I2-JYxnSiB0&t=191s)

## Acknowledgements

I would like to sincerly thank for my very pateint boyfriend who sat with me in a hostel in copenhagen and helped me check my readme files for possible errors and my mentor martina who was so so helpful, supportive and knowledgable about the criteria of the portfolio. 