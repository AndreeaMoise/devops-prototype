from swagger_server.service.identification_service import *
import connexion
import six

from swagger_server.models.identification import Identification  # noqa: E501
from swagger_server import util


def identify(body=None):  # noqa: E501
    """identify

    Verify whether the driver, truck, load and location sent at a checkpoint match # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Identification.from_dict(connexion.request.get_json())  # noqa: E501
        return add(body);
    return 500,'error'
