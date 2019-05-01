import gensim
from pprint import pprint
from collections import defaultdict

def get_lda_model(texts):
    # 単語の出現回数を格納するfrequency変数を定義
    frequency = defaultdict(int)

    # 単語の出現回数をfrequency変数でカウント
    for text in texts:
        for token in text:
            frequency[token] += 1

    # frequency変数で1より上の単語のみを配列に構築
    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    # 辞書を作成 (単語ID・単語・単語出現回数を持つデータのこと)
    dictionary = gensim.corpora.Dictionary(texts)

    # 辞書を保存することもできる
    # dictionary.save('/src/deerwester.dict')
    # dictionary.save_as_text('/src/deerwester.txt')

    # コーパスを作成 (単語ID・出現頻度をタプル配列で表現したデータのこと)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # ファイルに保存できる
    # corpora.MmCorpus.serialize('/src/deerwester.mm', corpus)

    # LDAモデルを構築
    # num_topic=5で、5個のトピックを持つLDAモデルを作成
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=5, id2word=dictionary)

    # トピックは単語・適合度の組み合わせで構築される
    return lda.show_topics()
    # pprint(lda.show_topic(0))
    # pprint(lda.show_topics())
    # [(0,
    #   '0.139*"graph" + 0.139*"user" + 0.139*"minors" + 0.139*"survey" + '
    #   '0.139*"time" + 0.139*"response" + 0.024*"trees" + 0.024*"system" + '
    #   '0.024*"interface" + 0.024*"eps"'),
    #  (1,
    #   '0.078*"trees" + 0.078*"graph" + 0.077*"system" + 0.077*"user" + 0.077*"and" '
    #   '+ 0.077*"eps" + 0.077*"minors" + 0.077*"human" + 0.077*"interface" + '
    #   '0.077*"time"'),
    #  (2,
    #   '0.330*"trees" + 0.228*"graph" + 0.125*"minors" + 0.125*"and" + '
    #   '0.021*"system" + 0.021*"user" + 0.021*"interface" + 0.021*"time" + '
    #   '0.021*"response" + 0.021*"human"'),
    #  (3,
    #   '0.219*"system" + 0.150*"eps" + 0.150*"human" + 0.150*"interface" + '
    #   '0.082*"user" + 0.082*"and" + 0.082*"computer" + 0.015*"trees" + '
    #   '0.014*"graph" + 0.014*"response"'),
    #  (4,
    #   '0.139*"response" + 0.139*"survey" + 0.139*"system" + 0.139*"user" + '
    #   '0.139*"time" + 0.139*"computer" + 0.024*"trees" + 0.024*"graph" + '
    #   '0.024*"interface" + 0.024*"eps"')]

