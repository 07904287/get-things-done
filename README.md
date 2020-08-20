![Screenshot of homepage](https://github.com/ricardobayes/get-things-done/blob/master/Screenshot%20from%202020-08-14%2012-45-26.png)


Given how much I procrastinated instead of deciding on a final project for CS50, I decided to write a web app that helps productivity.
Therefore, "Get things done", an easy-to-use web app was brought to life.
It's key features:
- Add and edit things that you need or want to do
- Ability to start a 5-minute sprint (focused work) based off said things, or standalone

I believe it's more complex and different from other projects because:
It is responsive, has an animated sidebar (on mobile screens), utilizes file upload including changing/clearing and downloading an uploaded file, a date picker and an animated, circular progress bar with countdown.
Last but not least, I believe there is a major improvement in the looks department over my previous apps.

Description of files:
templates/saas:
layout.html - Governs the structure of the page, including the header and sidebar and a placeholder for the main content, all other pages include this so all pages look the same.
index.html - Going through tasks saved in the database in a for loop and displaying them. For each entry it is possible to mark them complete by clicking the checkmark icon, edit them, or start a sprint based off that task, or download the attachment if there is any.
create.html - Form for adding new a Tasks object to the database through a django form.
edit.html - Same as create page, only with pre-populated form fields based on existing data
register.html - Form that captures user data to create a User object
sprint.html - Countdown of 5 minutes with a circular progress bar updating every second. The idea is that you want to focus on a given task for 5 minutes, giving it your undivided attention. If the timer reaches 0:00, confetti is thrown! There are buttons to reset the timer and to mark the task complete. A standalone sprint can be started without logging in.

static/saas: 
style.css - Controls the appearance of the pages
index.js - Contains the function for the animation of the progress bar and the countdown in sprint.html, the function for making tasks complete (a POST fetch) and throwing confetti!

Special thanks to Brian Yu and David J. Malan for creating this ground-breaking course, during which I went zero to hero!

Credit:
sidebar https://bootstrapious.com/p/bootstrap-sidebar
circular progress bar https://bootstrapious.com/p/circular-progress-bar
confetti https://codepen.io/cerpow/pen/RwNaeOb
