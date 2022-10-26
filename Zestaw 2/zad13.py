# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

tekst = "Lorem ipsum"
tekst = tekst.replace(",", "")
tekst = tekst.replace(".", "")
tekst = tekst.replace(" ", "")

print(len(tekst))