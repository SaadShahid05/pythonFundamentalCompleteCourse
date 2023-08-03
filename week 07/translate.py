message = "secret code is about to be written"
secret = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
print("'secret code is about to be written' has been translated as: ", message.translate(secret))