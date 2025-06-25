name = "maya"

version = "2026.1"

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
    env.PATH.prepend("C:\\PROGRA~1\\Autodesk\\Maya2026\\bin")
