# Lesson 2 - Kalman Filters
#### - kalman filter takes observations with noise and uncertainty and estimates automatically state

## Tracking Intro: Used to estimate the state of a system
### Kalman Filter: Continuous & uni-modal

#### - Measurement update is product related / Bayes rule
#### - Motion update is convolution related / total probability
##### -- Feedback loop combining Measurement cycle and prediction cycle with gausian distributions
##### -- The new belief will be more certain than either the previous belief OR the measurement: more measurements means greater certainty
#### - Parameter Update: multiply two gausians using Bayes Rule
##### -- New mean is weighted sum of old means (normalized): 
##### --- mu_new = (mu_prior * var_measurement + var_prior * mu_measurement) / (var_measurement + var_prior)
##### -- New variance is combined similar to resistors in parallel (smaller value)
##### --- var_new = 1 / ((1/var_prior) + (1/var_measurement))

####
### Monte Carlo Localization: Discrete & multi-modal

####
### Particle Filter: Continuous & multi-modal 
