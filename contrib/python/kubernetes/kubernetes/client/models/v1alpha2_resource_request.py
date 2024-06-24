# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.30
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha2ResourceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'named_resources': 'V1alpha2NamedResourcesRequest',
        'vendor_parameters': 'object'
    }

    attribute_map = {
        'named_resources': 'namedResources',
        'vendor_parameters': 'vendorParameters'
    }

    def __init__(self, named_resources=None, vendor_parameters=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2ResourceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._named_resources = None
        self._vendor_parameters = None
        self.discriminator = None

        if named_resources is not None:
            self.named_resources = named_resources
        if vendor_parameters is not None:
            self.vendor_parameters = vendor_parameters

    @property
    def named_resources(self):
        """Gets the named_resources of this V1alpha2ResourceRequest.  # noqa: E501


        :return: The named_resources of this V1alpha2ResourceRequest.  # noqa: E501
        :rtype: V1alpha2NamedResourcesRequest
        """
        return self._named_resources

    @named_resources.setter
    def named_resources(self, named_resources):
        """Sets the named_resources of this V1alpha2ResourceRequest.


        :param named_resources: The named_resources of this V1alpha2ResourceRequest.  # noqa: E501
        :type: V1alpha2NamedResourcesRequest
        """

        self._named_resources = named_resources

    @property
    def vendor_parameters(self):
        """Gets the vendor_parameters of this V1alpha2ResourceRequest.  # noqa: E501

        VendorParameters are arbitrary setup parameters for the requested resource. They are ignored while allocating a claim.  # noqa: E501

        :return: The vendor_parameters of this V1alpha2ResourceRequest.  # noqa: E501
        :rtype: object
        """
        return self._vendor_parameters

    @vendor_parameters.setter
    def vendor_parameters(self, vendor_parameters):
        """Sets the vendor_parameters of this V1alpha2ResourceRequest.

        VendorParameters are arbitrary setup parameters for the requested resource. They are ignored while allocating a claim.  # noqa: E501

        :param vendor_parameters: The vendor_parameters of this V1alpha2ResourceRequest.  # noqa: E501
        :type: object
        """

        self._vendor_parameters = vendor_parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha2ResourceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2ResourceRequest):
            return True

        return self.to_dict() != other.to_dict()