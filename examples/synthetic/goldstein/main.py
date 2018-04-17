import numpy as np
from thor_client import ThorClient
from goldstein import goldstein as obj


# Create experiment.
tc = ThorClient()
name = "Goldstein-Price"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": -2., "high": 2.},
    {"name": "x2", "dim_type": "linear", "low": -2., "high": 2.},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = obj(np.array([x["x1"], x["x2"]]))
    # Submit recommendation.
    rec.submit_recommendation(val)
