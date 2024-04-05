



def sent(k):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    pstv=0
    ngtv=0
    ntl=0
    sid = SentimentIntensityAnalyzer()


    ss = sid.polarity_scores(k)

    a = float(ss['pos'])
    b = float(ss['neg'])
    c = float(ss['neu'])

    return str(a),str(b),str(c)
