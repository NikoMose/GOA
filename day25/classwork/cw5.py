def longer_word(word1, word2):
    if len(word1) > len(word2):
        print(word1)
    else:
        if len(word2) > len(word1):
            print(word2)
        else:
            print("booth Word lenghts  are equal:", word1)
