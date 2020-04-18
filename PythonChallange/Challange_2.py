# from string import maketrans
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"
coded = []
uncoded = []
for i in range(95, 123):
    coded += chr(i)

code = "".join(coded)

for x in range(97, 125):
    if x >= 123:
        x = x - 26
    uncoded += chr(x)

uncode = "".join(uncoded)

trantab = str.maketrans(code, uncode)
print(trantab)

print(text.translate(trantab))
