import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def hello_get(language):  # noqa: E501
    """Get a hello world message in a language of your choice

    Get a hello world message in a language of your choice # noqa: E501

    :param language: The language of the response
    :type language: str

    :rtype: InlineResponse200
    """
     query_string = [('language', 'language_example')]
        response = self.client.open(
            '/hello',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
    return 'do some magic!'
