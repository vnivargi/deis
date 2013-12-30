"""
Deis exception classes.
"""

from __future__ import unicode_literals

from rest_framework.exceptions import APIException
from rest_framework import status


class BuildNodeError(APIException):
    """Indicates a problem in building or bootstrapping a node."""

    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, detail=None):
        self.detail = detail