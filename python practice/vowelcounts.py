def count_of_vowels(input_str):
    vowel_count =0
    print(input_str)
    for char in input_str:
        if char in "e":
            vowel_count +=1
    print(vowel_count)

count_of_vowels("test")