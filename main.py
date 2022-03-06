from ast import Str
import os
from typing import List, Optional
from webbrowser import get

path: str = "/home/nix/discordExports/hive/"


def moveOs(origin, target):
    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target))
    os.system("mv '" + origin + "' '" + target + "'")

def copyOs(origin, target):
    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target))
    os.system("cp '" + origin + "' '" + target + "'")


def removeStartFolder() -> None:
    for folder in os.listdir(path):
        #input("mv '" + path + folder + "' '" + path + folder.replace("Hive Backup Project - ", "") + "'")
        moveOs(path + folder, path + folder.replace("Hive Backup Project - ", ""))

def listFolderWith(search) -> List[Str]:
    results = []
    for folder in os.listdir(path):
        if search in folder and folder[-5:] != ".html":
            results.append(folder)
    return results

def getExtension(path) -> Str | None:
    try:
        return path.split(".")[-1]
    except:
        return None


def getFolderMapName(path) -> Str | None:
    try:
       return path.split("[")[0].split(" - ")[1].strip()
    except:
        return None


def copyFilesRightFolder(origin, target, mapName) -> None:
    match getExtension(origin):
        case "zip":
            copyOs(origin, path + "/AA_zips_" + target + ".zip")
        case "png":
            copyOs(origin, path + "/AA_pngs_" + target + ".png")
        case "jpg":
            copyOs(origin, path + "/AA_pngs_" + target + ".jpg")


def checkValidFolder(folder) -> bool:
    if(len(os.listdir(path + folder)) != 2):
        if "_" in folder:
            return True
        else:
            input("CONFIG ISSUE @" + folder)
            return False
    return False

#fait:
#lobbies
#deathrun
#gravity
#survival games
#



githubuser: str = "hivebackup"
githubrepo: str = "hivemaps"

githubRelease: str = "Arcade"
search: str = "Arcade - battery-d"
fullName: str = "Battery Dash"

staticFolder: str = "Arcade/BatteryDash"
fullHtml = ""
baseHtml = f"""<!DOCTYPE html>

<body>
    <div id="sidebar" class="sidebar"></div>

   <h1>{fullName}</h1>

    <div class="grid-container">
        TOREPLACE
    </div>
</body>

<style>
    @import url('static/html.css');
</style>
<script src="/static/sidebar.js"></script>
<script src="/static/grabDownloadCount.js"></script>
<script>
    setCount(releaseID = TOCHANGE!!)
</script>
"""

#baseHtml = "TOREPLACE"


def genHtml(zipname, imgname, mapName):
    fullHtml = f'<a href="https://github.com/{githubuser}/{githubrepo}/releases/download/{githubRelease}/{zipname}">'
    fullHtml += '<div class="grid-item">\n'
    fullHtml += f'<img src="/static/previews/{staticFolder}/{imgname}">\n'
    fullHtml += f'Map name: {mapName}<br>\n'
    fullHtml += f'<div id="{zipname}"></div>\n'
    fullHtml += '</div></a>\n'
    return fullHtml



def doTheThing():
    for folder in listFolderWith(search):
        #print(folder)
        print(folder)
        if checkValidFolder(folder): continue

        mapName = getFolderMapName(folder)
        
        genMapName = mapName.replace("-", " ").title()
        genZipName = mapName.replace(" ", "_") + ".zip"
        genImgName = mapName.replace(" ", "_") + ".png"

        fullHtml += genHtml(genZipName, genImgName, genMapName)


        for file in os.listdir(path + folder):
            copyFilesRightFolder(path + folder + "/" + file, search.replace(" ", "_") + "/" + mapName, mapName)

    print(baseHtml.replace("TOREPLACE", fullHtml))


#doTheThing()

bp = "/home/nix/.minecraft/saves/"
for folder in os.listdir(bp):
    if getExtension(folder) == 'zip':
        os.system("7z e "+bp+folder+ " -o"+bp+folder[:-4])
        os.system("rm "+bp+folder)
        continue
    
    if not os.path.exists(bp + folder+ "/region"):
        os.makedirs(bp + folder+ "/region")

    for file in os.listdir(bp + folder):
        print(file[:7])
        if file[:7] == "region\\":
            os.system("mv '"+bp+folder+"/"+file+"' '"+bp+folder+"/region/"+file[7:]+"'")