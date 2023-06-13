from django.db import models
import datetime

# Create your models here.
class Destinations:
    id : int
    title: str
    description : str
    img : str
    time : datetime.date
    comment : str
