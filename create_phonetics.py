from dragonmapper import hanzi, transcriptions

hanziin = input("Enter characters: ")
pinzhus = input("Do you want Zhuyin, or Pinyin, or Both [Z/p/b]: ")
htmls = input("Do you want the HTML [y/N]: ")

zhuyin = True
pinyin = False
html = False
vertical = False
accented = False

htmltext = ""

zh_phons = ""
pi_phons = ""
phonperchar = []
hanzichars = []

phonpairs = []

if pinzhus == "z":
	pass
elif pinzhus == "p":
	zhuyin = False
	pinyin = True
elif pinzhus == "b":
	pinyin = True
if htmls == "y":
	html = True
if html:
	verticals = input("Vertical or horizontal [v/H]: ")
	if verticals == "v":
		vertical = True
if pinyin:
	accenteds = input("Accented Pinyin [y/N]: ")
	if accenteds == "y":
		accented = True


zh_phons = hanzi.to_zhuyin(hanziin).split(" ")
pi_phons = transcriptions.zhuyin_to_pinyin(hanzi.to_zhuyin(hanziin), accented=accented).split(" ")

if (zhuyin == True) and (pinyin == False):
	print("Zhuyin, no Pinyin")
	phonperchar = zh_phons
elif (pinyin == True) and (zhuyin == False):
	print("Pinyin, no Zhuyin")
	phonperchar = pi_phons
elif (zhuyin == True) and (pinyin == True):
	print("Both Zhuyin, and Pinyin")
	phonperchar = (pi_phons, zh_phons)

for i in hanziin:
	hanzichars.append(i)

print(zhuyin, pinyin)
print(hanzichars)
print(zh_phons)
print(pi_phons)
print(phonperchar)

if zhuyin and pinyin:
	for i in range(0, len(hanzichars)):
		phonpairs.append((hanzichars[i], phonperchar[0][i], phonperchar[1][i]))
else:
	for i in range(0, len(hanzichars)):
		phonpairs.append((hanzichars[i], phonperchar[i], phonperchar[i]))

print(phonpairs)

if zhuyin and not pinyin:
	print("Text in Zhuyin: {0}".format(zh_phons))
elif pinyin and not zhuyin:
	print("Text in Pinyin: {0}".format(pi_phons))
elif pinyin and zhuyin:
	print("Text in Zhuyin: {0}".format(zh_phons))
	print("Text in Pinyin: {0}".format(pi_phons))

if html:
	htmltext+="<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf8\">\n\t\t<link rel=\"stylesheet\" href=\"style.css\">\n\t</head>\n\t<body>\n"
	htmltext+="\t\t<table>\n\t\t\t<tbody>\n"
	if zhuyin and not pinyin:
		if vertical:
			for i in range(0, len(phonpairs)):
				htmltext+="\n\t\t\t\t<tr>"
				splitphons = ""
				for x in phonpairs[i][1]:
					splitphons+="{0}<br>".format(x)
				htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
				htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(splitphons)
				htmltext+="\n\t\t\t\t</tr>"
		else:
			htmltext+="\t\t\t\t<tr>"
			for i in range(0, len(phonpairs)):
				splitphons = ""
				for x in phonpairs[i][1]:
					splitphons+="{0}<br>".format(x)
				htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
				htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(splitphons)
			htmltext+="\n\t\t\t\t</tr>"
	elif pinyin and not zhuyin:
		htmltext+="\t\t\t\t<tr>"
		for i in range(0, len(phonpairs)):
			htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
		htmltext+="\n\t\t\t\t</tr>"
		htmltext+="\n\t\t\t\t<tr>"
		for i in range(0, len(phonpairs)):
			htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
		htmltext+="\n\t\t\t\t</tr>"
	elif pinyin and zhuyin:
		htmltext+="\t\t\t\t<tr>"
		for i in range(0, len(phonpairs)):
			splitphons = ""
			for x in phonpairs[i][2]:
				splitphons+="{0}<br>".format(x)
			htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
			htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(splitphons)
		htmltext+="\n\t\t\t\t</tr>"
		htmltext+="\n\t\t\t\t<tr>"
		for i in range(0, len(phonpairs)):
			htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
			htmltext+="\n\t\t\t\t\t<td></td>"
		htmltext+="\n\t\t\t\t</tr>"
	htmltext+="\n\t\t\t</tbody>\n\t\t</table>\n"
	htmltext+="\t</body>\n</html>"

print(htmltext)
