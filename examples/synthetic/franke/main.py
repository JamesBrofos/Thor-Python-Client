import numpy as np
from thor_client import ThorClient
from franke import franke as obj


# Create experiment.
tc = ThorClient()
name = "Franke Function"
# Create space.
dims = [
    {"name": "x", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "y", "dim_type": "linear", "low": 0., "high": 1.}
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(8):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = obj(np.array([x["x"], x["y"]]))
    # Submit recommendation.
    rec.submit_recommendation(val)