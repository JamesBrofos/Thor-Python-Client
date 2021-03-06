from thor_client import ThorClient
from lda_on_grid import lda_on_grid


# Create experiment.
tc = ThorClient()
name = "Latent Dirichlet Allocation (LDA)"
# Create space.
dims = [
    {"name": "kappa", "dim_type": "integer", "low": 0, "high": 5},
    {"name": "tau", "dim_type": "integer", "low": 0, "high": 5},
    {"name": "S", "dim_type": "integer", "low": 0, "high": 7},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(50):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = -lda_on_grid(x["kappa"], x["tau"], x["S"])
    # Submit recommendation.
    rec.submit_recommendation(val)
