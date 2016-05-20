from dragonmapper import hanzi, transcriptions
import sys, getopt

verbose = False

def usage():
	print("-----------------------------------------------")
	print("Usage:\npython3 create_phonetics.py [OPTIONS]")
	print("OPTIONS:")
	print("-z, --zhuyin adds Zhuyin")
	print("-p, --pinyin adds Pinyin")
	print("-v, --vertical makes text vertical in HTML")
	print("-m, --markup outputs HTML")
	print("-t, --text outputs text")
	print("-a, --accented makes Pinyin accented [as oppossed to numbered]")
	print("-o, --ontop places phonetics on top of character [only works with one phonetic system]")
	print("-i --input \"chinese string\"")
	print("-h, --help this help menu")
	print("--verbose for debuging (must be placed first)")
	print("-----------------------------------------------")

def verbose_print(s):
	if verbose:
		print(s)
	else:
		pass

try:
	opts, args = getopt.getopt(sys.argv[1:], "i:zopvmhta", ["help", "input=", "markup", "vertical", "zhuyin", "pinyin", "accented", "verbose", "ontop", "text"])
except getopt.GetoptError as err:
	# print help information and exit:
	print(err) # will print something like "option -a not recognized"
	usage()
	sys.exit(2)

hanziin = ""

zhuyin = False
pinyin = False
html = False
vertical = False
accented = False
ontop = False
text = False

for o, a in opts:
	verbose_print(o+" | "+a)
	if o == "-z" or o == "--zhuyin":
		zhuyin = True;
	elif o == "-p" or o == "--pinyin":
		pinyin = True
	elif o == "-m" or o == "--markup":
		html = True
	elif o == "-t" or o == "--text":
		text = True
	elif o == "-v" or o == "--vertical":
		vertical = True
	elif o == "-a" or o == "--accented":
		accented = True
	elif o == "-o" or o == "--ontop":
		ontop = True
	elif o == "-i" or o == "--input":
		hanziin = a
		verbose_print(a+" "+hanziin)
	elif o == "-h" or o == "--help":
		usage()
		exit(0)
	elif o == "--verbose":
		verbose = True
	else:
		print(err)
		usage()

htmltext = ""

zh_phons = ""
pi_phons = ""
phonperchar = []
hanzichars = []

phonpairs = []

zh_phons = hanzi.to_zhuyin(hanziin).split(" ")
pi_phons = transcriptions.zhuyin_to_pinyin(hanzi.to_zhuyin(hanziin), accented=accented).split(" ")

if (zhuyin == True) and (pinyin == False):
	verbose_print("Zhuyin, no Pinyin")
	phonperchar = zh_phons
elif (pinyin == True) and (zhuyin == False):
	verbose_print("Pinyin, no Zhuyin")
	phonperchar = pi_phons
elif (zhuyin == True) and (pinyin == True):
	verbose_print("Both Zhuyin, and Pinyin")
	phonperchar = (pi_phons, zh_phons)
elif not zhuyin and not pinyin:
	print("\nERROR: NO PHONETIC SYSTEM SPECIFIED!\n")
	usage()
	exit(2)

for i in hanziin:
	hanzichars.append(i)

verbose_print(zhuyin)
verbose_print(pinyin)
verbose_print(hanzichars)
verbose_print(zh_phons)
verbose_print(pi_phons)
verbose_print(phonperchar)

if zhuyin and pinyin:
	for i in range(0, len(hanzichars)):
		phonpairs.append((hanzichars[i], phonperchar[0][i], phonperchar[1][i]))
else:
	for i in range(0, len(hanzichars)):
		phonpairs.append((hanzichars[i], phonperchar[i], phonperchar[i]))

verbose_print(phonpairs)

if zhuyin:
	print("Text in Zhuyin: {0}".format(" ".join(zh_phons)))
if pinyin:
	print("Text in Pinyin: {0}".format(" ".join(pi_phons)))

if html:
	htmltext+="<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf8\">\n\t\t<link rel=\"stylesheet\" href=\"style.css\">\n\t</head>\n\t<body>\n"
	htmltext+="\t\t<table>\n\t\t\t<tbody>\n"
	if ontop:
		if zhuyin:
			if vertical:
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
					htmltext+="\n\t\t\t\t</tr>"
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
					htmltext+="\n\t\t\t\t</tr>"
			elif not vertical:
				htmltext+="\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
				htmltext+="\n\t\t\t\t</tr>"
				htmltext+="\n\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
				htmltext+="\n\t\t\t\t</tr>"
		elif pinyin:
			if vertical:
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
					htmltext+="\n\t\t\t\t</tr>"
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
					htmltext+="\n\t\t\t\t</tr>"
			elif not vertical:
				htmltext+="\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
				htmltext+="\n\t\t\t\t</tr>"
				htmltext+="\n\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
				htmltext+="\n\t\t\t\t</tr>"
	else:
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
			elif not vertical:
				htmltext+="\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					splitphons = ""
					for x in phonpairs[i][1]:
						splitphons+="{0}<br>".format(x)
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
					htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(splitphons)
				htmltext+="\n\t\t\t\t</tr>"
		elif pinyin and not zhuyin:
			if vertical:
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
					htmltext+="\n\t\t\t\t</tr>"
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
					htmltext+="\n\t\t\t\t</tr>"
			elif not vertical:
				htmltext+="\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
				htmltext+="\n\t\t\t\t</tr>"
				htmltext+="\n\t\t\t\t<tr>"
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
				htmltext+="\n\t\t\t\t</tr>"
		elif pinyin and zhuyin:
			if vertical:
				for i in range(0, len(phonpairs)):
					htmltext+="\n\t\t\t\t<tr>"
					splitphons = ""
					for x in phonpairs[i][2]:
						splitphons+="{0}<br>".format(x)
					htmltext+="\n\t\t\t\t\t<td class=\"hanzi\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][0])
					htmltext+="\n\t\t\t\t\t<td class=\"zhuyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(splitphons)
					htmltext+="\n\t\t\t\t</tr>"
					htmltext+="\n\t\t\t\t<tr>"
					htmltext+="\n\t\t\t\t\t<td class=\"pinyin\">\n\t\t\t\t\t\t<span>{0}</span>\n\t\t\t\t\t</td>".format(phonpairs[i][1])
					htmltext+="\n\t\t\t\t</tr>"
			elif not vertical:
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
