import argparse


class ngram:
    def ngrams(self, sentence, num):
        characters_list = []
        sentence_length = len(sentence) - num + 1
        for i in range(sentence_length):
            characters = sentence[i:i+num]
            characters_list.append(characters)

        return characters_list


    def diff_ngram(self, sentence_a, sentence_b, num):
        characters_list_a = self.ngrams(sentence_a, num)
        characters_list_b = self.ngrams(sentence_b, num)
        match_list = []
        count = 0
        for characters_a in characters_list_a:
            for characters_b in characters_list_b:
                if characters_a == characters_b:
                    count += 1
                    match_list.append(characters_a)

        return count / len(characters_list_a), match_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence_a", help="input first sentence", type=str)
    parser.add_argument("sentence_b", help="input second sentence", type=str)
    parser.add_argument("num", help="input ngram number", type=int)
    args = parser.parse_args()
    c = ngram()
    similarity, match_list = c.diff_ngram(args.sentence_a, args.sentence_b,
                                          args.num)
    print(similarity, match_list)
