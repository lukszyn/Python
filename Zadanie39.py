import re

tekst = input("Podaj ciag znakow: ")
szablon = '^[axyb]{2,8}$'
try:
    dopasowanie = re.match(szablon, tekst).group()
    print("Napis pasuje do szablonu")
except (TypeError, AttributeError):
    print("Napis nie pasuje do szablonu")