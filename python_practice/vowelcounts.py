def count_of_vowels(str):
    vowel_count =0
    
    for char in str:
        if char in "aeiouAEIOU":
            vowel_count +=1
    return vowel_count

count_of_vowels('test')