s = '0123456789'
chuoisochan = [s[i] for i in range(len(s)) if int(s[i]) % 2 == 0]
chuoisole = [s[i] for i in range(len(s)) if int(s[i]) % 2 != 0]
print("Chuỗi con số chẵn là =", ''.join(chuoisochan))
print("Chuỗi con số lẻ là =", ''.join(chuoisole))