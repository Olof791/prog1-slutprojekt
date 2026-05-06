pass_val= {
    "Armpass": ["Preachercurl", "Sidedeltraises","Tricepexstension", "Inclinecurl"],
     "Pushpass": ["Hoist Inclinepress", "Pec deck", "Sidedeltraises", "Tricepexstension"],
     "Pullpass": ["Mid row", "Pulldowns", "Rear delt flyes", "Preachercurl"],
     "Benpass": ["Hack squat", "Leg extension", "Sittande leg curl", "Sittande vadpress"],
     "Upperpass": ["Mid row", "Hoist Inclinepress", "Pec deck", "Pulldowns", "Sidedeltraises", "Tricepexstension", "Preachercurl", "Rear delt flyes", "Inclinecurl"]
}

pass_idag = input("Vilket pass har du kört idag? (Armpass, Pushpass, Pullpass, Benpass) ")
if pass_idag in pass_val:
    övingar = pass_val[pass_idag]
    dagens_logg=[]

    print(f"{pass_idag}")

    for öving in övingar:
        print(f"Övning: {öving}")
        sets = input("Hur många set gjorde du? ")
        reps = input("Hur många reps gjorde du? ")
        vikt = input("Vilken vikt använde du? ")
        datum = input("Vad var datumet för passet?")

        dagens_logg.append({
            "övning": öving,
            "sets": sets,
            "reps": reps,
            "vikt": vikt,
            "datum": datum
        })

    print("\nDagens logg:")
    for logg in dagens_logg:
        print(f"Övning: {logg['övning']}, Sets: {logg['sets']}, Reps: {logg['reps']}, Vikt: {logg['vikt']} kg, Datum: {logg['datum']}")