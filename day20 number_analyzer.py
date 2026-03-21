numbers = []

while True:
    user = input("Enter Number or stop | ").strip().lower()
    if user == "stop":
        break

    try:
        num = float(user)
        numbers.append(num)
    except:
        print("Invalid Input Ignored.")

if numbers:
    total = sum(numbers)
    count =  len(numbers)
    avg = total / count
    print("\nStatistics")
    print("Total |", total)
    print("Count |", count)
    print("Average |", avg)
    print("Longest |", max(numbers))
    print("Shortest |", min(numbers))
else:
    print("Invalid Input Ignored.")
input("\nFeedback | ")