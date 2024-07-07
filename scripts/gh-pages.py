#!/usr/bin/env python3
"""Generates GitHub pages for `js-dos` project."""
# pylint:disable=invalid-name
# cspell:ignore doswindow,jsdos,ghpages

import os
from os.path import join, exists
from zipfile import ZipFile


def inject_doswindow(file: str):
    """Injects DOS window into the subscription page."""
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read().replace(
            ".doswindow.",
            """
<div style="border: 2px solid blue; height: 600px;">
    <iframe id="doswindow" style="width: 100%; height: 100%;"></iframe>
</div>
<script>
    const params = new URLSearchParams(location.search);
    const refresh_token = params.get("jsdos_token");
    const token_param = refresh_token ? "?jsdos_token=" + refresh_token : "";
    document.getElementById("doswindow").src = "/iframe/blank.html${token_param}";
    if (refresh_token) {
        window.history.replaceState(null, "", "/subscription.html#create-account");
    }
</script>
""",
        )

    with open(file, "w", encoding="utf-8") as f:
        f.write(contents)


def main():
    """Main entry point."""
    # Get the current directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    ghpages_root = join(current_dir, "..", "js-dos-gh-pages")
    archive = "webHelpJSDOS2-all.zip"

    if not exists(join(ghpages_root, "CNAME")):
        print("Can't find gh-pages in", ghpages_root)
        exit(1)

    if not exists(archive):
        print("Document archive not found")
        exit(2)

    ZipFile(archive).extractall(ghpages_root)

    inject_doswindow(join(ghpages_root, "subscription.html"))


if __name__ == "__main__":
    main()
