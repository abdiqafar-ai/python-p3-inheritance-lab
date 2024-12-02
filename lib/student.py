#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class with first_name and last_name
        super().__init__(first_name, last_name)
        # Initialize an empty knowledge list for the student
        self.knowledge = []

    def learn(self, new_knowledge):
        # Add the new knowledge to the student's knowledge list
        self.knowledge.append(new_knowledge)
