name = "maya"

version = "2025.2-r.1"

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
    env.PATH.prepend("C:\\PROGRA~1\\Autodesk\\Maya2025\\bin")
