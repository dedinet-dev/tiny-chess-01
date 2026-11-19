import lzma,sys
d=open(__file__,'rb').read()
exec(lzma.decompress(d[134:],format=lzma.FORMAT_RAW,filters=[{'id':lzma.FILTER_LZMA2}]))
