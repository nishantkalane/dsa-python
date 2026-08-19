groups={

}
for word in ["cat","dog","cow","donkey","camel"]:
    groups.setdefault(word[0],[]).append(word)
print(groups)