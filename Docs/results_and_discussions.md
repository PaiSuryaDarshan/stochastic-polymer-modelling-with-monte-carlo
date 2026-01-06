# Results and Discussions

### Interpretation Based on the Shown Results Only

(See Cell 18-21, [Statistical_comparison.ipynb](../Notebook/Statistical_comparison.ipynb))

#### Are both methods “good”?

Yes — **both methods are internally consistent and behave sensibly**, but they are **good for different purposes**, as evidenced by the plots and tables shown.

### What the Metropolis Monte Carlo (TM) results show

From the TM plots and table:

- Both $R_g$ and end-to-end distance increase smoothly and monotonically with chain length $N$.
- Error bars grow with $N$, but the trends remain clear and stable.
- The fitted curves are smooth, and replicate variability (from earlier paired analyses) is small relative to the mean trend.
- The 3D polymer snapshot shows an extended, spatially explored conformation without obvious artefacts.

**Interpretation from these images:**

- TM produces a stable, reproducible equilibrium ensemble.
- The growth of $R_g$ and $R_{ee}$ with $N$ is consistent across runs.
- The method samples configurations that are relatively more extended.

From this alone, TM appears **well-suited for quantitative analysis of equilibrium polymer statistics**.

### What the Growth Sampling (GS) results show

From the GS plots and table:

- $R_g$ and end-to-end distance also increase monotonically with $N$.
- The trends are smooth and physically reasonable.
- The error bars are comparable in magnitude to TM for small $N$, but the mean values are consistently lower.
- The 3D polymer snapshot shows a visually plausible, compact random-walk–like structure.

**Interpretation from these images:**

- GS reliably generates valid self-avoiding polymer configurations.
- The method produces visually realistic and diverse conformations.
- However, the mean polymer size measures are systematically smaller than those from TM at the same $N$.

From the images alone, GS is **internally consistent but systematically shifted** toward more compact conformations.

### Are the methods equivalent?

No.

From the side-by-side comparison visible in the plots:

- TM and GS show the same qualitative trends.
- They differ quantitatively in both $R_g$ and end-to-end distance at all $N$.
- The difference grows with increasing chain length.

This indicates that the two methods sample **different effective ensembles**, even though both generate valid polymers.

### Advantages of each method (based only on the shown results)

#### Growth Sampling (GS)

**Advantages:**

- Produces independent polymer conformations.
- Generates visually diverse and intuitive polymer shapes.
- Simple, fast, and robust for generating example configurations.
- Suitable for qualitative exploration and small-chain studies.

**Limitations (as seen here):**

- Produces systematically smaller $R_g$ and end-to-end distances.
- Deviates increasingly from TM results as $N$ grows.

#### Metropolis Monte Carlo (TM)

**Advantages:**

- Produces larger $R_g$ and end-to-end distances consistently across $N$.
- Shows stable, smooth scaling behaviour.
- Results are reproducible across replicates.
- Better suited for extracting quantitative polymer statistics.

**Limitations (as seen here):**

- Individual configurations may look less visually “random” due to correlated sampling.
- Requires longer runs and careful sampling parameters.

### Final conclusion

- **Both GS and TM are valid polymer simulation methods.**
- GS is best viewed as a **qualitative and exploratory tool**.
- TM is better suited for **quantitative equilibrium analysis**.
- The observed differences are systematic, reproducible, and increase with chain length, indicating that the choice of method materially affects the measured polymer properties.

## Interpretation of the Mean Difference in Radius of Gyration Across Replicates

(See Cell 24, [Statistical_comparison.ipynb](../Notebook/Statistical_comparison.ipynb))

The plot shows the difference in the mean radius of gyration, $\Delta R_g = R_g^{\mathrm{GS}} - R_g^{\mathrm{TM}}$, as a function of chain length $N$ across multiple independent replicates. Individual replicate trajectories are shown as faint lines, while the bold line represents the average difference over all replicates.

