from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test Team')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=50)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 50)
