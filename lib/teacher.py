#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class with first_name and last_name
        super().__init__(first_name, last_name)
        # Teacher can modify or add more knowledge if needed
        # Knowledge is already initialized by the parent User class

    def teach(self):
        # Return a random item from the knowledge list
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]





