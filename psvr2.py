import subprocess
import webbrowser
import os
from sys import platform
from sys import argv
# imports above
base = os.path.dirname(os.path.abspath(__file__))
wayvr = False
if len(argv) >= 2:
    if argv[1] == "wayvr":
        wayvr=True
        print("Using wayvr!")
print("Initiating jailbreak...") # start vr2jb
try:
    print("Detected platform: " + platform)
    if platform == "win32":
        ran = subprocess.run("vr2jb/vr2jb.exe")
    else: ran = subprocess.run("vr2jb/vr2jb")
    if ran.returncode != 0:
        print("jailbreak failed! check that a folder named \"vr2jb\" exists and is near the script, and contains vr2jb")
        if platform != "win32": print("Make sure to run \"chmod +x ./*\" in the vr2jb folder.")
    else:
        print("jailbreak succeeded")
except FileNotFoundError:
    print("No jailbreak folder found! Skipping jailbreak...")
print("initializing SteamVR") # start steamvr
if wayvr:
    print("Starting WayVR...")
    ran = subprocess.run("wayvr", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if ran != 0: print("Error starting WayVR")
    else: print("WayVR started successfully!")
else:
    print("Starting SteamVR")
    webbrowser.open("steam://rungameid/250820")
try:
    extras = os.listdir(os.path.join(base, "extras"))
    if len(extras) != 0:
        print("Extras found!")
        if platform != "win32":
            for extra in extras:
                if extra.endswith(".sh"): subprocess.run(["bash", "extras/" + extra])
                else: subprocess.run("extras/" + extra)
        else:
            for extra in extras:
                os.startfile(os.path.join(base, "extras", extra))
    else:
        print("Extras not found.")
except FileNotFoundError:
    print("No extras folder.")
print("Nothing else to do: Finished!")
