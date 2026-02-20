from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_user(self):
        team = Team.objects.create(name='Test Team2', description='A test team2')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_create_activity(self):
        team = Team.objects.create(name='Test Team3', description='A test team3')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Run', duration_minutes=30, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'Run')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for_team='Test Team')
        self.assertEqual(workout.name, 'Test Workout')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team4', description='A test team4')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
