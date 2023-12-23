def baseN(num, b, numerals="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])



b = int(input("mabna mored nazar ra vared konid: "))
n = int(input("adad mored nazar ra vared konid: "))
print("adad {n} dar mabnaye {b} barabar ast ba => ({n}){b} = {f}".format(n = n,b =  b, f = baseN(n, b)))