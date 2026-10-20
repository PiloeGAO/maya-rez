name = "maya"

version = "2027.2-r.1"

authors = [
    "Autodesk"
]

description = \
    """
    Animation and VFX  software.
    """

requires = [
    "python-3.13.9",
]

uuid = "autodesk.maya"

build_command = ""

def commands():
    env.PATH.prepend("C:\\PROGRA~1\\Autodesk\\Maya2027\\bin")
