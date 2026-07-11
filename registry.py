import requests


# --------------------------------------------
# Maven Registry
# --------------------------------------------
def check_maven(package):

    url = f"https://search.maven.org/solrsearch/select?q=a:{package}&rows=1&wt=json"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return {
                "registry": "Maven",
                "package": package,
                "exists": False,
                "version": None
            }

        data = response.json()

        docs = data.get("response", {}).get("docs", [])

        if docs:
            return {
                "registry": "Maven",
                "package": package,
                "exists": True,
                "version": docs[0].get("latestVersion")
            }

        return {
            "registry": "Maven",
            "package": package,
            "exists": False,
            "version": None
        }

    except (requests.exceptions.RequestException,
            requests.exceptions.JSONDecodeError):
        return {
            "registry": "Maven",
            "package": package,
            "exists": False,
            "version": None
        }


# --------------------------------------------
# PyPI Registry
# --------------------------------------------
def check_pypi(package):

    url = f"https://pypi.org/pypi/{package}/json"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return {
                "registry": "PyPI",
                "package": package,
                "exists": False,
                "version": None
            }

        data = response.json()

        return {
            "registry": "PyPI",
            "package": package,
            "exists": True,
            "version": data["info"]["version"]
        }

    except requests.exceptions.JSONDecodeError:
        print(f"[!] Invalid JSON received from PyPI for '{package}'")

        return {
            "registry": "PyPI",
            "package": package,
            "exists": False,
            "version": None
        }

    except requests.exceptions.RequestException as e:
        print(f"[!] Network error while accessing PyPI: {e}")

        return {
            "registry": "PyPI",
            "package": package,
            "exists": False,
            "version": None
        }


# --------------------------------------------
# npm Registry
# --------------------------------------------
def check_npm(package):

    url = f"https://registry.npmjs.org/{package}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return {
                "registry": "npm",
                "package": package,
                "exists": False,
                "version": None
            }

        data = response.json()

        return {
            "registry": "npm",
            "package": package,
            "exists": True,
            "version": data["dist-tags"]["latest"]
        }

    except requests.exceptions.JSONDecodeError:
        print(f"[!] Invalid JSON received from npm for '{package}'")

        return {
            "registry": "npm",
            "package": package,
            "exists": False,
            "version": None
        }

    except requests.exceptions.RequestException as e:
        print(f"[!] Network error while accessing npm: {e}")

        return {
            "registry": "npm",
            "package": package,
            "exists": False,
            "version": None
        }


# --------------------------------------------
# Testing
# --------------------------------------------
if __name__ == "__main__":

    print("=== PyPI ===")
    print(check_pypi("requests"))
    print(check_pypi("company-internal-auth"))

    print("\n=== npm ===")
    print(check_npm("express"))
    print(check_npm("company-payment-api"))

    print("\n=== Maven ===")
    print(check_maven("spring-core"))