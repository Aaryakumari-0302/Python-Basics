# from Module1.hello import add
# add(15,4)

import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)
from Module1.hello import add
add(5,20)