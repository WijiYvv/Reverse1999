def toNomal(titor):
    titor = titor.upper()
    res = []
    for i in range(0, len(titor), 2):
        num_hex = titor[i : i + 2]  # 每2个字符转换为1个十六进制数字
        num_ord = int(num_hex, 16)  # 把十六进制转换为十进制
        letter = chr(num_ord)  # 按照ascii表，把十进制数字转换为字母
        res.append(letter)
    return "".join(res)


def toTitor(nomal):
    nomal = list(nomal)
    res = []
    for i in range(len(nomal)):
        num_ord = ord(nomal[i])  # 把每个字母转换为十进制数字
        num_hex = hex(num_ord)[2:]  # 将十进制数字转换为十六进制
        res.append(num_hex)
    return "".join(res).upper()
