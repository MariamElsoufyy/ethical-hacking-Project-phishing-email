def unpack_hex(val, length=8):
    # Convert number to bytes in little endian
    return list(val.to_bytes(length, 'little'))

# Secret (param_2)
secret = (
    unpack_hex(0x7b67737c51525045) +
    unpack_hex(0x7569, 2) +
    unpack_hex(0x68716a626675, 6) +
    unpack_hex(0x756f, 2) +
    unpack_hex(0x7e686d68766768)
)

# Mask (param_3)
mask = (
    unpack_hex(0x0502010103020302) +
    unpack_hex(0x0304, 2) +
    unpack_hex(0x010305030102, 6) +
    unpack_hex(0x0706, 2) +
    unpack_hex(0x0101ffff040203)
)

# Generate password
password = [chr((s - m) % 256) for s, m in zip(secret, mask)]

print("".join(password))
