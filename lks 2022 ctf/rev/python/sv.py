from base64 import encode


enc = (127, 122, 98, 98, 128, 122, 74, 11, 6, 82, 3, 84, 3, 11, 4, 5, 88, 88, 2, 7, 84, 87, 82, 5, 82, 88, 12, 6, 12, 2, 88, 8, 84, 8, 87, 12, 5, 88, 87, 80)

print(''.join([chr((i - 1) ^ 50) for i in enc]))

# LKSSMK{87c0a0816ee34adc6ce9793e5a5d96ed}