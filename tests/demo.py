from reliability_extension.Repairable_systems import optimal_replacement_time
import matplotlib.pyplot as plt
from numpy.testing import assert_allclose

ORT=optimal_replacement_time(cost_PM=1, cost_CM=5, weibull_alpha=1000,
                             weibull_beta=2.5,q=0,unit_year=365000)
print(ORT.optimal_reactive_ratio)
print(ORT.yearly_optimal_ratio)
print(ORT.ORT)



plt.show()

atol = 1e-8
rtol = 1e-7
ort0 = optimal_replacement_time(cost_PM=1, cost_CM=5, weibull_alpha=1000,
        weibull_beta=2.5, q=0)
assert_allclose(ort0.ORT,493.1851185118512,rtol=rtol,atol=atol)
assert_allclose(ort0.min_cost, 0.0034620429189943167, rtol=rtol, atol=atol)
ort1 = optimal_replacement_time(cost_PM=1, cost_CM=5, weibull_alpha=1000,
        weibull_beta=2.5, q=1)
assert_allclose(ort1.ORT,1618.644582767346,rtol=rtol,atol=atol)
assert_allclose(ort1.min_cost, 0.0051483404213951, rtol=rtol, atol=atol)

