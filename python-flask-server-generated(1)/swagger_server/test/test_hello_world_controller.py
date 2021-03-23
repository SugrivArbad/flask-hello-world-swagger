# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHelloWorldController(BaseTestCase):
    """HelloWorldController integration test stubs"""

    def test_hello_get(self):
        """Test case for hello_get

        Get a hello world message in a language of your choice
        """
        query_string = [('language', 'language_example')]
        response = self.client.open(
            '/hello',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
