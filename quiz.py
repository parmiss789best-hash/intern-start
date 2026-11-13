rules = {"hello": "سلام!", "bye": "خداحافظ!"}
print(rules["hello"])

rules["price"] = "ماهی 10 دلار"
print(len(rules))

msg = "  HeLLo "
word = msg.strip().lower()
print(word in rules, "time" in rules)
print(rules[word])
