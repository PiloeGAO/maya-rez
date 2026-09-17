name = "maya"

version = "2027.2"

authors = [
    "Autodesk"
]

description = \
    """
    Animation and VFX  software.
    """

uuid = "autodesk.maya"

build_command = ""

def commands():
    env.PATH.prepend("C:\\PROGRA~1\\Autodesk\\Maya2027\\bin")
