import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from seven_books import model_parable


def main():
y0 = [0.2, 0.1, 0.15, 0.6]
t = np.linspace(0, 50, 500)

# No intervention
sol_none = odeint(model_parable, y0, t)

# Early intervention (t=10)
sol_early = odeint(
lambda y, t: model_parable(y, t, nudge_time=10),
y0, t
)

# Right timing (t=25)
sol_right = odeint(
lambda y, t: model_parable(y, t, nudge_time=25),
y0, t
)

# Late intervention (t=40)
sol_late = odeint(
lambda y, t: model_parable(y, t, nudge_time=40),
y0, t
)

# Plot coherence for all
fig, ax = plt.subplots(figsize=(12, 6))

coherence_none = np.mean(sol_none[:, :3], axis=1)
coherence_early = np.mean(sol_early[:, :3], axis=1)
coherence_right = np.mean(sol_right[:, :3], axis=1)
coherence_late = np.mean(sol_late[:, :3], axis=1)

ax.plot(t, coherence_none, label='No Intervention',
linewidth=2.5, linestyle='--', color='gray')
ax.plot(t, coherence_early, label='Early (t=10)',
linewidth=2.5, alpha=0.7)
ax.plot(t, coherence_right, label='Right Timing (t=25)',
linewidth=3, color='darkgoldenrod')
ax.plot(t, coherence_late, label='Late (t=40)',
linewidth=2.5, alpha=0.7)

ax.axvline(x=10, color='C1', linestyle=':', alpha=0.5
```

