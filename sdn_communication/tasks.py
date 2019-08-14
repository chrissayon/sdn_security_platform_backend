# # Create your tasks here
# from __future__ import absolute_import, unicode_literals
# from celery import shared_task


# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)

from celery import task 
from celery import shared_task 
import requests 
# We can have either registered task 
@task(name='summary') 
def send_import_summary():
    response = requests.get('http://0.0.0.0:8080/stats/port/1')
    print(response)
    # Magic happens here ... 
# or 

# @shared_task 
# def send_notifiction():
#     print("Hi")
#      # Another trick