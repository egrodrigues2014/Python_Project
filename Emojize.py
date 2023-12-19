#Emojize

import emoji

answer = [":1st_place_medal:", ":money_bag:", ":smile_cat:"]

for item in answer:
    output = emoji.emojize(item)
    print("Output:", output)