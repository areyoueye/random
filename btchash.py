import struct
import hashlib


'''
ref: http://blockexplorer.com/rawblock/000000000000000006ecee94daaa034bbd026cad52a9d3c6a5b7972716e5d566
'''

ver = 3
prev_block = "0000000000000000109b2a06d44012cf596b22e814aecf0952426d3ecd016cd1"
mrkl_root = "ff85fd9cd81784c63ffbacafc2a0d4c1e05d60fb0dcda13f1d7f9db7869216cf"
time = 1433194298
bits = 404167307
nonce = 3466471841

block = {}

block['ver'] = struct.pack('<I', ver).encode('hex')
block['prev_block'] =  "".join(reversed([prev_block[i:i+2] for i in range(0, len(prev_block), 2)]))
block['mrkl_root'] = "".join(reversed([mrkl_root[i:i+2] for i in range(0, len(mrkl_root), 2)]))
block['time'] = struct.pack('<I', time).encode('hex')
block['bits'] = struct.pack('<I', bits).encode('hex')
block['nonce'] = struct.pack('<I', nonce).encode('hex')

print block

header_hex = (block['ver'] + 
    block['prev_block'] +
    block['mrkl_root'] +
    block['time'] +
    block['bits'] +
    block['nonce'])

print header_hex

header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print "The hash"
print hash.encode('hex_codec')
print "Swap endian"
print hash[::-1].encode('hex_codec')
