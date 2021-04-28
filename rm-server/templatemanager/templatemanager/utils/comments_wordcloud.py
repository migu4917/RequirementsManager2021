import jieba
import pandas as pd
import wordcloud


def genewordcloud(file):
    # parse the df to list
    df = pd.DataFrame(file)
    # use the list to generate wordcloud picture
    return df
