import json


def json_parser(result, auth_token, cls=None):
    """JSON Parser Method

    This method transforms JSON data into usable Python objects, if required and
    generally checks for errors. Moreover, in the case that the desired Python
    object requires an authentication token, this function provides that to the
    constructor as well.

    Parameters:
        result (HTTP request object): This object will be returned by the
            `requests` library when a POST request is made to the server. It
            will contain information about the status of the request (400
            indicating a failure mode) and the actual value that was returned,
            encapsulated as a JSON.
        auth_token (str): String containing a user's specific API key provided
            by the Thor server.
        cls Thor Python class (`ExperimentClient` or `RecommendationClient`): An
            object class representing the kind of object that should be created
            from the data contained in the JSON.

    Returns:
        Object of type `cls` or a list of objects of type `cls` or dictionary:
            If `cls` is provided and is not `None` then an object of type `cls`
            will be produced. If the JSON is a list, then a list of such `cls`
            objects will be produced. Otherwise, if `cls` is `None`, then
            instead the JSON data will be returned as a Python dictionary.

    Examples:
        The JSON parser method can be used to convert a response from Thor's
        server as follows:

        >>> import requests
        >>> result = requests.post(url=url.format("create_experiment"), json=data)
        >>> exp = json_parser(result, "YOUR_AUTH_TOKEN", ExperimentClient)

    Raises:
        ValueError: If the request was retrieved by a 400-code HTTP error, then
            a value error is produced.
    """
    json_data = json.loads(result.text)
    if result.status_code == 400:
        # Handle bad outcomes.
        raise ValueError(json_data["error"])
    else:
        if cls:
            if isinstance(json_data, list):
                return [cls.from_dict(d, auth_token) for d in json_data]
            else:
                return cls.from_dict(json_data, auth_token)
        else:
            return json_data
