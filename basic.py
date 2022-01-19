from androguard.misc import AnalyzeAPK

def class_of_name(name):
    return "L" + name.replace(".", "/") + ";"


class TypeError(Exception):
    pass

def succ_off(m, curr_off, instr):
    if (instr.get_name() == 'if-gt'):
        return [curr_off + instr.get_length(), curr_off + instr.CCCC * 2]
    elif (instr.get_name() == 'goto'):
        return [curr_off + instr.AA * 2]
    elif (instr.get_name() == 'return'):
        return []
    else:
        return [curr_off + instr.get_length()]

def max_type(t1, t2):
    if t1 == None:
        return t2
    elif t2 == None:
        return t1
    elif t1 == t2:
        return t1
    else:
        raise TypeError


def max_reg(reg1, reg2):
    result = {}
    if (len(reg1) == len(reg2)):
        for i in range(len(reg1)):
            result[i] = max_type(reg1[i], reg2[i])
        return result
    else:
        raise TypeError


def get_activity(a,d, activity_name):
    activity = class_of_name(a.get_package()+'.'+activity_name)
    for classdef in d:
        c = classdef.get_class(activity)
        if c:
            break
    return c