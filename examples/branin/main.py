import numpy as np
from thor_client import ThorClient
from branin import branin_hoo


# Authentication token.
auth_token = "YOUR_AUTH_TOKEN"

# Create experiment.
tc = ThorClient(auth_token)
name = "Branin-Hoo"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": -5., "high": 10.},
    {"name": "x2", "dim_type": "linear", "low": 0., "high": 15.},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = -branin_hoo(np.array([x["x1"], x["x2"]]))
    # Submit recommendation.
    rec.submit_recommendation(val)


