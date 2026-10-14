import libs.common.number as num
import libs.common.message as msg

note = "module libs.calculate contains mathematic functions"

def calc_hypotenuse(a, b):
    return num.sqrt(num.pow(a) + num.pow(b))