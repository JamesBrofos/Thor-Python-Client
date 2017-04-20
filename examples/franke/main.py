import numpy as np
from thor_client import ThorClient
from thor.evaluation import franke


# Authentication token.
auth_token = "YOUR_AUTH_TOKEN"

# Create experiment.
tc = ThorClient(auth_token)
name = "Franke Function"
# Create space.
dims = [
    {"name": "x", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "y", "dim_type": "linear", "low": 0., "high": 1.}
]
exp = tc.create_experiment(name, dims)

# Main optimization loop.
for i in range(30):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = franke(np.array([x["x"], x["y"]]))
    # Submit recommendation.
    rec.submit_recommendation(val)

