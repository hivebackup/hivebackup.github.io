const user = "hivebackup"
const repo = "hivemaps"

Element.prototype.getElementById = function(id) {
    return document.getElementById(id);
}


async function setCount(releaseID, parentId) {
    return fetch('https://api.github.com/repos/${user}/${repo}/releases/${releaseID}'
        .replace('${user}', user).replace('${repo}', repo).replace('${releaseID}', releaseID))
        .then(async r => setDlCounts(JSON.parse(await r.text()), parentId))
        .catch(e => console.error('Boo...' + e));
}

function setDlCounts(release, parentId) {

    const assets = release.assets
    for (const index in assets) {
        const asset = assets[index]
        replaceElement(asset.name, "Downloads: " + asset.download_count, parentId)
    }
}

function replaceElement(toReplace, replacing, parentId) {
    if (parentId == null) {
        const elem = document.getElementById(toReplace)
        elem.innerText = replacing
    } else {
        //lmao thanks js
        const epic = toReplace.replace(".", "\\.")
        const elem = document.querySelector("#"+parentId+" #"+epic); 
        elem.innerText = replacing
    }
}