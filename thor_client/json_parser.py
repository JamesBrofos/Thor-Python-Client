import json


def json_parser(result, auth_token, cls=None):
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
