from django.test import TestCase

# Create your tests here.
from milestones.models import ProjectsTable, MilestonesTable

class MilestonesTestCase(TestCase):
    fixtures = [
        "milestones_test_fixtures.json",
    ]

    def setUp(self):
        self.project = ProjectsTable.objects.get(pk=1)

    def test_string_representation_project(self):
        expected = "PyCon Talk"
        self.assertEqual(expected, str(self.project))

    def test_string_representation_milestone(self):
        expected = "Start the project"
        milestone = MilestonesTable.objects.get(pk=1)
        self.assertEqual(expected, str(milestone))

    def test_contains_title(self):
        title = "Milestone Tracking"
        response = self.client.get("/")
        self.assertContains(response, title)
