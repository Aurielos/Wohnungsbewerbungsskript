# Nutzer gibt die Daten der Wohnungsbewerbung ein
name = input("Bitte geben Sie Ihren Namen ein: ")
ort = input("Bitte geben Sie den Ort der Wohnung ein: ")
datum = input("Bitte geben Sie das Datum ein: ")
wohnung_oder_haus = input("Handelt es sich um eine Wohnung oder ein Haus? ")
groeße: str = input("Bitte geben Sie die Größe der Wohnung/des Hauses in Quadratmetern ein: ")
anzahl_zimmer = input("Bitte geben Sie die Anzahl der Zimmer an: ")
Beruf = input("Bitte geben Sie ihren Beruf an: ")

nachricht = f"""""
Bewerbung für eine Wohnung

Sehr geehrte/r Vermieter/in,

hiermit bewerbe ich mich um die {wohnung_oder_haus} in {ort}. Die Wohnung/das Haus hat eine Größe von
{groeße} Quadratmetern und verfügt über {anzahl_zimmer} Zimmer. Ich bin an einem Mietbeginn zum {datum} interessiert.

Mit freundlichen Grüßen,
{name}
"""
