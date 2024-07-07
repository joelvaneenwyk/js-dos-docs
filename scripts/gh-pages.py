#!/usr/bin/env python3
"""Generates GitHub pages for `js-dos` project."""
# pylint:disable=invalid-name

import sys
import os
from os.path import join, exists
from zipfile import ZipFile
import logging


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


def main() -> int:
    """Main entry point."""

    try:
        # Get the current directory of this script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        ghpages_root = join(current_dir, "..", "js-dos-gh-pages")
        archive = "webHelpJSDOS2-all.zip"

        # Initialize logger
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logger = logging.getLogger(__name__)

        if not exists(join(ghpages_root, "CNAME")):
            logger.error("Can't find gh-pages in: '%s'", ghpages_root)
            return 1

        if not exists(archive):
            logger.error("Document archive not found: '%s'", archive)
            return 2

        with ZipFile(archive) as zip_file:
            zip_file.extractall(ghpages_root)

        inject_doswindow(join(ghpages_root, "subscription.html"))
    except Exception as e:  # pylint:disable=broad-except
        logger.error(e)

    return 0


if __name__ == "__main__":
    sys.exit(main())
