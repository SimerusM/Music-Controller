from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    # Generating random codes until we find one that's not in DB and is unique
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # will store a bunch of characters
    host = models.CharField(max_length=50, unique=True) # rule: 1 host can not have multiple rooms
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    





