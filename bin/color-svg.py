import os
import lxml.etree


# Constants
IMAGE_PATH = "../dist/themes/discord/images"
ICONS_PATH = f"{IMAGE_PATH}/icons"
INDICATORS_PATH = f"{IMAGE_PATH}/indicators"
VARIANTS = ("invert", "progressive", "destructive", "warning")

# Maps
file_maps = {
    "icons": [_ for _ in os.listdir(ICONS_PATH)],
    "indicators": [_ for _ in os.listdir(INDICATORS_PATH)]
}


class SVG:
    def __init__(self, path):
        self.path = path
        self.tree = lxml.etree.ElementTree(file=path)

    def edit(self, color="#fff"):
        root = self.tree.getroot()
        parent = lxml.etree.Element('g', fill=f"{color}")
        parent.extend(root)
        root.append(parent)
        self.tree = lxml.etree.ElementTree(root)
        return lxml.etree.tostring(self.tree)

    def write(self):
        self.tree.write(self.path)
        print(f"Wrote: {self.path}")


def main():
    """Abominable hack to recolor non-variant SVGs. Fix later!"""
    for folder, files in file_maps.items():
        for file_name in files:
            if not any(_ in file_name for _ in VARIANTS):
                if folder == "icons":
                    path = f"{ICONS_PATH}/{file_name}"
                    svg = SVG(path)
                    svg.edit()
                    svg.write()
                elif folder == "indicators":
                    path = f"{INDICATORS_PATH}/{file_name}"
                    svg = SVG(path)
                    svg.edit()
                    svg.write()


if __name__ == "__main__":
    main()
