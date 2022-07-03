import utils
import sys
from sympy import *

def run(string,entities):
    func=''
    x=symbols('x')
    for item in entities:
        if item['entity']=='func':
            func=item['sourceText'].lower()
    
    if not func:
        return utils.output('end','func_not_provided',utils.translate('func_not_provided'))
    try:
        res=str(integrate(eval(func),x))
        return utils.output('end','show_int_ans',utils.translate(
            'show_int_ans',{'ans':res}
        ))
    except:
        return utils.output('end','error',utils.translate('error'))
