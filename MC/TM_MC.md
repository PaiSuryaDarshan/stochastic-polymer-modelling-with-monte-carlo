# True Metropolis Monte Carlo Simulation

## Why It’s Not “Metropolis MC” (the Important Difference)

**Metropolis Monte Carlo (MC)** is defined as a **Markov chain over complete configurations**.

In Metropolis MC, the procedure is:

1. Start from a valid configuration \( X \).
2. Propose a new configuration \( X' \) using a stochastic move.
3. Accept the proposal with probability:
   
   $$
   P_{\text{acc}} = \min\!\left(
   1,
   \frac{\pi(X')\,q(X \mid X')}{\pi(X)\,q(X' \mid X)}
   \right)
   $$

   where:
   - \( \pi(X) \) is the target distribution,
   - \( q(X' \mid X) \) is the proposal probability.

For **Boltzmann sampling**, the target distribution is:
\[
\pi(X) \propto e^{-\beta E(X)}
\]

If the proposal distribution \( q \) is symmetric, this reduces to:
\[
P_{\text{acc}} = \min\!\left(1, e^{-\beta \Delta E}\right)
\]

---

## What Happens in `GS.MC.md` Instead

What happens in `GS.MC.md` is **growth-based sampling** rather than Metropolis sampling:

- The polymer is **built step-by-step** from one end.
- At each step, a randomly chosen local move is attempted.
- If the walk becomes trapped (no valid continuation), the **entire chain is discarded and restarted**.

---

## Consequences of Growth Sampling

This approach leads to two fundamental differences from Metropolis MC:

### 1. No Markov Chain Over Full Configurations
The algorithm does not propose modifications to an already complete polymer configuration. Instead, configurations are constructed incrementally from scratch. As a result, there is no Markov chain whose state space consists of full-length self-avoiding walks.

### 2. Sampling Bias
Different self-avoiding walks are **not sampled with equal probability**. Early branching decisions strongly constrain later growth, and configurations that are difficult to complete are disproportionately rejected through restarts. This introduces a bias toward walks that are easier to grow, rather than uniformly sampling the space of all valid SAWs.

---

## Summary

- **Monte Carlo?** Yes — randomness and ensemble averaging are present.
- **Metropolis Monte Carlo?** No — there is no Markov chain, no acceptance–rejection step based on a target distribution, and no guarantee of unbiased equilibrium sampling.

The method implemented in `GS.MC.md` is therefore best described as a **stochastic growth Monte Carlo algorithm**, not a Metropolis Monte Carlo simulation.
