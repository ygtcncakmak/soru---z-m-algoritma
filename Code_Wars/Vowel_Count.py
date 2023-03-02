def get_count(sentence):
    sentence=list(sentence)
    vowel = "aeiou"
    vowel_count = 0
    for i in vowel:
        result= sentence.count(i)
        vowel_count+=result
    print(vowel_count)
    return vowel_count


get_count("aeiou")
