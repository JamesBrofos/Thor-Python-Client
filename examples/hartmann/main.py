import numpy as np
from thor_client import ThorClient
from hartmann import hartmann_6


# Authentication token.
auth_token = "YOUR_AUTH_TOKEN"

# Create experiment.
tc = ThorClient(auth_token)
name = "Hartmann 6-D"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x2", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x3", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x4", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x5", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x6", "dim_type": "linear", "low": 0., "high": 1.},
]
exp = tc.create_experiment(name, dims)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = -hartmann_6(np.array([
        x["x1"], x["x2"], x["x3"], x["x4"], x["x5"], x["x6"]
    ]))
    # Submit recommendation.
    rec.submit_recommendation(val)


