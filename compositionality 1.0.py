# Compositionality
# no support for multinucs - the criterion is not explicit on this

import sys
from defaulthandlers import *

comp_dict = {}

def get_exp_list(args):
    exp_list = []
    for rp in args:
        exp_list.append(compose(rp))
    return exp_list

def format_rp(rel, exp_list):
    return '{}({})'.format(rel,','.join(map(str,exp_list)))

def compose(rp):
   
    if not isinstance(rp, tuple):
        return rp

    rel, args = rp[0], rp[1]
    sat = args[0]
    nuc = args[1]
    
    exp = format_rp(rel, get_exp_list(args))

    if isinstance(sat, tuple) and isinstance(nuc, tuple):
        
        sat = compose(sat[1][1])  # nuc of sat 
        nuc = compose(nuc[1][1])   # nuc of nuc
        
        comp_dict[exp] = '{}({},{})'.format(rel,sat,nuc)
        
    elif isinstance(sat, tuple):

        sat = compose(sat[1][1])
        comp_dict[exp] = '{}({},{})'.format(rel,sat,nuc)

    elif isinstance(nuc, tuple):
        
        nuc = compose(nuc[1][1])
        comp_dict[exp] = '{}({},{})'.format(rel,sat,nuc)
        
    else:
        comp_dict[exp] = nuc

    return exp

# not lazy
# exp = 'background(volitional_result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'

# arithmetic
exp = 'concession(condition(2,1),evidence(condition(5,concession(7,6)),antithesis(4,3)))'

# Marcu tobacco
# exp = 'evidence(concession(4,3),unconditional(1,2))'

# Frege 
# exp = 'concession(condition(1,2),evidence(background(antithesis(4,5),6),3))'

compose(eval(exp))

for comp, inf in comp_dict.items():
    print('{}:\n{}\n'.format(comp, inf))



