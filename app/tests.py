from django.test import TestCase
import re


is_email = re.match(r'^[\w\.-]+@[\w\.-]+$','duah.marfochristian@gmail.com')
is_email = re.search(r'^[\w\.-]+@[\w\.-]+$','duah.marfochristian@gmail.com')

print(is_email)
# Create your tests here.
