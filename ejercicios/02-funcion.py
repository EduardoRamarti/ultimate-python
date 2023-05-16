def palin(text):
    if " " in text:
        text_trab = text.lower()
        text_trab = text_trab.replace(" ", "")
        reverse_text = text_trab[::-1]
        if reverse_text == text_trab:
            return True
        else:
            return False
    else:
        text_trab = text.lower()
        reverse_text = text_trab[::-1]
        if reverse_text == text_trab:
            return True
        else:
            return False


print("Hola adios Hola", palin("Hola adios hola"))
print("Abba", palin("Abba"))
print("Ojo mojo", palin("Ojo mojo"))
print("Amo la paloma", palin("Amo la paloma"))
print("Reconocer", palin("Reconocer"))
