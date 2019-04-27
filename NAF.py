import sys

ip_addr = str(input("Введите ip адрес: "))
if ip_addr.count(".") != 3:
    sys.exit("[Ошибка] Неправильный формат ip адреса.")
mask = str(input("Введите маску сети: "))
if mask.count(".") != 3:
    sys.exit("[Ошибка] Неправильный формат маски")
print("_____________________________________________________________________")
print("")
net_addr: str
ip_mas: list = []
mask_mas: list = []
net_mas: list = [0, 0, 0, 0]
dot = 0


def ip_splitter(ip):
    def ip_double(a):
        s = ""
        global ip_mas
        while a > 1:
            s = s + str(a % 2)
            a //= 2
        s = s + str(a)
        ip_mas.append(s[::-1])

    global dot
    while dot != -1:
        dot = ip.find(".")
        if dot == -1:
            break
        a = int(ip[0:dot])
        ip = ip[dot + 1:]
        ip_double(a)
    a = int(ip)
    ip_double(a)
    dot = 0


def mask_splitter(m):
    def mask_double(a):
        s = ""
        global mask_mas
        while a > 1:
            s = s + str(a % 2)
            a //= 2
        s = s + str(a)
        mask_mas.append(s[::-1])

    global dot
    while dot != -1:
        dot = m.find(".")
        if dot == -1:
            break
        a = int(m[0:dot])
        m = m[dot + 1:]
        mask_double(a)
    a = int(m)
    mask_double(a)
    dot = 0


def mask_formater(f):
    global mask_mas, i
    if len(f) < 8:
        n = 8 - len(f)
        f = "0" * n + f
        mask_mas[i] = f


def ip_formater(g):
    global ip_mas, i
    if len(g) < 8:
        n = 8 - len(g)
        g = "0" * n + g
        ip_mas[i] = g


def net_formater(h):
    global net_mas, i
    if len(h) < 8:
        n = 8 - len(h)
        h = "0" * n + h
        net_mas[i] = h


ip_splitter(ip_addr)
mask_splitter(mask)

free: list = []

for i in range(0, 4):
    if mask_mas[i] == "0" or ip_mas[i] == "0":
        net_mas[i] = "0"
    elif mask_mas[i] == "11111111":
        net_mas[i] = ip_mas[i]
    elif ip_mas[i] == "11111111":
        net_mas[i] = mask_mas[i]
    else:
        free.append(i)
    mask_formater(mask_mas[i])
    ip_formater(ip_mas[i])

print("Двоичная запись ip адреса: ", ip_mas[0], ".", ip_mas[1], ".", ip_mas[2], ".", ip_mas[3], sep="")
print("Двоичная запись маски: ", mask_mas[0], ".", mask_mas[1], ".", mask_mas[2], ".", mask_mas[3], sep="")
print("_____________________________________________________________________")
print("")

nm = ""

if len(free) != 0:
    for i in free:
        nm = ""
        mm = mask_mas[i]
        im = ip_mas[i]
        for k in range(0, 8):
            nm += str(int(mm[k]) * int(im[k]))
        net_mas[i] = nm
for i in range(0, 4):
    net_formater(net_mas[i])

print("Двоичная запись адреса сети: ", net_mas[0], ".", net_mas[1], ".", net_mas[2], ".", net_mas[3], sep="")
print("_____________________________________________________________________")
print("")

c = 1

for i in range(0, 4):
    nm = net_mas[i]
    net_mas[i] = 0
    for k in range(0, 8):
        if k == 8:
            c = 0
        net_mas[i] += int(nm[k]) * (2 ** (len(nm) - k - c))

print("Адрес сети: ", net_mas[0], ".", net_mas[1], ".", net_mas[2], ".", net_mas[3], sep="")
