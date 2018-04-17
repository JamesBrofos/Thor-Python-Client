import numpy as np
from thor_client import ThorClient
from levy import levy as obj


# Create experiment.
tc = ThorClient()
name = "Levy"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": -10., "high": 10.},
    {"name": "x2", "dim_type": "linear", "low": -10., "high": 10.},
    {"name": "x3", "dim_type": "linear", "low": -10., "high": 10.},
    {"name": "x4", "dim_type": "linear", "low": -10., "high": 10.},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = obj(np.array([x["x1"], x["x2"], x["x3"], x["x4"]]))
    # Submit recommendation.
    rec.submit_recommendation(val)
