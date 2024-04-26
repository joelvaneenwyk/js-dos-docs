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