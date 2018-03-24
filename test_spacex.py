import os
import spacex
import unittest
import tempfile


class SpaceXTestCase(unittest.TestCase):

    def setUp(self):
        spacex.app.testing = True
        self.app = spacex.app.test_client()

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_launch1_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/launch/1')

        # assert the response data
        assert b'Space X Launch 1' in result.data
        assert b'Falcon 1' in result.data
        assert b'0a_00nJ_Y88' in result.data


if __name__ == '__main__':
    unittest.main()
