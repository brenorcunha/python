def main():
    current_note = 100
    note_quantity = 0
    note_100 = 5
    note_50 = 5
    note_20 = 5
    note_10 = 5
    note_5 = 20
    note_2 = 60
    total_cash = (note_100 * 100) + (note_50 * 50) + (note_20 * 20) + (note_10 * 10) + (note_5 * 5) + (note_2 * 2)
    continue_withdrawal = 'Y'

    while continue_withdrawal == 'Y':
        withdrawal_amount = int(input("Enter an amount to withdraw:\n"))
        total = withdrawal_amount
        while True:
            if withdrawal_amount <= total_cash:
                if current_note == 100 and note_100 == 0:
                    current_note = 50
                elif current_note == 100 and note_100 > 0:
                    if total>=100:
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total -= current_note
                        note_quantity += 1
                        current_note = 50
                        note_100 -= note_quantity
                        print("Ejecting 100-note")
                    else:
                        current_note = 50
                elif current_note == 50 and note_50 == 0:
                    current_note = 20
                elif current_note == 50 and note_50 > 0:
                    if total>=50:
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total -= current_note
                        note_quantity += 1
                        current_note = 20
                        note_50 -= note_quantity
                        print("Ejecting 50-note")
                    else:
                        current_note=20
                elif current_note == 20 and note_20 == 0:
                    current_note = 10
                elif current_note == 20 and note_20 > 0:
                    if total >= 20:
                        total -= current_note
                        current_note = 10
                        note_20 -= note_quantity
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        print("Ejecting 20-note")
                    else:
                        current_note=10
                elif current_note == 10 and note_10 == 0:
                    current_note = 5
                elif current_note == 10 and note_10 > 0:
                    if total >= 10:
                        total -= current_note
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        current_note = 5
                        note_10 = note_10 - note_quantity
                        print("Ejecting 10-note")
                    else:
                        current_note=5
                elif current_note == 5 and note_5==0:
                    current_note = 2
                elif current_note == 5 and note_5>0:
                    if total >=5:
                        total -= current_note
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        current_note = 2
                        note_5 -= note_quantity
                        print("Ejecting 5-note")
                    else:
                        current_note=2
                elif current_note == 2 and note_2 > 0:
                    if total >= 2:
                        total -= current_note
                        current_note=100
                        note_2 -= note_quantity
                        print("Ejecting 2-note")
                        
                if total > 0 and total <2:
                    print("The remain value can´t be paid:",total)
                    break
                if total == 0:
                    print(f"Remaining {note_100} 100-notes")
                    print(f"Remaining {note_50} 50-notes")
                    print(f"Remaining {note_20} 20-notes")
                    print(f"Remaining {note_10} 10-notes")
                    print(f"Remaining {note_5} 5-notes")
                    print(f"Remaining {note_2} 2-notes")
                    break
        else:
            print("This amount isn't available.")
        continue_withdrawal = input("Do you want to make more operations?: (Y/N)\n")
        
        
if __name__ == "__main__":
    main()
