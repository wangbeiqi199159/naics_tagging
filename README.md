# NAICS Codes Tagging for Companies

Becky Wang

beiqi.wang0509@gmail.com

### Objectives

This project is about extracting textual data from HTML files and using the data for categorizing companies using NAICS ([North American Industry Classification System](https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2017)).

Each company will be assigned one or more NAICS codes based on publicly available information about the company and on descriptions of NAICS codes. Descriptions of NAICS subsector codes are provided in the HTML files in the zipped file. Snippets of text about 4 companies are provided as separate text files.

### Methodologies

In the project, I first scrape all HTML files under ```lookup``` folder. I only focus on three parts of the descriptions on HTLM page. As shown below: I scrape part 1 for NAICS subsector code and name, part 2 for the first paragrah and part 3 for all industry groups under the subsector.

After getting all the information needed, I use bag-of-words method to get the similarity matrix of company's description to all NAICS subsector descriptions, trying to find top three NAICS subsector that are most related. The method I use is called ```Term Frequency, Inverse Document Frequency``` abbreviated to ```tf-idf```, which is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.

### Environment

- Python 3.6
- pandas
- numpy
- nltk
- sklearn

## Tips:

How to run the program : Get to local path in console, type ```python naics_tagging.py```

The process of parsing HTLM, loading data, matching company description to NAICS codes can be found in ```NAICS codes tagging for companies (demo).html```