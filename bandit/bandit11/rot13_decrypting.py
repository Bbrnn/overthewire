string = "Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"

for abcd in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
	string = ''.join([abcd[(abcd.index(char) + 13) % 26] if char in abcd else char for char in string])

print(string)

