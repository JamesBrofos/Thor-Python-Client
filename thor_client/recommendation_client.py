import requests
import json
from .config import auth_token, base_url
from .json_parser import json_parser


class RecommendationClient(object):
    """Thor Recommendation Client Class

    The purpose of this class is to provide an interface for interacting with
    suggestions provided by the Thor API. In particular, once a recommendation
    is received, it will be evaluated by the client's local computer. After
    this, its value as a configuration will be transmitted back to the Thor
    server.

    Parameters:
        identifier (int): An integer identifier for this recommendation. This
            allows the Thor server to identify which recommendation was
            associated with a given value of the metric on the client side.
        config (dictionary): A dictionary containing the recommended parameter
            values for each dimension of the optimization problem.
        auth_token (str): String containing a user's specific API key provided
            by the Thor server.
        base_url (str): String indicating the URL template for API calls.
        description (str, optional): Optional text describing a particular
            observation/recommendation.

    Examples:
        The recommendation client sends metric values back to the Thor server
        using a convenient API interface.

        >>> exp = tc.experiment_for_name("YOUR_EXPERIMENT_NAME")
        >>> rec = exp.create_recommendation()
        >>> rec.submit_recommendation(1.0)

        To add a description to a recommendation, pass it to
        create_recommendation().

        >>> exp = tc.experiment_for_name("YOUR_EXPERIMENT_NAME")
        >>> rec = exp.create_recommendation(description="run-123")
        >>> rec.submit_recommendation(1.0)
    """
    def __init__(self, identifier, config, auth_token=auth_token,
                 base_url=base_url, description=""):
        """Initialize the parameters of the recommendation client object."""
        self.recommendation_id = identifier
        self.config = config
        self.auth_token = auth_token
        self.base_url = base_url
        self.description = description

    def submit_recommendation(self, value):
        """Submit the returned metric value for a point that was recommended by
        the Bayesian optimization routine.

        Parameters:
            value (float): A number indicating the performance of this
                configuration of model parameters.

        Returns:
            dictionary: A dictionary containing the recommendation identifier
                and a boolean indicator that the recommendation was submitted.
        """
        assert isinstance(value, float)
        post_data = {
            "auth_token": self.auth_token,
            "recommendation_id": self.recommendation_id,
            "value": value
        }
        result = requests.post(
            url=self.base_url.format("submit_recommendation"),
            json=post_data
        )
        return json_parser(result, self.auth_token)

    @classmethod
    def from_dict(cls, dictionary, auth_token):
        """Convert a dictionary to a recommendation client object."""
        return cls(
            identifier=dictionary["id"],
            config=json.loads(dictionary["config"]),
            auth_token=auth_token,
            description=dictionary["description"]
        )
