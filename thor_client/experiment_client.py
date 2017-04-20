import requests
import json
from .base_url import base_url
from .recommendation_client import RecommendationClient
from .json_parser import json_parser


class ExperimentClient(object):
    """Experiment Client Class"""
    def __init__(self, identifier, name, date, dims, auth_token):
        """Initialize parameters of the experiment client object."""
        self.experiment_id = identifier
        self.name = name
        self.date = date
        self.dims = dims
        self.auth_token = auth_token

    def submit_observation(self, config, target):
        """Upload a pairing of a configuration alongside an observed target
        variable.
        """
        post_data = {
            "auth_token": self.auth_token,
            "experiment_id": self.experiment_id,
            "configuration": json.dumps(config),
            "target": target
        }
        result = requests.post(
            url=base_url.format("submit_observation"),
            json=post_data
        )
        return json_parser(result, self.auth_token)

    def create_recommendation(self, rand_prob=None, n_model_iters=None):
        """Get a recommendation for a point to evaluate next."""
        post_data = {
            "auth_token": self.auth_token,
            "experiment_id": self.experiment_id,
            "n_model_iters": n_model_iters,
            "rand_prob": rand_prob
        }
        result = requests.post(
            url=base_url.format("create_recommendation"),
            json=post_data
        )
        return json_parser(result, self.auth_token, RecommendationClient)

    def best_configuration(self):
        """Get the configuration of parameters that produced the best value of
        the objective function.
        """
        post_data = {
            "auth_token": self.auth_token,
            "experiment_id": self.experiment_id
        }
        result = requests.post(
            url=base_url.format("best_configuration"),
            json=post_data
        )
        return json_parser(result, self.auth_token)

    def pending_recommendations(self):
        """Query for pending recommendations that have yet to be evaluated."""
        post_data = {
            "auth_token": self.auth_token,
            "experiment_id": self.experiment_id
        }
        result = requests.post(
            url=base_url.format("pending_recommendations"),
            json=post_data
        )
        return json_parser(result, self.auth_token, RecommendationClient)

    @classmethod
    def from_dict(cls, dictionary, auth_token):
        """Create an experiment object from a dictionary representation. Pass
        the authentication token as an additional parameter.

        TODO: Can the authentication token be a return parameter?
        """
        return cls(
            identifier=dictionary["id"],
            name=dictionary["name"],
            date=dictionary["date"],
            dims=dictionary["dimensions"],
            auth_token=auth_token
        )


