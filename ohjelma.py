a = int(input("Anna luku: "));
b = int(input("Anna toinen luku: "));

print("A:n arvo on", a, "ja B:n arvo on", b)
while(1):
	a = a * 3
	b = b + 10

	print("A:n arvo on", a, "ja B:n arvo on", b)

	if a > b:
		print("Game over")
		break
	elif a > 1000:
		print("Game over")
		break
	elif b > 1000:
		print("Game over")
		break
	
print("Heippa!")
