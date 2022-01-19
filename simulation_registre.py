from androguard.misc import AnalyzeAPK
from basic import *

# Analyse 1

def evaluate(instr, registers):
    result = registers.copy()
    name = instr.get_name()
    if (name == 'if-gt' or name == 'return' or name == 'goto'):
        pass
    elif (name == 'mul-int'):
        if (registers[instr.BB] == 'int' and registers[instr.CC] == 'int'):
            result[instr.AA] = 'int'
        else:
            raise TypeError
    elif (name == 'add-int/lit8'):
        if (registers[instr.BB] == 'int' and registers[instr.CC] == 'int'):
            result[instr.AA] = 'int'
        else:
            return TypeError

    elif (name=='move'):
        result[instr.A] = registers[instr.B]

    elif (name == 'move/from16'):
        result[instr.AA] = registers[instr.BBBB]

    elif(name=='move/16'):
        result[instr.AAAA] = registers[instr.BBBB]

    elif (name=='move-wide'):
        result[instr.A]= registers[instr.B]

    elif (name == 'move-wide/from16'):
        result[instr.AA] = registers[instr.BBBB]

    elif(name=='move-wide/16'):
        result[instr.AAAA] = registers[instr.BBBB]

    elif (name=='move-object'):
        result[instr.A]= registers[instr.B]

    elif (name == 'move-object/from16'):
        result[instr.AA] = registers[instr.BBBB]

    elif(name=='move-object/16'):
        result[instr.AAAA] = registers[instr.BBBB]

    elif (name == 'const/4'):
        result[instr.A] = 'int'

    elif name in ['const', 'const/16', 'const/high16', 'const-wide', 'const-wide/high16', 'const-wide/16', 'const-wide/32']:
        result[instr.AA] = 'int'

    elif (name =='const-string'):
        result[instr.AA] = 'String'

    elif (name =='const-string/jumbo'):
        result[instr.AA] = 'String'

    elif (name == 'const-class'):
        result[instr.AA]=instr.cm.get_type(instr.BBBB)

    elif (name == 'array-length'):
        result[instr.A]=result[instr.B]

    elif (name == 'check-cast'):
        result[instr.AA] = instr.cm.get_type(instr.BBBB)

    elif (name == 'new-instance'):
        result[instr.AA] = instr.cm.get_type(instr.BBBB)

    elif (name == 'new-array'):
        if(registers[instr.BBBB]=='int'):
            result[instr.AA] = "array["+instr.cm.get_type(instr.CCCC)+"]"
        else :
            return TypeError

    elif (name == 'filled-new-array/range'):
        result[instr.AA] = "array["+instr.cm.get_type(instr.BBBB)+"]"

    elif name in ["if-test", "if-eq", "if-ne", "if-lt", "if-ge", "if-gt", "if-le"]:
        result[instr.A]=registers[instr.B]

    elif name in ["arrayop", "aget","aget-wide","aget-object","aget-boolean","aget-byte","aget-char","aget-short","aput", "aput-wide","aput-object","aput-boolean","aput-byte","aput-char","aput-short"]:
        if(registers[instr.BB]=="array" and registers[instr.CC]=="array") :
            result[instr.AA]="array"
        else :
            return TypeError

    elif (name=="binop"):
        if (registers[instr.B] == registers[instr.C] == "boolean"):
            result[instr.A] = "boolean"

    elif (name=="binop/2adrr"):
        result[instr.A]="boolean"

    elif (name == "binop/lit16"):
        result[instr.A] = "boolean"

    elif (name == "binop/lit8"):
        result[instr.AA] = "boolean"

    elif name in ["add-int", "sub-int","mul-int","div-int","rem-int","and-int","or-int","xor-int","shl-int", "shr-int","ushr-int"]:
        if(registers[instr.BB]==registers[instr.CC]=="int"):
            result[instr.AA]="int"
        else :
            return TypeError

    elif name in ["add-long","sub-long","mul-long","div-long","rem-long","and-long","or-long","xor-long","shl-long","shr-long","ushr-long"]:
        if (registers[instr.BB] == registers[instr.CC] == "long"):
            result[instr.AA] = "long"
        else:
            return TypeError

    elif name in [" add-float","sub-float","mul-float","div-float","rem-float"]:
        if (registers[instr.BB] == registers[instr.CC] == "float"):
            result[instr.AA] = "float"
        else:
            return TypeError

    elif name in ["add-double","sub-double","mul-double","div-double","rem-double"]:
        if (registers[instr.BB] == registers[instr.CC] == "double"):
            result[instr.AA] = "double"
        else:
            return TypeError

    elif name in ["add-int/2addr", "sub-int/2addr","mul-int/2addr","div-int/2addr","rem-int/2addr","and-int/2addr","or-int/2addr","xor-int/2addr","shl-int/2addr", "shr-int/2addr","ushr-int/2addr"]:
        if(registers[instr.B]=="int"):
            result[instr.A]="int"
        else :
            return TypeError

    elif name in ["add-long/2addr","sub-long/2addr","mul-long/2addr","div-long/2addr","rem-long/2addr","and-long/2addr","or-long/2addr","xor-long/2addr","shl-long/2addr","shr-long/2addr","ushr-long/2addr"]:
        if (registers[instr.B] == "long"):
            result[instr.AA] = "long"
        else:
            return TypeError

    elif name in [" add-float/2addr", "sub-float/2addr", "mul-float/2addr", "div-float/2addr", "rem-float/2addr"]:
        if (registers[instr.B] == "float"):
            result[instr.A] = "float"
        else:
            return TypeError

    elif name in ["add-double/2addr","sub-double/2addr","mul-double/2addr","div-double/2addr","rem-double/2addr"]:
        if (registers[instr.B] == "double"):
            result[instr.A] = "double"
        else:
            return TypeError

    elif name in ["add-int/lit16", "sub-int/lit16","mul-int/lit16","div-int/lit16","rem-int/lit16","and-int/lit16","or-int/lit16","xor-int/lit16"]:
        if (registers[instr.B] == "int"):
            result[instr.A] = "int"
        else:
            return TypeError

    elif name in ["add-int/lit8", "sub-int/lit8","mul-int/lit8","div-int/lit8","rem-int/lit8","and-int/lit8","or-int/lit8","xor-int/lit8", "shl-int/lit8","shr-int/lit8","ushr-int/lit8"]:
        if (registers[instr.B] == "int"):
            result[instr.A] = "int"
        else:
            return TypeError

    return result




def compute_successors(m):
    successors = []
    off = 0
    for instr in m.get_instructions():
        isucc_off = succ_off(m, off, instr)
        isucc = list(map(m.code.get_bc().off_to_pos, isucc_off))
        successors.append(isucc)
        off += instr.get_length()
    return successors


def compute(m):
    successors = compute_successors(m)
    instructions = list(m.get_instructions())
    # number of local registers and parameters
    local_reg = m.get_information()['registers'][1] + 1
    params = len(m.get_information()['params'])
    # initialize the content of variables per program point
    state = []
    for instr in instructions:
        state.append({i: None for i in range(local_reg + params)})
    for p in m.get_information()['params']:
        state[0][p[0]] = p[1]

    todo = [0]
    while todo != []:
        i = todo.pop()
        new = evaluate(instructions[i], state[i])
        for k in successors[i]:
            succstate = max_reg(new, state[k])
            if succstate != state[k]:
                state[k] = succstate
                todo.append(k)
    return new