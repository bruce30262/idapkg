__version__ = '0.1.0'

import sys
from commands import *

# expose 'pkg' in global namespace
__builtins__[__name__] = sys.modules[__name__]
