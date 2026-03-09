# Bayes' Test

Test positive for that nasty dose of something? Well fear not, here's a simple Bayesian test to see if you actually have it! 

It will update the prior for subsequent positive or negative results. The calculation isn't hard but is easy to screw up, hence the code.

E.g. the classic medical testing problem - if the true positive rate is 99% and the false positive rate is 2% and you test positive, the news doesn't appear that good. 

But if only 0.1% of the population have the disease, there's only a 4.7% chance you actually have it, so not that bad<sup>*</sup> (a second positive test will put this at 71% and a negative test at 0.051%).

<sup>*</sup>Something that's never pointed out, as far as I know, is that this assumes that you don't exhibit symptoms specific to the ailment in question. Still good for spotting an unfair coin though!

