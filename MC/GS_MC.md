# Growth Sampling Monte Carlo (A workaround)

## Why is this Monte Carlo?

**Monte Carlo (MC)** = Methods estimating expectations by **random sampling**.

The GS_monte_carlo.py code satisfies this definition in all essential aspects:

### 1. Randomness
You explicitly use a random number generator (`np.random.default_rng`) and randomize trial directions at each step of the walk construction. This introduces stochasticity into the generation of configurations.

### 2. Sampling of Configurations
Each execution of the growth procedure produces a **random polymer conformation**, specifically a **self-avoiding walk (SAW)** on a cubic lattice. Each completed chain represents one sampled configuration from the space of allowed walks.

### 3. Ensemble Averaging
You generate many independent chains and compute statistical observables—such as the radius of gyration and end-to-end distance—by averaging over the ensemble of sampled configurations.

Formally, it is estimating an expectation value of an observable \( A \) as:

\[
\langle A \rangle \;\approx\; \frac{1}{M} \sum_{k=1}^{M} A\!\left(\mathbf{R}^{(k)}\right)
\]

where:
- \( M \) is the number of sampled chains,
- \( \mathbf{R}^{(k)} \) is the \( k \)-th randomly generated polymer configuration.

### Conclusion
Because your observables are computed as **statistical averages over randomly generated configurations**, your approach **does qualify as Monte Carlo sampling** in the standard statistical-physics sense.

It is therefore correct to describe your simulation as a **Monte Carlo simulation of self-avoiding polymer chains**, even though it is not a Metropolis–Hastings or equilibrium Markov-chain Monte Carlo method.
