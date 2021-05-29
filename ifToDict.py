a = "C"

def commonIf():
    # 10 linhas, ifs baseados em copy-paste
    if a == "a":
        return "it's lower"
    elif a == "b":
        return "it's lower, but it isn't a"
    elif a == "B":
        return "it's upper, but it isn't A"
    elif a == "A":
        return "it's upper"
    else:
        return "it isn't either aA or bB"

def niceIf():
    # 3 linhas, ifs baseados em keys de um dict.
    cases = {"a": "it's lower", "b": "it's lower, but it isn't a", "B": "it's upper, but it isn't A", "A": "it's upper"}
    try: return cases[a]
    except KeyError: return "it isn't either aA or bB"

print("a =", a)
print("common if =>", commonIf())
print("nice if =>", niceIf())