chmod 755 ./unpacker.py
allparams=${@}
scl enable rh-python35 "./unpacker.py $allparams"
