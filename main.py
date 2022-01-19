from androguard.misc import AnalyzeAPK
from basic import *
from extraction_communication import *
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # recupere le nom de l'APK à annalyser
    apk_name = sys.argv[1]
    # recupere le nom de l'activity à annalyser
    activity_name = sys.argv[2]
    a, d, dx = AnalyzeAPK(apk_name+'.apk')
    #compute(activity_selected)
    get_info_class(a, d, activity_name)
##############################################################################################