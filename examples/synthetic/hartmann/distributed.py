import numpy as np
from thor_client import ThorClient
from hartmann import hartmann_6 as obj


# Create experiment.
tc = ThorClient()
# A boolean variable to determine whether or not we should use an integrated
# acquisition function.
integrated = False
# Create space.
dims = [
    {"name": "x1", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x2", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x3", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x4", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x5", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "x6", "dim_type": "linear", "low": 0., "high": 1.},
]
name = "Hartmann 6-D (Integrated - {})".format(integrated)
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(100):
    # Request new recommendation.
    if integrated:
        recs = [exp.create_recommendation() for _ in range(5)]
    else:
        recs = exp.create_recommendation(integrate_acq=False)
    for r in recs:
        x = r.config
        # Evaluate new recommendation.
        val = obj(np.array([
            x["x1"], x["x2"], x["x3"], x["x4"], x["x5"], x["x6"]
        ]))
        # Submit recommendation.
        r.submit_recommendation(val)

