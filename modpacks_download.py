import os, sys
import shutil, errno
import json
from subprocess import call

def copy_dir(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                copy_dir(os.path.join(src, f), 
                        os.path.join(dest, f), 
                        ignore)
    else:
        shutil.copyfile(src, dest)


def makedir(directory):
    """
        Make the directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def download(url, destination):
    """
        Download with wget the url to the destination
    """
    call(["wget", url, "-q", "--show-progress", "-nc", "-P", destination, "--content-disposition"])


def download_curseforge_mods(mods, target, game_version):
    """
        Download all mods listed from CurseForge to target
    """
    # Make sure the directory exists
    makedir(target)
    
    # Download from CurseForge each mod
    if game_version == "1.7.10":
        version_filter = "?filter-game-version=1738749986%3A5"
    elif game_version == "1.8.9":
        version_filter = "?filter-game-version=1738749986%3A4"
    else:
        print("[ERRO] Bad game version : " + game_version)
        return
    
    for mod_name in mods:
        print("[INFO] Looking for " + mod_name + "...", end='\r')
        sys.stdout.write("\033[K")
        url = "http://minecraft.curseforge.com/projects/" + mod_name + "/files/latest" + version_filter
        download(url, target)


def update_modpacks(modpacks):
    """
        Copy and download mods for each modpack
    """
    for modpack_name in modpacks:
        src_directory = "modpack-" + modpack_name + "/"
        target_directory = "creator_workspace/" + modpack_name + "/"

        # Get the list of mods
        print("[INFO] Loading " + modpack_name + " packages...")
        with open(src_directory + 'mods.json') as data_file:    
            mods = json.load(data_file)

        # Copy manifest and get the version of the modpack
        shutil.copyfile(src_directory + "modpack.json", target_directory + "modpack.json")
        with open(src_directory + 'modpack.json') as data_file:    
            version = json.load(data_file)["gameVersion"]

        # Download and copy mods
        download_curseforge_mods(mods["curseforge_coremods"], target_directory + "src/coremods/", version)  # Core mods
        download_curseforge_mods(mods["curseforge_mods"], target_directory + "src/mods/", version)  # Main mods
        download_curseforge_mods(mods["curseforge_client_mods"], target_directory + "src/mods/_CLIENT/", version)  # Client-only mods
        download_curseforge_mods(mods["curseforge_server_mods"], target_directory + "src/mods/_SERVER/", version)  # Server-only mods
        copy_dir(src_directory + "mods-manual/", target_directory + "src/mods/")
        if os.path.isdir(src_directory + "config/"):
            copy_dir(src_directory + "config/", target_directory + "src/config/")


modpacks = ["dobbyvanilla", "badapack", "dobbymod", "dobbymod-magic", "dobbytech"]
update_modpacks(modpacks)

