from django.test import TestCase
from sdn_communication import tasks
from rest_framework import status

class TasksTestCase(TestCase):
    def test_switch_number(self):
        """Testing if switch numbers are available"""
        self.assertNotEqual(tasks.get_switch_number(), status.HTTP_200_OK)

        #self.assertEqual(tasks.get_switch_number()."apple")
