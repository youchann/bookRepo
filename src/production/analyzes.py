# -*- coding: utf-8 -*-

import MeCab
import neologdn

def analyze_from_file(file_path):
    tagger = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    tagger.parse("")

    all_reviews_result = []

    with open(file_path, encoding='utf-8') as fh:
        stop_words = get_stop_words()
        for line in fh:
            one_review = line.strip()
            analyzed_review = analyze_review(one_review, stop_words, tagger)
            if len(analyzed_review) > 3 : all_reviews_result.append(analyzed_review)

    return all_reviews_result

def analyze_review(review, stop_words, tagger):
    review = neologdn.normalize(review) # 正規化
    node = tagger.parseToNode(review)
    result = []
    while node:
        feature = node.feature.split(",")
        # if feature[0] in ['名詞', '動詞', '形容詞', '感動詞', '副詞'] and not feature[1] in ['固有名詞', '数']:
        if feature[0] in ['名詞', '形容詞', '感動詞'] and not feature[1] in ['固有名詞', '数']:
                result.append(node.surface)  # 語幹に変換
            # result.append(node.feature.split(",")[6]) # そのまま
        node = node.next

    result = list(filter(lambda x: x not in stop_words, result))
    return result

def get_stop_words():
    with open('/src/src/production/Japanese.txt', encoding='utf-8') as fd:
        words = fd.read().splitlines()
        stop_words = frozenset(words)
    return stop_words


# LDAを構築したい
# →品詞選定
# →辞書使えているか確認
# →ストップワードを定義
# →分割した配列にする
# →サンプルになぞってndaを構築
# →各トピックの頻度を取得
# DB保存までを行う

# あとはid5個連続で解析できれば問題なし
# ジャンルを求めるフローを確立
# 大量のidを取得する