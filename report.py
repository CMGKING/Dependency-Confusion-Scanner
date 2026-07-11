import json
from datetime import datetime


def generate_report(findings):


    high = 0
    medium = 0
    low = 0
    safe = 0


    for item in findings:


        if item["risk"] == "HIGH":

            high += 1


        elif item["risk"] == "MEDIUM":

            medium += 1


        elif item["risk"] == "LOW":

            low += 1


        elif item["risk"] == "SAFE":

            safe += 1



    report = {


        "scanner":

        "Dependency Confusion Scanner",



        "scan_time":

        str(datetime.now()),



        "summary": {


            "total_packages":

            len(findings),


            "high_risk":

            high,


            "medium_risk":

            medium,


            "low_risk":

            low,


            "safe":

            safe

        },


        "mitigation": [


            "Use private package namespaces",


            "Maintain internal package allowlist",


            "Configure private registry priority",


            "Pin dependency versions",


            "Review public package ownership"

        ],



        "findings":

        findings

    }



    with open(

        "dependency_report.json",

        "w"

    ) as file:



        json.dump(

            report,

            file,

            indent=4

        )



    print(

        "\n[+] Report saved: dependency_report.json"

    )