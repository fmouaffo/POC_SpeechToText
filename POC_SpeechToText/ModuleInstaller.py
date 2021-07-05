
import subprocess
import sys

#This module will allow this installation of packages
#Using either conda when available, or fallback using pip


def isConda() -> bool:
    try:
        import conda
    except:
        is_conda = False
    else:
        is_conda =  True
    
    return is_conda

def isPip() -> bool:
    try:
        import pip
    except:
        is_pip = False
    else:
        is_pip = True
    
    return is_pip

def installModule(package:str):
    #Suppose pip
    packageManager = "pip"

    if isConda() == True:
        packageManager = "conda"
        subprocess.check_call([sys.executable, "-m", packageManager, "install", "-y", package])
    else:
        subprocess.check_call([sys.executable, "-m", packageManager, "install", package])
