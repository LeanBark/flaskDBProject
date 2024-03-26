import subprocess, shlex, platform

def install_reqs(command):
    cmd = shlex.split(command)
    output = subprocess.check_output(cmd)
    return output

def install_dependencies():
    is_windows = False
    system_type = platform.system()
    if system_type != "Windows":
        check_for_pip = f"python3 -m pip --version"
        install_pip = f"python3 -m ensurepip --default-pip"
    else:
        check_for_pip = f"py -m pip --version"
        install_pip = f"py -m ensurepip --default-pip"
        is_windows = True

    print("Checking for pip..")
    try:
        install_reqs(check_for_pip)
    except:
        print("pip installer not found.")
        print("Attempting to install pip...")
        try:
            install_reqs(install_pip)
        except:
            print("Unable to install pip. Please visit to https://packaging.python.org/en/latest/tutorials/installing-packages/ to manually install pip")
            return
    
    with open("requirements.txt") as reqs:
        install_requires = reqs.read().splitlines()
        if is_windows:
            key_command = "py"
        else:
            key_command = "python3"
        for req in install_requires:
            install_cmd = f"{key_command} -m pip install {str(req)}"
            pkg = str(req).split(">=")
            print(f"Installing/Updating {pkg[0]}...")
            install_reqs(install_cmd)


install_dependencies()