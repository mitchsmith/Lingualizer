from app import app, db
import unittest
import os
import tempfile
from flask import json
#import yaml

TEST_DB = 'test.db'

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """initial test. ensure that the database exists"""
        tester = os.path.exists("lingualizer_alchemy.db")
        self.assertEqual(tester, True)

if __name__ == '__main__':
    unittest.main()
