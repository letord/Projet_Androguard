#!/usr/bin/python3
from basic import *
import sys
from simulation_registre import *
from androguard.misc import AnalyzeAPK

#Analyse 3

def get_info_class(a,d,name):
    with open(name+".report", 'w') as file :
        file.write("Analyse de la classe "+name+" de l'application "+a.get_app_name()+"\n")
        if (len(a.get_permissions()) == 0):
            file.write("Aucunes permissions demandees.\n")
        else:
            text = "Permissions demandees :\n"
            for permission in a.get_permissions():
                text = text + "- " + permission + "\n"
            file.write(text)

        if (len(a.get_declared_permissions()) == 0):
            file.write("Aucunes permissions declarees.\n")
        else:
            text = "Permissions declarees :\n"
            for declared_permission in a.get_declared_permissions():
                text = text + "- " + declared_permission + "\n"
            file.write(text)

        file.write("\n")
        file.write(get_list_method(list(get_activity(a, d, name).get_methods())))
    return None


def get_list_method(list):
    text = ""
    i=1
    while i< len(list):
        method=list[i]
        text=text+"Nom de la methode : "+method.get_name()+'\n'
        #text = text + "Nom de la signature : " + method.get_signature() + '\n'
        text = text + "Registre de sortie : "+str(compute(method))+"\n"
        text = text + "\n"
        i=i+1
    return text