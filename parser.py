import json
import xml.etree.ElementTree as ET


# --------------------------------------------
# Parse requirements.txt
# --------------------------------------------
def parse_requirements(file):

    packages = []

    with open(file, "r") as f:

        for line in f:

            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Skip comments
            if line.startswith("#"):
                continue

            # Remove inline comments
            if "#" in line:
                line = line.split("#")[0].strip()

            # Remove version specifiers
            for operator in ["==", ">=", "<=", "~=", ">", "<"]:
                if operator in line:
                    line = line.split(operator)[0].strip()
                    break

            if line:
                packages.append(line)

    return packages


# --------------------------------------------
# Parse package.json
# --------------------------------------------
def parse_package_json(file):

    packages = []

    with open(file, "r") as f:

        data = json.load(f)

    dependencies = data.get("dependencies", {})
    packages.extend(dependencies.keys())

    return packages


# --------------------------------------------
# Parse pom.xml
# --------------------------------------------
def parse_pom(file):

    packages = []

    tree = ET.parse(file)
    root = tree.getroot()

    for dependency in root.iter():

        if dependency.tag.endswith("artifactId"):

            if dependency.text:
                packages.append(dependency.text.strip())

    return packages


# --------------------------------------------
# Testing
# --------------------------------------------
if __name__ == "__main__":

    print("requirements.txt")
    print(parse_requirements("samples/requirements.txt"))

    print("\npackage.json")
    print(parse_package_json("samples/package.json"))

    print("\npom.xml")
    print(parse_pom("samples/pom.xml"))