\# PortSwigger Lab Solver: Unprotected Admin Functionality



&#x20;\*\*Note on Learning \& Development:\*\*  

This script was written to practice and strengthen my \*\*Python scripting skills for cybersecurity and digital forensics\*\*, developed in collaboration with \*\*Gemini AI\*\* as a learning partner.



\---



\## Script Overview (`portswigger\_exploit\_lab.py`)



\*\*Target Platform:\*\* PortSwigger Web Security Academy

\*\*Category:\*\* Broken Access Control / Information Disclosure \*\*Lab Level:

\*\* Apprentice

\*\*Vulnerability:\*\* Unauthenticated access to administrative functionality exposed via `robots.txt`.



\---



\## Execution Flow

1\. \*\*Dynamic Target Input:\*\* Asks the user to paste their active PortSwigger lab URL at runtime.

2\. \*\*Reconnaissance:\*\* Requests `/robots.txt` and uses regular expressions (`re`) to locate the `Disallow:` administrative path.

3\. \*\*HTML Parsing:\*\* Uses `BeautifulSoup4` to scan the admin panel's DOM tree for action links.

4\. \*\*Exploitation:\*\* Locates the specific user deletion endpoint for `carlos` and dispatches the deletion request via `requests.Session`.





