import math

# is math in sys modules?
# if not load and insert ref
# add math to modules global namespace

import math as r_math

# is math in sys modules?
# if not load and insert ref
# add r_math symbol to module global namespace

from math import sqrt

# is math in sys modules
# if not load and insert ref
# add sqrt to module global namespace referencing math.sqrt


# in the 3 examples above the oinly difference was what gets put in the global namespace

from math import *

# is math in sys modules
# if not load and insert ref
# add all the stuff from __all__ into global name space

import sys

for key in sorted(sys.modules.keys()):
    print(key)