# Information Masker
[![Pylint](https://github.com/tyfncn/InformationMasker/actions/workflows/pylint.yml/badge.svg)](https://github.com/tyfncn/InformationMasker/actions/workflows/pylint.yml)

This repo contains a module that masks info from cvs file (hopefuly sql in later versions).
Masked cvs file can be used for development testing purposes.

## Local Usage - As console app
```console
git clone https://github.com/tyfncn/InformationMasker.git
cd InformationMasker/
python3 -m information_masker [input cvs file]
```

## Usage as Library and Extending
Install as pypi package
```
cd /tmp
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/tyfncn/InformationMasker.git
```
Use as preferred in own python project. Here is an example script for all caps transformation.
```python
#extend_library.py
from information_masker.input_reader import CvsReader
from information_masker.output_writer import CvsWriter
from information_masker.maskers import alpha_numeric_masker

header = ['ID', 'Name', 'Email', 'Billing', 'Location']
in_file = CvsReader("customers.csv", header)
out_file = CvsWriter("masked_customers.csv")
out_file.write_item(header)
for item in in_file:
    masked_item = (
        item[0],                       # ID
        item[1].upper(),               # Name    
        item[2].lower(),               # Email 
        item[3],                       # Billing
        alpha_numeric_masker(item[4])  # Location
    )
    out_file.write_item(masked_item)

```
