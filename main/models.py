from datetime import datetime
from django.db import models
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PHONE_REGEX = re.compile(r'^\+?1?\d{9,15}$')
# Create your models here.


class MovingManager(models.Manager):
    def moving_validator(self, postData):
        errors = {}
        if len(postData['inputName']) < 2:
            errors['name'] = "Name must be more than 2 characters!"
        if not EMAIL_REGEX.match(postData['inputEmail']):
            errors['email'] = "Invalid email address!"
        if not PHONE_REGEX.match(postData['inputPhone']):
            errors['phone'] = "Invalid phone number!"
        if len(postData['inputCurrentAddress']) < 15:
            errors['currentAddress'] = "Please include Street Address, City, ST, & ZIP for current address."
        if len(postData['inputMovingAddress']) < 15:
            errors['movingAddress'] = "Please include Street Address, City, ST, & ZIP for moving to address."
        if postData['inputMoveDate'] < str(datetime.date.today()):
            errors['moveDate'] = "Please select a date or one that is not in the past."
        return errors


class JunkRemovalManager(models.Manager):
    def junk_removal_validator(self, postData):
        errors = {}
        if len(postData['inputName']) < 2:
            errors['name'] = "Name must be more than 2 characters!"
        if not EMAIL_REGEX.match(postData['inputEmail']):
            errors['email'] = "Invalid email address!"
        if not PHONE_REGEX.match(postData['inputPhone']):
            errors['phone'] = "Invalid phone number!"
        if len(postData['inputItemAddress']) < 15:
            errors['currentAddress'] = "Please include Street Address, City, ST, & ZIP for Item address."
        if postData['inputMoveDate'] < str(datetime.date.today()):
            errors['moveDate'] = "Please select a date or one that is not in the past."
        if len(postData['inputMessage']) < 10:
            errors['movingAddress'] = "Please give some more details about the item we will be picking up."
        return errors


class ConsignmentManager(models.Manager):
    def consignment_validator(self, postData):
        errors = {}
        if len(postData['inputName']) < 2:
            errors['name'] = "Name must be more than 2 characters!"
        if not EMAIL_REGEX.match(postData['inputEmail']):
            errors['email'] = "Invalid email address!"
        if not PHONE_REGEX.match(postData['inputPhone']):
            errors['phone'] = "Invalid phone number!"
        if len(postData['inputItemAddress']) < 15:
            errors['currentAddress'] = "Please include Street Address, City, ST, & ZIP for Item address."
        if postData['inputMoveDate'] < str(datetime.date.today()):
            errors['moveDate'] = "Please select a date or one that is not in the past."
        if len(postData['inputMessage']) < 10:
            errors['movingAddress'] = "Please give some more details about the item we will be picking up."
        return errors


class Moving(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=15)
    currentAddress = models.CharField(max_length=1024)
    movingAddress = models.CharField(max_length=1024)
    moveDateTime = models.DateTimeField()
    itemImages = models.ImageField(blank=True, upload_to='upload_images/')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovingManager()


class JunkRemoval(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=15)
    itemAddress = models.CharField(max_length=1024)
    moveDateTime = models.DateTimeField()
    itemImages = models.ImageField(blank=True, upload_to='upload_images/')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JunkRemovalManager()


class Consignment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=15)
    itemAddress = models.CharField(max_length=1024)
    moveDateTime = models.DateTimeField()
    itemImages = models.ImageField(blank=True, upload_to='upload_images/')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ConsignmentManager()
