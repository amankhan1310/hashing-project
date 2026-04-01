Hashing Utilities (Python)
**Overview**

This repository contains Python scripts for hashing mobile numbers and generating secure hash values for data processing and anonymization tasks.

It includes utilities for handling large datasets efficiently and applying hashing techniques such as SHA-256 and HMAC.

**📂 Files**
github_1.py
→ Script for hashing mobile numbers from CSV/Excel files using SHA-256
github_hmac.py
→ Script demonstrating hashing using HMAC for enhanced security
🚀 Features
Cleans and standardizes mobile numbers
Supports large files using chunk-based processing
Generates consistent hash outputs
Efficient and scalable for real-world datasets
🛠️ Technologies Used
Python 3
Pandas
Hashlib
HMAC
Regular Expressions (re)
▶️ How to Run
1. Install dependencies
pip install pandas
2. Run the script
python github_1.py

or

python github_hmac.py
📥 Input
CSV or Excel file containing mobile numbers
📤 Output
CSV file containing hashed values
🔒 Notes
Sensitive data (like salts/keys) should not be hardcoded
Use environment variables for secure handling
Do not upload real datasets or confidential information

**⚠️ Disclaimer**

These scripts are intended for data processing and anonymization purposes only.
They are not designed for secure password storage systems.

👨‍💻 Author

Aman Khan
