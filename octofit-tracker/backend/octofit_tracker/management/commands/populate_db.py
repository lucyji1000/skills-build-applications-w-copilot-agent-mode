from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many([
            {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        db.teams.insert_many([
            {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
            {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
        ])

        db.activity.insert_many([
            {"user": "thundergod", "activity_type": "Cycling", "duration": "1:00:00"},
            {"user": "metalgeek", "activity_type": "Crossfit", "duration": "2:00:00"},
            {"user": "zerocool", "activity_type": "Running", "duration": "1:30:00"},
            {"user": "crashoverride", "activity_type": "Strength", "duration": "0:30:00"},
            {"user": "sleeptoken", "activity_type": "Swimming", "duration": "1:15:00"},
        ])

        db.leaderboard.insert_many([
            {"user": "thundergod", "score": 100},
            {"user": "metalgeek", "score": 90},
            {"user": "zerocool", "score": 95},
            {"user": "crashoverride", "score": 85},
            {"user": "sleeptoken", "score": 80},
        ])

        db.workouts.insert_many([
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))