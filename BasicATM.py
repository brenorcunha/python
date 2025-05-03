def main():
    current_note = 100
    note_quantity = 0
    note_100 = 10
    note_50 = 20
    note_20 = 30
    note_10 = 50
    note_5 = 50
    note_2 = 80
    total_cash = (note_100 * 100) + (note_50 * 50) + (note_20 * 20) + (note_10 * 10) + (note_5 * 5) + (note_2 * 2)
    continue_withdrawal = 'Y'

    while continue_withdrawal == 'Y':
        withdrawal_amount = int(input("Enter an amount to withdrawn:\n"))
        total = withdrawal_amount
        while total > 0:
            if total <= total_cash:
                if current_note == 100 and total >=100 and note_100 > 0:
                    while total>=100 and note_100 > 0:
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total -= current_note
                        note_100 -= 1
                        total_cash-=current_note
                        print("Ejecting 100-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note = 50
                elif current_note == 100:
                    current_note=50
                elif current_note == 50 and total >=50 and note_50 > 0:
                    while total>=50 and note_50 > 0:
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total -= current_note
                        note_50 -= 1
                        total_cash-=current_note
                        print("Ejecting 50-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note=20
                elif current_note == 50:
                    current_note=20
                elif current_note == 20 and total>=20 and note_20 > 0:
                    while total >= 20 and note_20 > 0:
                        total -= current_note                 
                        note_20 -= 1
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total_cash-=current_note
                        print("Ejecting 20-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note=10
                elif current_note == 20:
                    current_note=10
                elif current_note == 10 and total >=10 and note_10 > 0:
                    while total >= 10 and note_10 > 0:
                        total -= current_note
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        total_cash-=current_note
                        note_10 -= 1
                        print("Ejecting 10-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note=5
                elif current_note == 10:
                    current_note=5
                elif current_note == 5 and total >= 5 and note_5>0:
                    while total >=5 and note_5 > 0:
                        total -= current_note
                        #print(f"Requires {note_quantity} notes of {current_note}")
                        note_5 -= 1
                        total_cash-=current_note
                        print("Ejecting 5-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note=2
                elif current_note == 5:
                    current_note=2
                elif current_note == 2 and total>=2 and note_2 > 0:
                    while total >= 2 and note_2 > 0:
                        total -= current_note
                        note_2 -= 1
                        total_cash-=current_note
                        print("Ejecting 2-note")
                    print(f"Remaining cache: {total_cash}")
                    current_note=100
                elif total <2 and total > 0:
                    print(f"The remain value cannot be paid: {total}")
                    print(f"Remaining cache: {total_cash}")
                    break
            else:
                print(f"The remain value cannot be paid: {total}")
                print(f"Remaining cache: {total_cash}")
                break
        if total==0:
            print(f"total: {total}")
            print(f"Remaining {note_100} 100-notes")
            print(f"Remaining {note_50} 50-notes")
            print(f"Remaining {note_20} 20-notes")
            print(f"Remaining {note_10} 10-notes")
            print(f"Remaining {note_5} 5-notes")
            print(f"Remaining {note_2} 2-notes")
            continue_withdrawal = input("Do you want to make more operations?: (Y/N)\n")
            if continue_withdrawal=='N':
                print("Thanks for using our ATM! See you next time.")
                break
if __name__ == "__main__":
    main()
