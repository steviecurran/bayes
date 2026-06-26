## Bayesian Test Probability Calculator

A simple Python notebook demonstrating Bayesian inference for diagnostic-style testing problems with an updatable prior.

The project calculates the probability that a condition is truly present after one or more positive or negative test results, given:

- prior probability / prevalence
- true positive rate / sensitivity
- false positive rate
- sequential test outcomes

This is a compact demonstration of conditional probability, Bayes' theorem and iterative belief updating.

### Example

For a test with:

- True positive rate: 99%
- False positive rate: 2%
- Prevalence: 0.1%

A single positive result gives a posterior probability of approximately 4.7%.

A second positive test increases this to approximately 71%, while a subsequent negative result reduces the probability substantially.

### Important caveat

This example assumes the prior probability is based only on population prevalence. In real clinical settings, symptoms, exposure history and other evidence would change the prior probability before any test result is considered.
