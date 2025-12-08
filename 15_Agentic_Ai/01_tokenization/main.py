import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Rahul Arya"
token = enc.encode(text)


# Token [25216, 3274, 0, 3673, 1308, 382, 161608, 107851, 64]
print("Token",token)

decoded = enc.decode( [25216, 3274, 0, 3673, 1308, 382, 161608, 107851, 64])
print("Decoded",decoded)
