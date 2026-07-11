from internal_checker import check_internal
from packaging import version



def detect_confusion(package_result):


    package = package_result["package"]


    internal = check_internal(package)



    # Case 1:
    # Package is not declared as internal

    if internal is None:


        return {

            "package": package,

            "registry": package_result.get("registry"),

            "risk": "LOW",

            "reason":
            "Package is not listed as internal"

        }



    # Case 2:
    # Internal package exists publicly

    if package_result["exists"]:


        public_version = package_result["version"]

        private_version = internal["version"]



        # Compare versions

        if version.parse(public_version) > version.parse(private_version):


            return {


                "package": package,

                "registry": package_result.get("registry"),

                "risk": "HIGH",

                "reason":
                "Internal package exists publicly with higher version. Possible dependency confusion"

            }



        else:


            return {


                "package": package,

                "registry": package_result.get("registry"),

                "risk": "MEDIUM",

                "reason":
                "Internal package exists publicly but version is not higher"

            }



    # Case 3:
    # Internal package does not exist publicly


    else:


        return {


            "package": package,

            "registry": package_result.get("registry"),

            "risk": "SAFE",

            "reason":
            "Internal package not found publicly"

        }





# Test

if __name__ == "__main__":


    test_package = {


        "package": "company-payment-api",

        "registry": "npm",

        "exists": True,

        "version": "99.0.0"

    }



    result = detect_confusion(test_package)


    print(result)