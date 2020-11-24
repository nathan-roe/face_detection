from django.db import models
import bcrypt
import re
# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['post_first']) < 3:
            errors['first_error'] = 'Please enter a longer first name.'
        if len(post_data['post_last']) <3:
            errors['last_error'] = 'Please enter a longer last name.'
        EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if not EMAIL_REGEX.match(post_data['post_email']):
            errors['email_error'] = 'There was an error with your email, please try again.'
        if len(post_data['post_password']) < 7:
            errors['password_error'] = 'This password is not secure, please enter a longer password'
        if post_data['post_password'] != post_data['post_confirm']:
            errors['confirm_error'] = "The passwords didn't match, please try again."
        return errors
    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')     
        if not EMAIL_REGEX.match(post_data['post_login_email']):
            errors['email_error'] = 'There was an error with your email, please try again.'
        if len(post_data['post_login_password']) < 7:
            errors['password_error'] = 'This password is not secure, please enter a longer password'
        # if email exists in database
        user_list = User.objects.filter(email=post_data['post_login_email'])
        if len(user_list) < 1:
            errors['query_error'] = "There was a problem with login"

        return errors
class User(models.Model):
    first_name=models.CharField(max_length=255)   
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    image = models.ImageField(upload_to='face_detector/static/known_faces')
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True)
    objects = UserManager()
