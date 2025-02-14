from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_model = []

pm(unprinted_designs, completed_model)
scm(completed_model)