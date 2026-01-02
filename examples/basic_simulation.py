import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from seven_books import model_parable, plot_trajectory


def main():
# Initial state: low activation, moderate dwelling
y0 = [0.2, 0.1, 0.15, 0.6]

# Time span
t = np.linspace(0, 50, 500)

# Simulate with intervention at t=25
intervention_time = 25
sol = odeint(
lambda y, t: model_parable(y, t, nudge_time=intervention_time),
y0, t
)

# Plot
fig = plot_trajectory(t, sol, intervention_time)
plt.savefig('basic_simulation.png', dpi=300, bbox_inches='tight')
plt.show()

# Print final states
print("Final states:")
print(f" Facet 1: {sol[-1, 0]:.4f}")
print(f" Facet 2: {sol[-1, 1]:.4f}")
print(f" Facet 3: {sol[-1, 2]:.4f}")
print(f" Dwelling: {sol[-1, 3]:.4f}")
print(f" Coherence: {np.mean(sol[-1, :3]):.4f}")


if __name__ == "__main__":
main()
```

-----

