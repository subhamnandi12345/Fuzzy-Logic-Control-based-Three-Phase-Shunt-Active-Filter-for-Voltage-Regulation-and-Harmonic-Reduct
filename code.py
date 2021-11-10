import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
Negative Large = ctrl.Antecedent(np.arange(0, 11, 1), 'NP')
Negative Medium = ctrl.Antecedent(np.arange(0, 11, 1), 'NM')
Negative Small = ctrl.Consequent(np.arange(0, 26, 1), 'NS')
ZERO = ctrl.Antecedent(np.arange(0, 11, 1), 'ZE')
Positive Small = ctrl.Antecedent(np.arange(0, 11, 1), 'PS')
Positive Medium = ctrl.Consequent(np.arange(0, 26, 1), 'PM')
Positive large=ctrl.Consequent(np.arrange(0,26,1), 'PL')

# Auto-membership function population is possible with .automf(3, 5, or 7)
q.automf(3)
s.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip['NP'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['NM'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['NS'] = fuzz.trimf(tip.universe, [13, 25, 25])
tip['ZE'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['PS'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['PM'] = fuzz.trimf(tip.universe, [13, 25, 25])
tip['PL'] = fuzz.trimf(tip.universe, [13, 25, 25])
