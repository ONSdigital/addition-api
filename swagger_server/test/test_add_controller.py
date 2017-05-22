# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase


class TestAddController(BaseTestCase):
    """ AddController integration test stubs """

    def test_add(self):
        """
        Test case for add

        adds two numbers
        """
        query_string = [('x', 56),
                        ('y', 56)]
        response = self.client.open('/addition-api/1.0.0/add',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
