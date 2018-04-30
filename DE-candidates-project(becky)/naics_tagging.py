import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    userInput = input('Input a company description:')
    print(similarity_matrix(userInput))

def similarity_matrix(test_text):
    """This function will clean the test text, then generate the similarity matrix 
        of company's description to all NAICS subsector descriptions, and print out
        top three NAICS subsector that are most related
    Args:
        text (str): text to be tested
    Returns:
        df: a sorted list of similarity ratio.
    """
    df = pd.read_csv("subsector_cleaned_data.csv")
    contents = df.cleaned_content
    subsector_codes = df.subsector_code
    subsector_names = df.subsector_name

    cleaned_test = clean_text(test_text)
    comb = [cleaned_test] + contents
    vect = TfidfVectorizer(min_df=0.002, max_df = .1, stop_words='english', norm='l2')
    tfidf = vect.fit_transform(comb)
    cor = (tfidf * tfidf.T).A
    corr_df = pd.DataFrame({"corrcoef": cor[0][1:]})
    corr_df_sorded = corr_df.sort_values(by = "corrcoef", ascending=False)

    result1 = "1: " + str(subsector_codes[corr_df_sorded.index[0]]) + " -- " + str(subsector_names[corr_df_sorded.index[0]])
    result2 = "2: " + str(subsector_codes[corr_df_sorded.index[1]]) + " -- " + str(subsector_names[corr_df_sorded.index[1]])
    result3 = "3: " + str(subsector_codes[corr_df_sorded.index[2]]) + " -- " + str(subsector_names[corr_df_sorded.index[2]])
    return result1 + "\n" + result2 + "\n" + result3

def clean_text(text): 
    """This function will clean the text, remove all punctuations and numbers
        and only keep stem of each word
    Args:
        text (str): text to be cleaned
    Returns:
        str: text after cleaning.
    """
    text = text.lower()
    text = text.replace("industry","")
    only_words = re.sub('[^a-zA-Z\s]+', '', text)
    words_list = word_tokenize(only_words)
    stemmer = SnowballStemmer("english")
    cleaned_text = ' '.join(stemmer.stem(word) for word in words_list)

    
    return cleaned_text

if __name__ == '__main__':
    main()

