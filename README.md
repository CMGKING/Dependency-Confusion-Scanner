Dependency Confusion Scanner

A Python-based static security analysis tool that detects **Dependency Confusion** vulnerabilities in software projects. The scanner parses dependency files, checks public package registries (PyPI, npm, and Maven Central), compares them with an internal package inventory, and generates a security report suitable for CI/CD environments.

---
OVERVIEW

Dependency Confusion is a software supply chain attack where an attacker publishes a malicious package with the same name as an organization's private package on a public package registry. If the public package has a higher version number, package managers may install the malicious package instead of the intended internal one.

This project helps identify such risks before deployment.

---

FEATURES

- Parse multiple dependency file formats:
  -  Python (`requirements.txt`)
  -  Node.js (`package.json`)
  -  Java Maven (`pom.xml`)
- Query public package registries:
  - PyPI
  - npm
  - Maven Central
- Compare packages against an internal package inventory
- Detect potential Dependency Confusion attacks
- Compare internal and public package versions
- Assign risk levels:
  - HIGH
  - MEDIUM
  - LOW
  - SAFE
- Generate a JSON security report
- CI/CD friendly (returns non-zero exit code on HIGH-risk findings)

---

 PROJECT STRUCTURE

 
Dependency-Confusion-Scanner/
│
├── scanner.py
├── parser.py
├── registry.py
├── confusion_engine.py
├── internal_checker.py
├── report.py
├── internal_packages.json
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── samples/
    ├── requirements.txt
    ├── package.json
    └── pom.xml
 

---

TECHNOLOGY USED

- Python 3
- Requests
- Packaging
- JSON
- XML Parser (`xml.etree.ElementTree`)
- argparse

---

INSTALLATION

Clone the repository:

  
git clone https://github.com/YOUR_USERNAME/Dependency-Confusion-Scanner.git

cd Dependency-Confusion-Scanner
 

Create a virtual environment:

  
python -m venv venv
 

Activate it.

Windows:

 powershell
venv\Scripts\activate
 

Linux:

  
source venv/bin/activate
 

Install dependencies:

  
pip install -r requirements.txt
 

---

USAGE

SCAN PYTHON PROJECT 

  
py scanner.py --file samples/requirements.txt
 

 Scan Node.js project

  
py scanner.py --file samples/package.json
 

 Scan Maven project

  
py scanner.py --file samples/pom.xml
 

---

EXAMPLE OUTPUT :

 
Dependency Confusion Report
========================================

Package : requests
Registry: PyPI
Risk    : HIGH
Reason  : Internal package exists publicly with higher version.

Package : flask
Registry: PyPI
Risk    : LOW
Reason  : Package is not listed as internal.

[+] Report saved: dependency_report.json

[!] Build failed: HIGH risk dependency confusion detected
 

---

RISK LEVEL

| Risk | Description |
|------|-------------|
| HIGH | Internal package exists publicly with a higher version (possible Dependency Confusion). |
| MEDIUM | Internal package exists publicly but version comparison indicates further review is needed. |
| LOW | Public package is not part of the internal package inventory. |
| SAFE | Internal package is not available on the public registry. |

---

CI/CD INTEGRATION 

The scanner can be integrated into CI/CD pipelines.

Exit codes:

| Exit Code | Meaning |
|-----------|---------|
| 0 | Security check passed |
| 1 | HIGH-risk Dependency Confusion detected |


Example:

py scanner.py --file requirements.txt
echo %ERRORLEVEL%
 

---

SAMPLES FILES

The repository includes sample dependency files for testing:

samples/requirements.txt`
samples/package.json`
samples/pom.xml`

---

FUTURE IMPROVEMENTS 

- Support private registries (Artifactory, Nexus, Azure Artifacts)
- Package scope support (`@company/*`)
- Typosquatting detection
- Homoglyph attack detection
- HTML/PDF report generation
- GitHub Actions integration




