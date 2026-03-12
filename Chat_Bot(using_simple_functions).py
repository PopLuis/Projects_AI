# ============================================
# CHATBOT MAGAZIN - Versiunea completă
# Nivel 1: if/else + dicționar + loop
# ============================================

def get_raspuns(mesaj,raspunsuri):
    mesaj = mesaj.lower().strip()
    for cuv_cheie, raspuns in raspunsuri.items():
        if cuv_cheie in mesaj:
            return raspuns

    return None

def main():
    raspunsuri = {
        "salut" : "Salut! Bine ai venit la Magazinul meu!",
        "buna": "Buna ziua! Cum pot sa vca ajut?",
        "pret": "Tricourile: 50 RON | Pantalonii: 120 RON | Rochii: 200 RON",
        "program": "Program: Luni-Vineri 9:00-18:00, Sâmbătă 10:00-14:00",
        "retur": "Retururile se acceptă în 30 de zile cu bon fiscal.",
        "livrare": "Livrare 2-3 zile lucrătoare. Gratuită peste 200 RON!",
        "contact": "Email: contact@magazin.ro | Tel: 0700 000 000",
        "ajutor": "Pot răspunde la: preț, program, retur, livrare, contact",
        "mulțumesc": "Cu plăcere! Mai pot ajuta cu ceva?",
        "multumesc": "Cu plăcere! Mai pot ajuta cu ceva?",
    }
    print("="*45)
    print("***ASISTENT MAGAZIN***")
    print("=" * 45)
    print("Bot: Bună! Scrie 'pa' sau 'exit' pentru a ieși.")
    print("Bot: Încearcă: preț, program, retur, livrare\n")
    while True:
        mesaj = input("Tu: ")
        if not mesaj.strip():
            continue

        if mesaj.lower() in ["pa","exit","quit"]:
            print("Bot: La revedere!")

        raspuns = get_raspuns(mesaj,raspunsuri)
        if raspuns:
            print(f"Bot:{raspuns}\n")
        else:
            print("Bot:Hmm, nu inteleg intrebarea!\n")

if __name__ == "__main__":
    main()

