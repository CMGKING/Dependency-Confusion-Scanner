import json


def load_internal_packages():

    with open("internal_packages.json", "r") as file:

        data = json.load(file)


    return data["internal_packages"]



def check_internal(package):

    internal_packages = load_internal_packages()


    for item in internal_packages:


        if item["name"] == package:


            return item



    return None



if __name__ == "__main__":


    print(
        check_internal(
            "company-payment-api"
        )
    )