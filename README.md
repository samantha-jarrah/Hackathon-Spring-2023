# Vocabulary Worksheet Generator - Hackathon Spring 2023
Cameron Chafin, Samantha Jarrah, Claudia Sitiriche, Emily Craven

## Summary
Utilizing the OpenAI API, this application generates a vocabulary worksheet for ESL/English teachers based on user input.

## Application Features
- An index page, which explains the function of the application to the user and provides a button for the form page
- A form page, which allows the user to provide input on the type of worksheet they would like to generate based on:
    - grade level
    - english ability 
    - vocabulary list
    - question type 
       - fill in the blank
       - definition matching
       - multiple choice
       - synonym
       - antonym
- Once the form is submitted, a call is made to the OpenAI API to generate a random worksheet in a visually pleasing format
- The user is routed to a download page where they may preview the generated .pdf and download if they wish

## Technologies Used
- Backend
    - Python
    - Flask
    - OpenAI API
- Frontend
    - Bootstrap
    - HTML
- Deployment
    - Heroku

## Demo
<a href="https://gifyu.com/image/SnoHd"><img src="https://s11.gifyu.com/images/Animation0729372aacccb0a3.gif" alt="Animation0729372aacccb0a3.gif" border="0" /></a>

<img src="https://i.imgur.com/18yQiWN.png">

## Notes
Lessons learned, etc
