import subprocess
import webbrowser
import os
# imports above
base = os.path.dirname(os.path.abspath(__file__))
print("Initiating jailbreak...") # start vr2jb
try:
    ran = subprocess.run("vr2jb/vr2jb.exe")
    if ran.returncode != 0: print("jailbreak failed! check that a folder named \"vr2jb\" exists and is near the script, and contains vr2jb.exe")
    else:
        print("jailbreak succeeded")
except FileNotFoundError:
    print("No jailbreak folder found! Skipping jailbreak...")
print("initializing SteamVR") # start steamvr
print("Starting SteamVR...")
webbrowser.open("steam://rungameid/250820")
try:
    extras = os.listdir(os.path.join(base, "extras"))
    if len(extras) != 0:
        print("Extras found!")
        for extra in extras:
            os.startfile(os.path.join(base, "extras", extra))
    else:
        print("Extras not found.")
except FileNotFoundError:
    print("No extras folder.")
print("Nothing else to do: Finished!")