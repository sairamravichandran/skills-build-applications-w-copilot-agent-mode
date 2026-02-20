from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc.name, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Activities
        for user in User.objects.all():
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for_team='Marvel')
        Workout.objects.create(name='Power Circuit', description='Strength and endurance for DC', suggested_for_team='DC')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
