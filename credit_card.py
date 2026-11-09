def luhn_check(card_number):
    
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False

    digits = [int(digit) for digit in card_number[::-1]]

    total = 0

    for i in range(len(digits)):

        digit = digits[i]

        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit -= 9

        total += digit

    # Valid if total is divisible by 10
    return total % 10 == 0



print("=== CREDIT CARD VALIDATOR ===")

card = input("Enter card number: ")

if luhn_check(card):
    print("Result: VALID card number!")
else:
    print("Result: INVALID card number!")