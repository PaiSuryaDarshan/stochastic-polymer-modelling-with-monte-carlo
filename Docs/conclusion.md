## Conclusion

<h3> Final Verdict : Growth Sampling (GS) vs. Metropolis Monte Carlo (TM)</h3>

Based on the results presented above, both Growth Sampling (GS) and Metropolis Monte Carlo (TM) produce valid self-avoiding polymer configurations and exhibit physically sensible trends in polymer size measures. However, the analyses demonstrate that the two methods are **not equivalent in the ensembles they sample**, and their differences have clear quantitative consequences.

At first inspection, GS produces polymer conformations that appear visually diverse and intuitively “random,” owing to the independent generation of each chain. In contrast, individual TM configurations may appear less visually varied due to correlated sampling. The results show, however, that visual appearance alone is not a reliable indicator of statistical behaviour.

Across all chain lengths studied, GS systematically yields smaller mean values of both the radius of gyration and the end-to-end distance compared to TM. Paired replicate analysis shows that these differences are consistent across runs and increase monotonically with chain length. Bootstrap confidence intervals further confirm that the discrepancies are statistically decisive and not attributable to finite-sample noise.

The scaling analysis provides the most conclusive evidence of nonequivalence. Fits of $\langle R_g \rangle \sim N^{\nu}$ performed independently for each replicate show that GS consistently produces smaller values of the scaling exponent $\nu$ than TM. Kernel density estimates reveal two well-separated, unimodal distributions of fitted exponents, indicating a systematic shift rather than overlap due to uncertainty. This demonstrates that GS samples an ensemble biased toward more compact polymer conformations.

From the results alone, TM exhibits stable, reproducible scaling behaviour and larger characteristic polymer sizes at all $N$, making it better suited for quantitative analysis of equilibrium polymer statistics. GS, while internally consistent and computationally efficient, is best interpreted as a qualitative or exploratory method whose results deviate increasingly from TM as chain length grows.

### Overall Assessment

- **Growth Sampling (GS)**

  - Produces independent and visually diverse polymer conformations
  - Simple and efficient for generating example configurations
  - Systematically underestimates polymer size measures and scaling behaviour

- **Metropolis Monte Carlo (TM)**
  - Produces correlated but reproducible configurations
  - Yields consistently larger $R_g$, $R_{ee}$, and scaling exponents
  - Provides more reliable quantitative characterisation of polymer statistics

In conclusion, both methods are valid within their respective scopes, but they sample **different effective ensembles**. For equilibrium polymer properties such as radius of gyration, end-to-end distance, and scaling behaviour, Metropolis Monte Carlo provides the more accurate representation of the sampled conformational statistics, while Growth Sampling is better suited for qualitative illustration and rapid exploration.
