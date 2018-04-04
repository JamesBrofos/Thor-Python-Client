from thor_client import ThorClient
from svm_on_grid import svm_on_grid


# Create experiment.
tc = ThorClient()
name = "Structured SVM"
# Create space.
dims = [
    {"name": "C", "dim_type": "integer", "low": 0, "high": 24},
    {"name": "alpha", "dim_type": "integer", "low": 0, "high": 13},
    {"name": "epsilon", "dim_type": "integer", "low": 0, "high": 3},
]
exp = tc.create_experiment(name, dims, overwrite=True)

# Main optimization loop.
for i in range(100):
    # Request new recommendation.
    rec = exp.create_recommendation()
    x = rec.config
    # Evaluate new recommendation.
    val = -svm_on_grid(x["C"], x["alpha"], x["epsilon"])
    # Submit recommendation.
    rec.submit_recommendation(val)
