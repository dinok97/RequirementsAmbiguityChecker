# Requirement Ambiguity Checker

A simple project to analyze ambiguous sentences inside SRS (Software Requirements Specification) Document.


## Method
This project use a very simple technique in **NLP** which are **Rule-Base Technique** and **Statistical-Base Technique**. 
- Rule-based techniques uses to determine whether a requirements sentence is ambiguous or unambiguous based on a repository of rules and recommendations that have been provided.
- Statistical-based techniques uses to provide corrective recommendations for ambiguous software requirement sentences


## Language and Libraries
Language: **Python >= 3.6**

Important Libraries:
1. Language processing: **[nltk](https://www.nltk.org/) 3.7**
2. User interface: **[tkinter](https://docs.python.org/3/library/tkinter.html) 0.1.0** 
3. File reader: **[python-docx](https://python-docx.readthedocs.io/en/latest/) 0.8.11**


## How to Use
The entrypoint of this project is Main.py
Just go to Docs directory and follow instruction in **HowToUse.MD**


## Constrains
Since this projects really simple, there are some constraints:
- Only work on SRS in Indonesian Language
- Only support for SRS in MS Word Document (.docx, .doc)
- Limited source of Rule (bank of ambiguous words)