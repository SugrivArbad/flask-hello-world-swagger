# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MessageSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, msg_text: str=None):  # noqa: E501
        """MessageSummary - a model defined in Swagger

        :param id: The id of this MessageSummary.  # noqa: E501
        :type id: str
        :param msg_text: The msg_text of this MessageSummary.  # noqa: E501
        :type msg_text: str
        """
        self.swagger_types = {
            'id': str,
            'msg_text': str
        }

        self.attribute_map = {
            'id': 'ID',
            'msg_text': 'msgText'
        }
        self._id = id
        self._msg_text = msg_text

    @classmethod
    def from_dict(cls, dikt) -> 'MessageSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageSummary of this MessageSummary.  # noqa: E501
        :rtype: MessageSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this MessageSummary.

        The ID of the message. Any alphanumeric string can be returned.  # noqa: E501

        :return: The id of this MessageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this MessageSummary.

        The ID of the message. Any alphanumeric string can be returned.  # noqa: E501

        :param id: The id of this MessageSummary.
        :type id: str
        """

        self._id = id

    @property
    def msg_text(self) -> str:
        """Gets the msg_text of this MessageSummary.

        The Hello World message in the requested language  # noqa: E501

        :return: The msg_text of this MessageSummary.
        :rtype: str
        """
        return self._msg_text

    @msg_text.setter
    def msg_text(self, msg_text: str):
        """Sets the msg_text of this MessageSummary.

        The Hello World message in the requested language  # noqa: E501

        :param msg_text: The msg_text of this MessageSummary.
        :type msg_text: str
        """
        allowed_values = ["Bonjour le monde", "Hello world", "Namastey sansar"]  # noqa: E501
        if msg_text not in allowed_values:
            raise ValueError(
                "Invalid value for `msg_text` ({0}), must be one of {1}"
                .format(msg_text, allowed_values)
            )

        self._msg_text = msg_text
