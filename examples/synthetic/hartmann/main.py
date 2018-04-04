import numpy as np
from thor_client import ThorClient
from hartmann import hartmann_6


# Create experiment.
tc = ThorClient()
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
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(100):
    # Request new recommendation.
    acq_func = "expected_improvement" if i < 50 else "improvement_probability"
    rec = exp.create_recommendation(acq_func=acq_func)
    x = rec.config
    # Evaluate new recommendation.
    val = -hartmann_6(np.array([
        x["x1"], x["x2"], x["x3"], x["x4"], x["x5"], x["x6"]
    ]))
    # Submit recommendation.
    rec.submit_recommendation(val)
