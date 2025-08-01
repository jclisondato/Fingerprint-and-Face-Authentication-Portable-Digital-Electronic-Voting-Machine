import os
import subprocess

if os.path.exists(‘/media/pi/L_CAMERA’):
    subprocess.run(["sudo", "python", "unmount", "-l","/media/pi/L_CAMERA"])
if os.path.exists(‘/media/pi/F_CAMERA’):
    subprocess.run(["sudo", "python", "unmount", "-l","/media/pi/F_CAMERA"])
if os.path.exists(‘/media/pi/B_CAMERA’):
    subprocess.run(["sudo", "python", "unmount", "-l","/media/pi/B_CAMERA"])
if os.path.exists(‘/media/pi/R_CAMERA’):
    subprocess.run(["sudo", "python", "unmount", "-l","/media/pi/R_CAMERA"])

