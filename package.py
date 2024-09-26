name = "maya"

version = "2025.2"

authors = [
    "Autodesk"
]

description = \
    """
    Animation and VFX  software.
    """

tools = [
    "maya",
    "mayabatch",
    "mayapy",
    "mayarender"
]

uuid = "autodesk.maya"

build_command = ""

def commands():
    env.MAYA_LOCATION = "C:\\PROGRA~1\\Autodesk\\Maya2025"

    alias("maya", "C:\\PROGRA~1\\Autodesk\\Maya2025\\bin\\maya.exe")
    alias("mayabatch", "C:\\PROGRA~1\\Autodesk\\Maya2025\\bin\\mayabatch.exe")
    alias("mayapy", "C:\\PROGRA~1\\Autodesk\\Maya2025\\bin\\mayapy.exe")
    alias("mayarender", "C:\\PROGRA~1\\Autodesk\\Maya2025\\bin\\Render.exe")
