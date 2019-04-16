# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1OAuthClient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token_inactivity_timeout_seconds': 'int',
        'access_token_max_age_seconds': 'int',
        'additional_secrets': 'list[str]',
        'api_version': 'str',
        'grant_method': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'redirect_ur_is': 'list[str]',
        'respond_with_challenges': 'bool',
        'scope_restrictions': 'list[V1ScopeRestriction]',
        'secret': 'str'
    }

    attribute_map = {
        'access_token_inactivity_timeout_seconds': 'accessTokenInactivityTimeoutSeconds',
        'access_token_max_age_seconds': 'accessTokenMaxAgeSeconds',
        'additional_secrets': 'additionalSecrets',
        'api_version': 'apiVersion',
        'grant_method': 'grantMethod',
        'kind': 'kind',
        'metadata': 'metadata',
        'redirect_ur_is': 'redirectURIs',
        'respond_with_challenges': 'respondWithChallenges',
        'scope_restrictions': 'scopeRestrictions',
        'secret': 'secret'
    }

    def __init__(self, access_token_inactivity_timeout_seconds=None, access_token_max_age_seconds=None, additional_secrets=None, api_version=None, grant_method=None, kind=None, metadata=None, redirect_ur_is=None, respond_with_challenges=None, scope_restrictions=None, secret=None):
        """
        V1OAuthClient - a model defined in Swagger
        """

        self._access_token_inactivity_timeout_seconds = None
        self._access_token_max_age_seconds = None
        self._additional_secrets = None
        self._api_version = None
        self._grant_method = None
        self._kind = None
        self._metadata = None
        self._redirect_ur_is = None
        self._respond_with_challenges = None
        self._scope_restrictions = None
        self._secret = None
        self.discriminator = None

        if access_token_inactivity_timeout_seconds is not None:
          self.access_token_inactivity_timeout_seconds = access_token_inactivity_timeout_seconds
        if access_token_max_age_seconds is not None:
          self.access_token_max_age_seconds = access_token_max_age_seconds
        if additional_secrets is not None:
          self.additional_secrets = additional_secrets
        if api_version is not None:
          self.api_version = api_version
        if grant_method is not None:
          self.grant_method = grant_method
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        if redirect_ur_is is not None:
          self.redirect_ur_is = redirect_ur_is
        if respond_with_challenges is not None:
          self.respond_with_challenges = respond_with_challenges
        if scope_restrictions is not None:
          self.scope_restrictions = scope_restrictions
        if secret is not None:
          self.secret = secret

    @property
    def access_token_inactivity_timeout_seconds(self):
        """
        Gets the access_token_inactivity_timeout_seconds of this V1OAuthClient.
        AccessTokenInactivityTimeoutSeconds overrides the default token inactivity timeout for tokens granted to this client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. This value needs to be set only if the default set in configuration is not appropriate for this client. Valid values are: - 0: Tokens for this client never time out - X: Tokens time out if there is no activity for X seconds The current minimum allowed value for X is 300 (5 minutes)

        :return: The access_token_inactivity_timeout_seconds of this V1OAuthClient.
        :rtype: int
        """
        return self._access_token_inactivity_timeout_seconds

    @access_token_inactivity_timeout_seconds.setter
    def access_token_inactivity_timeout_seconds(self, access_token_inactivity_timeout_seconds):
        """
        Sets the access_token_inactivity_timeout_seconds of this V1OAuthClient.
        AccessTokenInactivityTimeoutSeconds overrides the default token inactivity timeout for tokens granted to this client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. This value needs to be set only if the default set in configuration is not appropriate for this client. Valid values are: - 0: Tokens for this client never time out - X: Tokens time out if there is no activity for X seconds The current minimum allowed value for X is 300 (5 minutes)

        :param access_token_inactivity_timeout_seconds: The access_token_inactivity_timeout_seconds of this V1OAuthClient.
        :type: int
        """

        self._access_token_inactivity_timeout_seconds = access_token_inactivity_timeout_seconds

    @property
    def access_token_max_age_seconds(self):
        """
        Gets the access_token_max_age_seconds of this V1OAuthClient.
        AccessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this client. 0 means no expiration.

        :return: The access_token_max_age_seconds of this V1OAuthClient.
        :rtype: int
        """
        return self._access_token_max_age_seconds

    @access_token_max_age_seconds.setter
    def access_token_max_age_seconds(self, access_token_max_age_seconds):
        """
        Sets the access_token_max_age_seconds of this V1OAuthClient.
        AccessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this client. 0 means no expiration.

        :param access_token_max_age_seconds: The access_token_max_age_seconds of this V1OAuthClient.
        :type: int
        """

        self._access_token_max_age_seconds = access_token_max_age_seconds

    @property
    def additional_secrets(self):
        """
        Gets the additional_secrets of this V1OAuthClient.
        AdditionalSecrets holds other secrets that may be used to identify the client.  This is useful for rotation and for service account token validation

        :return: The additional_secrets of this V1OAuthClient.
        :rtype: list[str]
        """
        return self._additional_secrets

    @additional_secrets.setter
    def additional_secrets(self, additional_secrets):
        """
        Sets the additional_secrets of this V1OAuthClient.
        AdditionalSecrets holds other secrets that may be used to identify the client.  This is useful for rotation and for service account token validation

        :param additional_secrets: The additional_secrets of this V1OAuthClient.
        :type: list[str]
        """

        self._additional_secrets = additional_secrets

    @property
    def api_version(self):
        """
        Gets the api_version of this V1OAuthClient.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1OAuthClient.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1OAuthClient.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1OAuthClient.
        :type: str
        """

        self._api_version = api_version

    @property
    def grant_method(self):
        """
        Gets the grant_method of this V1OAuthClient.
        GrantMethod determines how to handle grants for this client. If no method is provided, the cluster default grant handling method will be used. Valid grant handling methods are:  - auto:   always approves grant requests, useful for trusted clients  - prompt: prompts the end user for approval of grant requests, useful for third-party clients  - deny:   always denies grant requests, useful for black-listed clients

        :return: The grant_method of this V1OAuthClient.
        :rtype: str
        """
        return self._grant_method

    @grant_method.setter
    def grant_method(self, grant_method):
        """
        Sets the grant_method of this V1OAuthClient.
        GrantMethod determines how to handle grants for this client. If no method is provided, the cluster default grant handling method will be used. Valid grant handling methods are:  - auto:   always approves grant requests, useful for trusted clients  - prompt: prompts the end user for approval of grant requests, useful for third-party clients  - deny:   always denies grant requests, useful for black-listed clients

        :param grant_method: The grant_method of this V1OAuthClient.
        :type: str
        """

        self._grant_method = grant_method

    @property
    def kind(self):
        """
        Gets the kind of this V1OAuthClient.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1OAuthClient.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1OAuthClient.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1OAuthClient.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1OAuthClient.
        Standard object's metadata.

        :return: The metadata of this V1OAuthClient.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1OAuthClient.
        Standard object's metadata.

        :param metadata: The metadata of this V1OAuthClient.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def redirect_ur_is(self):
        """
        Gets the redirect_ur_is of this V1OAuthClient.
        RedirectURIs is the valid redirection URIs associated with a client

        :return: The redirect_ur_is of this V1OAuthClient.
        :rtype: list[str]
        """
        return self._redirect_ur_is

    @redirect_ur_is.setter
    def redirect_ur_is(self, redirect_ur_is):
        """
        Sets the redirect_ur_is of this V1OAuthClient.
        RedirectURIs is the valid redirection URIs associated with a client

        :param redirect_ur_is: The redirect_ur_is of this V1OAuthClient.
        :type: list[str]
        """

        self._redirect_ur_is = redirect_ur_is

    @property
    def respond_with_challenges(self):
        """
        Gets the respond_with_challenges of this V1OAuthClient.
        RespondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects

        :return: The respond_with_challenges of this V1OAuthClient.
        :rtype: bool
        """
        return self._respond_with_challenges

    @respond_with_challenges.setter
    def respond_with_challenges(self, respond_with_challenges):
        """
        Sets the respond_with_challenges of this V1OAuthClient.
        RespondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects

        :param respond_with_challenges: The respond_with_challenges of this V1OAuthClient.
        :type: bool
        """

        self._respond_with_challenges = respond_with_challenges

    @property
    def scope_restrictions(self):
        """
        Gets the scope_restrictions of this V1OAuthClient.
        ScopeRestrictions describes which scopes this client can request.  Each requested scope is checked against each restriction.  If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.

        :return: The scope_restrictions of this V1OAuthClient.
        :rtype: list[V1ScopeRestriction]
        """
        return self._scope_restrictions

    @scope_restrictions.setter
    def scope_restrictions(self, scope_restrictions):
        """
        Sets the scope_restrictions of this V1OAuthClient.
        ScopeRestrictions describes which scopes this client can request.  Each requested scope is checked against each restriction.  If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.

        :param scope_restrictions: The scope_restrictions of this V1OAuthClient.
        :type: list[V1ScopeRestriction]
        """

        self._scope_restrictions = scope_restrictions

    @property
    def secret(self):
        """
        Gets the secret of this V1OAuthClient.
        Secret is the unique secret associated with a client

        :return: The secret of this V1OAuthClient.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1OAuthClient.
        Secret is the unique secret associated with a client

        :param secret: The secret of this V1OAuthClient.
        :type: str
        """

        self._secret = secret

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1OAuthClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other