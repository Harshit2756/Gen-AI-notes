import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

text = "Hello, world!"

tokens = enc.encode(text)
print(tokens)  # Output the token IDs

decoded_text = enc.decode(tokens)
print(decoded_text)  # Output the original text

# Output:
# [15496, 11, 995]
# Hello, world!