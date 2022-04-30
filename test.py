import bz2, os, sys

filename_in = "C:\\Users\\hp\\Desktop\\Genki 1_ An Integrated Course in Elementary Japanese 1 ( PDFDrive ).pdf"
filename_out = ".\\compressed_data.bz2"

with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
    fout.write(fin.read())

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 48

with bz2.open(filename_out, "rb") as fin:
    data = fin.read()
    print(f"Decompressed size: {sys.getsizeof(data)}")
