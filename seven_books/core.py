```python
"""
Core dynamics of the Seven Books Model.

This module implements the differential equations governing contemplative
understanding through seven classical texts speaking simultaneously.
"""

import numpy as np


def hill(x, gamma=10.0, threshold=0.5, steepness=6):
"""
Steep sigmoidal activation—insight emerges sharply once threshold crossed.

Parameters
----------
x : float or array
Input activation level [0, 1]
gamma : float, default=10.0
Amplitude of activation response
threshold : float, default=0.5
Scale parameter for activation
steepness : int, default=6
Cooperativity (higher = sharper threshold)

Returns
-------
float or array
Activated response
"""
return gamma * x**steepness / (threshold**steepness + x**steepness)


def model_parable(y, t,
gamma=10.0, threshold=0.5, steepness=6,
base_decay=0.22,
dwelling_rise=0.35,
dwelling_fade=0.45,
coupling_boost=0.8,
decay_relief=0.6,
story_depth=0.8,
nudge_time=None,
nudge_duration=2.0,
nudge_strength=0.5):
"""
The Seven Books Model: Contemplative dynamics with dwelling field.

Parameters
----------
y : array-like, shape (4,)
State vector [x1, x2, x3, dwelling]
t : float
Current time
gamma : float, default=10.0
Hill function amplitude
threshold : float, default=0.5
Hill function threshold
steepness : int, default=6
Hill function cooperativity
base_decay : float, default=0.22
Base decay rate for facets
dwelling_rise : float, default=0.35
How readily dwelling arises with low coherence
dwelling_fade : float, default=0.45
How quickly dwelling releases with high coherence
coupling_boost : float, default=0.8
How dwelling enhances relational listening
decay_relief : float, default=0.6
How dwelling protects against premature closure
story_depth : float, default=0.8
Exogenous richness/complexity of the parable
nudge_time : float or None, default=None
Time for catalytic intervention (grace)
nudge_duration : float, default=2.0
Duration of intervention pulse
nudge_strength : float, default=0.5
Strength of intervention on x1

Returns
-------
list of float
Time derivatives [dx1/dt, dx2/dt, dx3/dt, d_dwelling/dt]

Notes
-----
The seven books encoded as forces:
1. Plato (Republic): Ascent toward ideal
2. Plutarch (Lives): Virtue through comparison
3. Augustine (Confessions): Memory shapes present
4. Marcus Aurelius (Meditations): Cosmic interconnection
5. Aristotle (Ethics): Golden mean
6. Boethius (Consolation): Wheel of fortune
7. Four Gospels: Closure field modulating all others
"""
x1, x2, x3, dwelling = np.clip(y, 0.0, 1.0)

# Current overall coherence
coherence = (x1 + x2 + x3) / 3.0

# Dwelling field dynamics
d_dwelling_dt = (dwelling_rise * story_depth * (1 - coherence) * (1 - dwelling) -
dwelling_fade * coherence * dwelling)

# How dwelling shapes the triad
coupling = 1.0 + coupling_boost * dwelling
decay = base_decay * (1.0 - decay_relief * dwelling)

# Activation of each interpretive facet (Hill function)
act1 = hill(x1, gamma, threshold, steepness)
act2 = hill(x2, gamma, threshold, steepness)
act3 = hill(x3, gamma, threshold, steepness)

# Mutual excitation modulated by dwelling
dx1_dt = coupling * (act2 + act3) / 2.0 * (1 - x1) - decay * x1
dx2_dt = coupling * (act1 + act3) / 2.0 * (1 - x2) - decay * x2
dx3_dt = coupling * (act1 + act2) / 2.0 * (1 - x3) - decay * x3

# Optional catalytic nudge (grace)
if nudge_time is not None and nudge_time <= t < nudge_time + nudge_duration:
dx1_dt += nudge_strength * (1 - x1)

return [dx1_dt, dx2_dt, dx3_dt, d_dwelling_dt]
```

-----
