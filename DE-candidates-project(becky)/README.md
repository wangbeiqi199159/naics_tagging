# NAICS Codes Tagging for Companies

Becky Wang

beiqi.wang0509@gmail.com

### Objectives

This project is about extracting textual data from HTML files and using the data for categorizing companies using NAICS ([North American Industry Classification System](https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2017)).

Each company will be assigned one or more NAICS codes based on publicly available information about the company and on descriptions of NAICS codes. Descriptions of NAICS subsector codes are provided in the HTML files in the zipped file. Snippets of text about 4 companies are provided as separate text files.

### Environment

- Python 3.6
- pandas
- numpy
- nltk
- sklearn

## Tips:

How to run the program : Get to local path in console, type "python naics_tagging.py"

The process of parsing HTLM, loading data, matching company description to NAICS codes can be found in "NAICS codes tagging for companies (demo).html"


