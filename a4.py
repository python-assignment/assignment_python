str1=input("enter comma separated words")
words=[word for word in str1.split(",")]
print(words)
print(",".join(sorted(list(set(words)))))
