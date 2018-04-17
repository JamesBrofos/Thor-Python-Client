import numpy as np
from thor_client import ThorClient
from michalewicz import michalewicz as obj


# Create experiment.
tc = ThorClient()
name = "Michalewicz Function"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x2", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x3", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x4", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x5", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x6", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x7", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x8", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x9", "dim_type": "linear", "low": 0., "high": np.pi},
    {"name": "x10", "dim_type": "linear", "low": 0., "high": np.pi},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = obj(np.array([
        x["x1"],
        x["x2"],
        x["x3"],
        x["x4"],
        x["x5"],
        x["x6"],
        x["x7"],
        x["x8"],
        x["x9"],
        x["x10"]
    ]))
    # Submit recommendation.
    rec.submit_recommendation(val)
