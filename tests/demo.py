from reliability_extension.Repairable_systems import optimal_replacement_time
from reliability_extension.Distributions import Normal_Distribution, Weibull_Distribution, Lognormal_Distribution, Exponential_Distribution, Gamma_Distribution, Beta_Distribution, Loglogistic_Distribution, Gumbel_Distribution, Competing_Risks_Model, Mixture_Model
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose


from reliability_extension.Fitters import Fit_Weibull_DS


f = [520, 740, 100, 17, 730, 764, 784, 760, 780, 779, 657, 765,500,600,459,800,]*10
rc = [3961, 4007, 4734, 6054, 7298, 10190, 23060, 27160, 28690, 37100, 40060, 45670,
      53000, 67000, 69630, 77350, 78470, 91680, 105700, 106300, 150400]*20
model_res=Fit_Weibull_DS(failures=f, right_censored=rc,show_probability_plot=False,
                            print_results=False)
model_res.distribution.HF(show_plot=True,input_type='runtime')
#model_res.distribution.HF(show_plot=True)
print(model_res.distribution)
print(model_res.distribution.name)

plt.show()




