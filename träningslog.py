pass_val= {
    "Armpass": ["Preachercurl", "Sidedeltraises","Tricepexstension", "Inclinecurl"],
     "Pushpass": ["Incline dumbellpress", "Pec deck", "Sidedeltraises", "Tricepexstension"],
     "Pullpass": ["Mid row", "Pulldowns", "Rear delt flyes", "Preachercurl"],
     "Benpass": ["Hack squat", "Leg extension", "Sittande leg curl", "Sittande vadpress"]
}

pass_idag = input("Vilket pass har du kört idag? (Armpass, Pushpass, Pullpass, Benpass) ")
if pass_idag in pass_val:
    övingar = pass_val[pass_idag]
    