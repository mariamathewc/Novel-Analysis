import pymysql
import requests
import unittest
import os


value = os.getenv("TEST_KEY") 
RUN_UNIT_TEST = True
class TestAPI(unittest.TestCase):
   
    request_url ="https://www.geeksforgeeks.org/largest-palindromic-number-in-an-array/"
    @unittest.skipUnless(RUN_UNIT_TEST == True, reason="unit test not required")
    def test_visitor_endpoint_status_code_equals_200(self):

        response = requests.get(TestAPI.request_url)
        assert response.status_code == 200

   


if __name__ == '__main__':
    unittest.main()
