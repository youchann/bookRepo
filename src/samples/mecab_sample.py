# -*- coding: utf-8 -*-

import MeCab
import neologdn
from pprint import pprint


def get_stop_words():
    with open('/src/src/samples/Japanese.txt', encoding='utf-8') as fd:
        words = fd.read().splitlines()
        stop_words = frozenset(words)
    return stop_words

def analyze_review(review, stop_words):
    review = neologdn.normalize(review) # 正規化
    node = m.parseToNode(review)
    result = []
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in ['名詞', '動詞', '形容詞', '感動詞', '副詞']:
            result.append(node.surface)  # 語幹に変換
            # result.append(node.feature.split(",")[6]) # そのまま
        node = node.next

    result = list(filter(lambda x: x not in stop_words, result))
    return result


m = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
m.parse("")

all_reviews_result = []

# テキストファイルを開く(実際は配列にまとまったレビュー群がくるのが理想)
with open('/src/src/samples/sample_reviews1.txt', encoding='utf-8') as fh:
    stop_words = get_stop_words()
    for line in fh:
        one_review = line.strip()
        all_reviews_result.append(analyze_review(one_review, stop_words))

pprint(all_reviews_result)

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