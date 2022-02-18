from django.db import models
from django.contrib.auth.models import AbstractUser

"""
# Create your models here.
class User(AbstractUser):
    # Basic User Model
    pass

    def __str__(self):
        return self.get_full_name()

class Word(models.Model):
    # Word model for table with all the words
    # todo Fields Below:
    # "text" (Charfield for holding the word)
    # "hash" (Charfield with a hash for the word, use generate_password [https://stackoverflow.com/a/51682653])
    # "length" (PositiveIntegerField that should be len(text))
    # "times_solved" (PositiveIntegerField with default=0, should hold
    #                   the number of correct submissions of this word)
    # "tries_to_solve" (PositiveIntegerField with default=0, should hold
    #                   the number of tries it took to solve [only should
    #                   update when a player solves the word])
    pass

    def __str__(self):
        return ""
        # todo string method
        # return the text, number of times solved,
        # and avg number of tries to solve... should be 0
        # if it's never been solved to avoid error

class Submission(models.Model):
    # Keeps track of user submissions for each word
    # [Each (user, word) pair should be unique]
    # todo Fields Below:
    # "user" (ForeignKey to User)
    # "word" (ForeignKey to Word)
    # "solved" (BooleanField)
    # "num_tries" (PositiveIntegerField, default=0, max=6 tries)
    pass
"""
