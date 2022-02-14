from reliability_extension.Repairable_systems import optimal_replacement_time
import matplotlib.pyplot as plt
ORT=optimal_replacement_time(cost_PM=1, cost_CM=5, weibull_alpha=1000,
                             weibull_beta=2.5,q=0,unit_year=365000)
print(ORT.optimal_reactive_ratio)
print(ORT.yearly_optimal_ratio)

plt.show()

