```python
"""
Visualization utilities for the Seven Books Model.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory(t, sol, intervention_time=None, title="Seven Books Trajectory"):
"""
Plot the evolution of facets and dwelling field.

Parameters
----------
t : array
Time points
sol : array, shape (n_points, 4)
Solution array [x1, x2, x3, dwelling]
intervention_time : float or None
Time of catalytic nudge (if any)
title : str
Plot title
"""
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Facets
ax1.plot(t, sol[:, 0], label='Facet 1', linewidth=2, alpha=0.8)
ax1.plot(t, sol[:, 1], label='Facet 2', linewidth=2, alpha=0.8)
ax1.plot(t, sol[:, 2], label='Facet 3', linewidth=2, alpha=0.8)

if intervention_time is not None:
ax1.axvline(x=intervention_time, color='gold', linestyle=':',
linewidth=2, label='Grace')

ax1.set_ylabel('Facet Activation', fontsize=12)
ax1.set_title(title, fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_ylim([-0.05, 1.05])

# Dwelling and coherence
coherence = np.mean(sol[:, :3], axis=1)
ax2.plot(t, sol[:, 3], label='Dwelling Field', linewidth=2.5,
color='darkgoldenrod')
ax2.plot(t, coherence, label='Coherence (mean)', linewidth=2,
color='navy', linestyle='--')

if intervention_time is not None:
ax2.axvline(x=intervention_time, color='gold', linestyle=':', linewidth=2)

ax2.set_xlabel('Time', fontsize=12)
ax2.set_ylabel('Value', fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_ylim([-0.05, 1.05])

plt.tight_layout()
return fig


def plot_comparison(t, sol_without, sol_with, intervention_time):
"""
Compare trajectories with and without intervention.

Parameters
----------
t : array
Time points
sol_without : array
Solution without intervention
sol_with : array
Solution with intervention
intervention_time : float
Time of intervention
"""
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Coherence comparison
coherence_without = np.mean(sol_without[:, :3], axis=1)
coherence_with = np.mean(sol_with[:, :3], axis=1)

ax = axes[0, 0]
ax.plot(t, coherence_without, label='Without Grace', linewidth=2.5,
color='gray', linestyle='--')
ax.plot(t, coherence_with, label='With Grace', linewidth=2.5,
color='darkgoldenrod')
ax.axvline(x=intervention_time, color='gold', linestyle=':',
linewidth=2, alpha=0.7)
ax.set_xlabel('Time')
ax.set_ylabel('Coherence')
ax.set_title('The Grace Paradox', fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)

# Dwelling comparison
ax = axes[0, 1]
ax.plot(t, sol_without[:, 3], label='Without Grace', linewidth=2.5,
color='gray', linestyle='--')
ax.plot(t, sol_with[:, 3], label='With Grace', linewidth=2.5,
color='darkgoldenrod')
ax.axvline(x=intervention_time, color='gold', linestyle=':',
linewidth=2, alpha=0.7)
ax.set_xlabel('Time')
ax.set_ylabel('Dwelling')
ax.set_title('Dwelling Field Evolution', fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)

# Individual facets (with grace)
ax = axes[1, 0]
ax.plot(t, sol_with[:, 0], label='Facet 1', linewidth=2, alpha=0.8)
ax.plot(t, sol_with[:, 1], label='Facet 2', linewidth=2, alpha=0.8)
ax.plot(t, sol_with[:, 2], label='Facet 3', linewidth=2, alpha=0.8)
ax.axvline(x=intervention_time, color='gold', linestyle=':',
linewidth=2, alpha=0.7)
ax.set_xlabel('Time')
ax.set_ylabel('Activation')
ax.set_title('Facet Dynamics (With Grace)', fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)

# Phase space
ax = axes[1, 1]
ax.plot(sol_with[:, 0], sol_with[:, 1], linewidth=2.5,
color='darkgoldenrod', label='Trajectory')
ax.scatter(sol_with[0, 0], sol_with[0, 1], s=150, c='blue',
marker='o', edgecolors='black', linewidths=2,
label='Start', zorder=5)
ax.scatter(sol_with[-1, 0], sol_with[-1, 1], s=150, c='green',
marker='s', edgecolors='black', linewidths=2,
label='End', zorder=5)
ax.set_xlabel('Facet 1')
ax.set_ylabel('Facet 2')
ax.set_title('Phase Space', fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

plt.tight_layout()
return fig
```

-----
