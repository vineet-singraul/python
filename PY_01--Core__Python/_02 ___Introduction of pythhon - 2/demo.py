import string

spe_char = string.punctuation
print(spe_char)
print(len(spe_char))
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 32



# All Capital Latter
Capi_lat = string.ascii_uppercase
print(Capi_lat)
print(len(Capi_lat))
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 26


# All Small Latter
Smol_lat = string.ascii_lowercase
print(Smol_lat)
print(len(Smol_lat))


# All number Latter
num = string.digits
print(num)
print(len(num))


# All Hex nUMBER Latter
HEXA = string.hexdigits
print(HEXA)
print(len(HEXA))


# All Hex nUMBER Latter
octa = string.octdigits
print(octa)
print(len(octa))

# All Hex nUMBER Latter
Prtab = string.printable
print(Prtab)
print(len(Prtab))