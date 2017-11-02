"""Counting Vowels."""

text = input("dame un texto plz\n")

counter = 0
for pos in range(0,len(text)):
    if text[pos:pos+3] == "bob":
    	counter += 1

print('hay', counter, ' bobs en:', text)