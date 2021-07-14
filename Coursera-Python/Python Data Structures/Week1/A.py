text = "X-DSPAM-Confidence:    0.8475"

pos_space=text.find(' ')
pos_number=text[pos_space+4:]
print(float(pos_number))