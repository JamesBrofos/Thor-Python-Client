from .config import auth_token, base_url
from .experiment_client import ExperimentClient
from .json_parser import json_parser

import requests


class ThorClient(object):
    """Thor Client Class

    The purpose of this module is to allow Python users to utilize the Thor
    utility for Bayesian optimization of machine learning systems. This module
    in particular is intended to properly authenticate with Thor and to create
    experiments.

    Parameters:
        auth_token (str): String containing a user's specific API key provided
            by the Thor server. This is used to authenticate with the Thor
            server as a handshake that these experiments belong to a user and
            can be viewed and edited by them.
        base_url (str): String indicating the URL template for API calls.

    Examples:
        The Thor Client can be used to create experiments as follows:

        >>> tc = ThorClient("YOUR_API_KEY")
        >>> dims = [{"name": "x", "dim_type": "linear", "low": 0., "high": 1.}]
        >>> exp = tc.create_experiment("YOUR_EXPERIMENT_NAME", dims)

        Alternatively, the Thor Client can be used to query for existing
        experiments.

        >>> exp = tc.experiment_for_name("YOUR_EXISTING_EXPERIMENT")
    """
    def __init__(self, auth_token=auth_token, base_url=base_url):
        """Initialize the parameters of the Thor API client."""
        assert isinstance(auth_token, str)
        self.auth_token = auth_token
        self.base_url = base_url

    def create_experiment(
            self,
            name,
            dimensions,
            overwrite=False
    ):
        """Create an experiment.

        Parameters:
            name (str): String containing the name of the experiment to create.
            dimensions (list of dictionaries): A list of dictionaries that
                specify the hyperparameters of the machine learning system. Each
                dimension must specify the following four properties:
                    1. The name of the dimension, which key "name".
                    2. The type of dimension to create, which must be one of
                       "linear", "exponential", "logarithmic", or "integer".
                        This is specified by the key "dim_type".
                    3. The minimum value of the dimension, specified by the key
                       "low".
                    4. The maximum value of the dimension, specified by the key
                       "high".
            overwrite (optional, bool): An indicator variable which will
                overwrite existing experiments with the given name if they
                already exist on Thor Server.

        Returns:
            ExperimentClient: A corresponding experiment with the provided name
                and dimensions.
        """
        assert isinstance(name, str)
        assert isinstance(dimensions, list) or isinstance(dimensions, dict)
        if isinstance(dimensions, list):
            for dim in dimensions:
                assert isinstance(dim["name"], str)
                assert dim["dim_type"] in (
                    "linear", "logarithmic", "exponential", "integer"
                )

        post_data = {
            "name": name,
            "auth_token": self.auth_token,
            "dimensions": dimensions,
            "overwrite": overwrite
        }
        result = requests.post(
            url=self.base_url.format("create_experiment"),
            json=post_data
        )
        return json_parser(result, self.auth_token, ExperimentClient)

    def experiment_for_name(self, name):
        """Get an experiment with a given name.

        Parameters:
            name (str): String containing the name of the experiment that should
                be obtained.

        Returns:
            ExperimentClient: A corresponding experiment with the provided name.
                The object returned by this method is identical in functionality
                to the object that is returned by the function
                `create_experiment`.
        """
        assert isinstance(name, str)
        post_data = {"name": name, "auth_token": self.auth_token}
        result = requests.post(
            url=self.base_url.format("experiment_for_name"),
            json=post_data
        )
        return json_parser(result, self.auth_token, ExperimentClient)

    def for_name_or_create(self, name, dimensions):
        """Query for an experiment and return it if it exists. Otherwise, if the
        experiment does not exist, create it.

        Parameters:
            name (str): String containing the name of the experiment to create.
            dimensions (list of dictionaries): A list of dictionaries that
                specify the hyperparameters of the machine learning system. Each
                dimension must specify the following four properties:
                    1. The name of the dimension, which key "name".
                    2. The type of dimension to create, which must be one of
                       "linear", "exponential", "logarithmic", or "integer".
                        This is specified by the key "dim_type".
                    3. The minimum value of the dimension, specified by the key
                       "low".
                    4. The maximum value of the dimension, specified by the key
                       "high".
            acq_func (optional, str): A string containing the name of the
                acquisition function to use. This can be one of "hedge",
                "upper_confidence_bound", "expected_improvement", or
                "improvement_probability".
            overwrite (optional, bool): An indicator variable which will
                overwrite existing experiments with the given name if they
                already exist on Thor Server.

        Returns:
            ExperimentClient: A corresponding experiment with the provided name
                and dimensions.
        """
        try:
            return self.experiment_for_name(name)
        except ValueError:
            return self.create_experiment(name, dimensions)
