This is a web application that allows users to sign in to a site using their face from their device's camera as identification. This implements an MVT pattern. 
I'm using Python, Django, MySQL and OpenCV (an object detection library).
Python: Primary language being used. 
Django: Used to create the login and registration, allowing a user to upload a profile image to compare their face to later, and create validation, 
including validation for face detection.
MySQL: Stores user information (First Name, Last Name, Email, Password, Profile Image). Using Django this can be retrieved to have a user specific page on valid login/registration.
OpenCV: Allows object detection through a device's camera, which is specified for faces in this project. 
MVT Pattern: Using a model - view - template patten, This project can redirect a user to a success page on valid login or registration, specific to that user. Because it's 
primarily just an example of how this could be implemented in a larger project, the success page simply shows the user's information on successful face detection or login.
