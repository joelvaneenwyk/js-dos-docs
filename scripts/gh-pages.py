from os.path import join, exists
from zipfile import ZipFile

ghpages_root = join("..", "js-dos-gh-pages")
archive = "webHelpJSDOS2-all.zip"

if not exists(join(ghpages_root, "CNAME")):
    print("Can't find gh-pages in", ghpages_root)
    exit(1)

if not exists(archive):
    print("Document archive not found")
    exit(2)

ZipFile(archive).extractall(ghpages_root)

def inject_doswindow(file: str):
    with open(file, "r") as f:
        contents = f.read().replace(".doswindow.", """
<div style="border: 2px solid blue; height: 600px;">
    <iframe id="doswindow" style="width: 100%; height: 100%;"></iframe>
</div>
<script>
    const params = new URLSearchParams(location.search);
    const refresh_token = params.get("jsdos_token");
    document.getElementById("doswindow").src = "/iframe/blank.html" + (refresh_token ? "?jsdos_token=" + refresh_token : "");
    if (refresh_token) {
        window.history.replaceState(null, "", "/subscription.html#create-account");
    }
</script>
""")

    with open(file, "w") as f:
        f.write(contents)
        
inject_doswindow(join(ghpages_root, "subscription.html"))
        
