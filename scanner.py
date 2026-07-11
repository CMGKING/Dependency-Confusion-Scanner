import argparse
import sys
import os

from parser import parse_requirements, parse_package_json, parse_pom
from registry import check_pypi, check_npm, check_maven
from confusion_engine import detect_confusion
from report import generate_report



def scan(file):


    results = []


    filename = os.path.basename(file)



    if filename == "requirements.txt":


        packages = parse_requirements(file)


        for package in packages:

            result = check_pypi(package)
            
            analysis = detect_confusion(result)
            
            results.append(analysis)




    elif filename == "package.json":


        packages = parse_package_json(file)


        for package in packages:


            result = check_npm(package)


            analysis = detect_confusion(result)


            results.append(analysis)




    elif filename == "pom.xml":


        packages = parse_pom(file)


        for package in packages:


            result = check_maven(package)


            analysis = detect_confusion(result)


            results.append(analysis)




    else:


        print("[!] Unsupported file type")

        sys.exit(1)



    return results



    

if __name__ == "__main__":



    parser = argparse.ArgumentParser()



    parser.add_argument(

        "--file",

        required=True

    )



    args = parser.parse_args()



    findings = scan(args.file)



    print("\nDependency Confusion Report")

    print("="*40)



    for item in findings:


        print(

f"""
Package : {item['package']}
Registry: {item['registry']}
Risk    : {item['risk']}
Reason  : {item['reason']}
"""

        )



    generate_report(findings)



    high_risk = False



    for item in findings:


        if item["risk"] == "HIGH":


            high_risk = True




    if high_risk:


        print(
            "\n[!] Build failed: HIGH risk dependency confusion detected"
        )


        sys.exit(1)




    else:


        print(
            "\n[+] Security check passed"
        )


        sys.exit(0)