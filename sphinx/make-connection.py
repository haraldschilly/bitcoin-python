#!/usr/bin/env python
# This small script generates the explicit entries for the sphinx documentation
# of connection.py. 
# Automatic inclusion works, including the documentation, but unfortunately the method
# signatures are lost :(

import os, re

# be relative to this file
os.chdir(os.path.abspath(os.path.dirname(__file__)))

intro = """\
:mod:`bitcoinrpc.connection` --- Connect to Bitcoin server via JSON-RPC
====================================================================================

.. automodule:: bitcoinrpc.connection
   :show-inheritance:

.. autoclass:: bitcoinrpc.connection.BitcoinConnection

"""

docentry = '  .. automethod:: bitcoinrpc.connection.BitcoinConnection.'

output = [ intro ]

pat = re.compile(r'^\s+def ')
sig = re.compile(r'def (\w+\([^)]+\))')

for line in open(os.path.join('..', 'src', 'bitcoinrpc', 'connection.py')).readlines():
  if pat.match(line) and 'def wrapper(' not in line:
    signature = sig.findall(line)
    print 'Signature:', signature[0]
    output.append(docentry + signature[0])

with open(os.path.join('source', 'bitcoinrpc.connection.rst'), 'w') as out:
  out.write('\n'.join(output))
