import numpy as np
from thor_client import ThorClient
from branin import branin_hoo as obj


# Create experiment.
tc = ThorClient()
name = "Branin-Hoo (Distributed)"
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": -5., "high": 10.},
    {"name": "x2", "dim_type": "linear", "low": 0., "high": 15.},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(200):
    # Request new recommendation.
    recs = [exp.create_recommendation() for _ in range(5)]
    for r in recs:
        x = r.config
        # Evaluate new recommendation.
        val = obj(np.array([x["x1"], x["x2"]]))
        # Submit recommendation.
        r.submit_recommendation(val)
