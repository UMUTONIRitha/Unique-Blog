import unittest
from app.models import Blog
Blog = Blog

class BlogTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_blog = Blog()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))