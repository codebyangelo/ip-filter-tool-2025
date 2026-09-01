# ip-filter-tool-for-access-control-2025

[![CI: Python Test](https://github.com/codebyangelo/PROJECT-NAME/actions/workflows/test.yml/badge.svg)](https://github.com/codebyangelo/ip-filter-tool-2025/actions/workflows/test.yml)

**Project Name:** `ip_filter_tool.py`

A Python-based script that enforces network access control by maintaining an allow-list of authorized IP addresses. Built as part of the Google Cybersecurity Certificate portfolio to demonstrate applied scripting in real-world data security scenarios.


## Purpose

This security tool automates the process of updating an IP address allow-list to ensure only authorized employees have network access to sensitive patient records. It minimizes human error by programmatically removing known unauthorized IP addresses while preserving legitimate ones.


#### Key Concepts Demonstrated

- Safe file operations using `with open()` (ensures automatic file closure)
- Defensive programming via least privilege access (read/write separation)
- String parsing and list transformations (`.read()`, `.split()`, `.join()`)
- Conditional filtering and controlled list mutation (`for` + `if` + `.remove()`)
- Basic data sanitation (manual detection of malformed/duplicate entries—optional future upgrade)


### How It Works

1. **Reads** a plaintext file named `allow_list.txt` containing IP addresses separated by spaces.
2. **Splits** the string into a Python list of IPs.
3. **Iterates** through the list and removes any IPs found in a predefined `remove_list`.
4. **Rewrites** the sanitized list back into the original file.


### Setup and Usage

**1. Clone Repository** 

bash

git clone https://github.com/codebyangelo/ip-filter-tool.git
cd ip-filter-tool


**2. Prepare your `allow_list.txt` file** 

### Format:

192.168.97.225 192.168.1.10 192.168.158.170 10.0.0.25 999.999.999.999 192.168.201.40
192.168.58.57 172.16.0.5 192.168.0.100


**3. Run the Script** 

Make sure you have Python 3.x installed, then:

bash

python ip_filter_tool.py



### Files Included

| File Name          | Description                                  |
|--------------------|----------------------------------------------|
| `ip_filter_tool.py`| Python script implementing the filter logic  |
| `allow_list.txt`   | List of authorized IPs (user-editable)       |
| `README.md`        | Documentation for project and portfolio use  |


### Notes

- Duplicate IP entries in `remove_list` require the script to run more than once to fully sanitize. This is a known limitation and can be enhanced using list comprehension or auxiliary filtering logic in future iterations.
- Malformed IPs (e.g., `999.999.999.999`) are not filtered unless explicitly added to the `remove_list`. Format validation is intentionally omitted for this first build to maintain clarity and scope control.


### Future Improvements

- Implement duplicate-safe filtering using list comprehension or `filter()`
- Add optional IP format validation using regex or built-in `ipaddress` module
- Modularize logging for audit trails
- Expand to CSV or config-file support for enterprise-scale lists


### Certification Context

This project was developed as part of the Google Cybersecurity Certificate. It reflects hands-on understanding of basic scripting, secure automation practices, and file-level access control. Demonstrating readiness for real-world infosec tasks.


Author: Angelo Ayton
