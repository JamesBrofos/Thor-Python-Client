import numpy as np
from thor_client import ThorClient
from lda_on_grid import lda_on_grid


# Authentication token.
auth_token = "$2b$12$.wA/rDDnUeNFoXOxBcJ6ze2ZzIF16ThQMM8hPfvuTwtTwZYVDlpXK"

# Create experiment.
tc = ThorClient(auth_token)
name = "Latent Dirichlet Allocation (LDA)"
# Create space.
dims = [
    {"name": "kappa", "dim_type": "integer", "low": 0, "high": 5},
    {"name": "tau", "dim_type": "integer", "low": 0, "high": 5},
    {"name": "S", "dim_type": "integer", "low": 0, "high": 7},
]
exp = tc.create_experiment(name, dims)

# Main optimization loop.
for i in range(100):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = -lda_on_grid(x["kappa"], x["tau"], x["S"])
    # Submit recommendation.
    rec.submit_recommendation(val)


