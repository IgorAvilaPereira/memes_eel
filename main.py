# https://github.com/python-eel/Eel
import eel
from subprocess import call

@eel.expose
def aumentaVolume(a):
    call(["amixer", "-D", "pulse", "sset", "Master", str(a)+"%+"])  

@eel.expose
def diminuiVolume(a):
    call(["amixer", "-D", "pulse", "sset", "Master", str(a)+"%-"])  

# @eel.expose
# def aumentaVolumeMicrofone(a):
#     call(["amixer", "-D", "pulse", "sset", "USB AUDIO", str(a)+"+"])

eel.init('web')
eel.start('main.html', size=(400,500))