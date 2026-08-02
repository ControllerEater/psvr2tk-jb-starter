import subprocess
import webbrowser
import os
import sys
# imports above
if getattr(sys, "frozen", False):
    base = os.path.dirname(sys.executable)
else:
    base = os.path.dirname(os.path.abspath(__file__))
wayvr = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "wayvr":
        wayvr=True
        print("Using wayvr!")
print("Initiating jailbreak...") # start vr2jb
try:
    print("Detected platform: " + sys.platform)
    vr2jb_dir = os.path.join(base, "vr2jb")
    vr2jb_name = "vr2jb.exe" if sys.platform == "win32" else "vr2jb"
    vr2jb_path = os.path.join(vr2jb_dir, vr2jb_name)
    ran = subprocess.run([vr2jb_path], cwd=vr2jb_dir)
    if ran.returncode != 0:
        print("jailbreak failed! check that a folder named \"vr2jb\" exists and is near the script, and contains vr2jb")
        if sys.platform != "win32": print("Make sure to run \"chmod +x ./*\" in the vr2jb folder.")
    else:
        print("jailbreak succeeded")
except FileNotFoundError:
    print("No jailbreak executable found at \"" + vr2jb_path + "\"! Skipping jailbreak...")
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
        if sys.platform != "win32":
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