For all values of $N$, $\Delta R_g$ remains negative, indicating that growth sampling systematically underestimates the radius of gyration relative to Metropolis Monte Carlo. The absence of any crossings of the zero line across replicates confirms that this discrepancy is not due to stochastic variability.

Moreover, the magnitude of the negative difference increases approximately monotonically with increasing $N$. This trend demonstrates that the bias introduced by growth sampling accumulates with chain length, consistent with a growth-induced distortion of the polymer conformational ensemble.

The relatively small spread between replicate trajectories compared to the overall downward trend indicates that the observed behaviour is robust and reproducible. Variations between replicates are minor compared to the systematic shift, reinforcing the conclusion that the difference arises from algorithmic bias rather than finite-sample noise.

## Interpretation of Bootstrap Confidence Intervals

(See Cell 26, [Statistical_comparison.ipynb](../Notebook/Statistical_comparison.ipynb))

The bootstrap confidence intervals provide information beyond the previously observed mean trends and scaling exponents.

First, for every chain length $N$, the 95% confidence intervals for the mean differences $\Delta R*g = R_g^{\mathrm{GS}} - R_g^{\mathrm{TM}}$ and $\Delta R*{ee} = R*{ee}^{\mathrm{GS}} - R*{ee}^{\mathrm{TM}}$ lie entirely below zero. This demonstrates that the discrepancies between growth sampling and Metropolis Monte Carlo are **statistically decisive**, ruling out the possibility that the observed differences arise from finite-sample noise.

Second, the magnitude of the negative mean differences increases monotonically with $N$. This shows that the bias introduced by growth sampling is **not constant**, but instead **accumulates with chain length**, which is characteristic of a growth-induced attrition bias affecting asymptotic polymer behaviour.

Third, the widths of the confidence intervals remain relatively narrow as $N$ increases. This indicates that the growing discrepancy is **not driven by increasing statistical uncertainty** at larger chain lengths, but reflects a genuine, systematic distortion of the sampled conformational ensemble.

Finally, the absolute magnitude of $\Delta R\_{ee}$ is consistently larger than that of $\Delta R_g$, indicating that the end-to-end distance is a more sensitive diagnostic of the growth-sampling bias than the radius of gyration. This suggests that growth sampling preferentially suppresses long-range chain extension rather than uniformly rescaling overall polymer size.

## Interpretation of the Scaling Fit

(See Cell 33, [Statistical_comparison.ipynb](../Notebook/Statistical_comparison.ipynb))

The most conclusive test was the scaling component log-log fit .

For each replicate, the scaling exponent $\nu$ was obtained by fitting $\langle R_g \rangle \sim N^{\nu}$ on log–log axes.

The resulting distributions of fitted exponents are shown. Growth sampling consistently yields smaller $\nu$ values than Metropolis Monte Carlo, indicating a systematic bias in the sampled conformational ensemble.”

The systematically smaller scaling exponent $\nu$ obtained from growth sampling indicates a bias toward more compact polymer conformations. Since $\nu$ characterises the global swelling behaviour of the chain, a consistent downward shift across replicates reflects a distortion of the equilibrium conformational ensemble rather than statistical noise. This bias originates from the growth-based construction, where early local choices constrain future configurations and trapped chains are discarded, leading to unequal sampling of self-avoiding walks. In contrast, Metropolis Monte Carlo samples complete configurations with correct equilibrium weights, yielding a larger and more accurate $\nu$.

A smaller $\nu$ is a sign of systematic bias because it means the algorithm consistently produces polymers that are too compact compared to the true equilibrium ensemble.

To further confirm, Kernel density estimates corroborate the histogram-based comparison, showing two well-separated, unimodal distributions of fitted scaling exponents. The absence of significant overlap confirms that the observed difference between GS and TM is systematic rather than an artefact of binning or statistical noise.

# Final verdict

see conclusion.md
