def main():
    current_note = 100
    note_quantity = 0
    note_100 = 0
    note_50 = 0
    note_20 = 0
    note_10 = 0
    note_5 = 20
    total_cash = (note_100 * 100) + (note_50 * 50) + (note_20 * 20) + (note_10 * 10) + (note_5 * 5)
    continue_withdrawal = 'Y'

    while continue_withdrawal == 'Y':
        withdrawal_amount = int(input("Enter an amount to withdraw:\n"))
        total = withdrawal_amount
        while True:
            if withdrawal_amount <= total_cash:
                if total >= current_note:
                    total -= current_note
                    note_quantity += 1
                else:
                    if current_note == 100 and note_100 == 0:
                        current_note = 50
                    elif current_note == 100 and note_100 > 0:
                        current_note = 50
                        note_100 = note_100 - note_quantity
                        print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 100-note")
                    elif current_note == 50 and note_50 == 0:
                        current_note = 20
                    elif current_note == 50 and note_50 > 0:
                        current_note = 20
                        note_50 = note_50 - note_quantity
                        print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 50-note")
                    elif current_note == 20 and note_20 == 0:
                        current_note = 10
                    elif current_note == 20 and note_20 > 0:
                        current_note = 10
                        note_20 = note_20 - note_quantity
                        print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 20-note")
                    elif current_note == 10 and note_10 == 0:
                        current_note = 5
                    elif current_note == 10 and note_10 > 0:
                        current_note = 5
                        note_10 = note_10 - note_quantity
                        print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 10-note")
                    elif current_note == 5 and note_5==0:
                        current_note = 50
                    elif current_note == 5 and note_5>0:
                        current_note = 50
                        note_5 = note_5 - note_quantity
                        print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 5-note")
                        
                    if total > 0 and total <5:
                        print("The remain value can´t be paid:",total)
                        break
                    if total == 0:
                        print(f"Remaining {note_100} 100-notes")
                        print(f"Remaining {note_50} 50-notes")
                        print(f"Remaining {note_20} 20-notes")
                        print(f"Remaining {note_10} 10-notes")
                        print(f"Remaining {note_5} 5-notes")
                        break
        else:
            print("This amount isn't available.")
        continue_withdrawal = input("Do you want to make more operations?: (Y/N)\n")
        
        
if __name__ == "__main__":
    main()
