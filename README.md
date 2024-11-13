# esse3-api-liuc


This library allows you to connect and perform some basic operations on the University's online platform. The code was tailor-made for the LIUC university (https://sol.liuc.it) but with minor changes it is possible to make it work for (more or less) 70 Italian universities.

## Installing

Just download the code and, for an implementation example, run main.py with python 3.x.

## Content

The ultimate goal of this project is to create a mobile application or a telegram bot that allows you to quickly access your university career information. 
The university site is developed by CINECA and is based on the ESSE3 platform.
Initially, since I was unaware that there were documented APIs, I replicated HTTP requests and wrote a script that "simulated" a user's standard navigation and scrapped the necessary information through XPath and CSS Selectors.
The results were satisfying and fast enough but a minor change to the academic site frontend would have broken the whole script.
So after a quick search, I found the official REST API documentation.
Through this I created some simple functions that returned grades, exams to be taken, exams taken, average marks, sessions available for booking.
Over the next few weeks, I will be adding more features, if time permits.


## Legal Use Notes

Since the APIs are publicly available, since there is no document on the university page that prohibits their use, and because there's no need for a APIkey I assumed they were intended for public use. In case I am wrong please contact me.

## Functions 

There are two types of function:
- Function that uses REST API calls 
- Function that works through HTTP requests and html scraping 

### REST API FUNCTIONS:

  **login**(username, pwd) = return info about the students, useful for other functions which requires the career ID for example.

  **get_appelli**(username, pwd) = return a matrix with info about next exams available for being booked, the matrix contains [exam_name, exam_date, open_bookings_date, closure_bookings_date, exam_description]

  **get_media**(username1, pwd) = return marks' average and potential degree evaluation 

  **get_libretto**(user,pass) = return matrix with exam_description and marks

### HTTP SCRAPING FUNCTIONS: 

  **get_last_mark**(user, pass) = return the last marks [professor, date, mark] only works after running liucLogin()

  **liucLogin**(user, pass) = needed for get_last_mark function


## How to implement for different universities

For other universities using the esse3 service all functions that rely on the REST API should work, but it is absolutely necessary to change the endpoints. It is enough to change the domain.
The function that uses HTTP requests scraping theoretically cannot work for other universities, as it is based on the html layout.

## What's next?

I'll try to implement endpoints for all the other unis in a dynamic way and add more functions. 
A simple telegram bot using these APIs will be released in few days. 

