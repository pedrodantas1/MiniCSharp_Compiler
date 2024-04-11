with open("SintaxeAbstrata.py", "r") as f:
    lines = [line.rstrip() for line in f]


saida = []
for line in lines:
    if "visitor.visit" in line:
        index = line.find(".visit")
        string = line[index + 1 :]
        aux = string.split(")")
        insertString = string.split("visit")[1].split("(self)")[0].lower()
        if "concrete" in insertString:
            insertString = insertString.split("concrete")[0]
        aux.insert(0, "def ")
        aux.insert(-1, f", {insertString}): pass\n")
        aux.insert(0, "\n@abstractmethod\n")
        saida.append("".join(aux))

print(len(saida))


with open("saida.txt", "w") as f:
    f.writelines(saida)
