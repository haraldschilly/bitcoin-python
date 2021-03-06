:mod:`bitcoinrpc.connection` --- Connect to Bitcoin server via JSON-RPC
====================================================================================

.. automodule:: bitcoinrpc.connection
   :show-inheritance:

.. autoclass:: bitcoinrpc.connection.BitcoinConnection


  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.accounts
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.balance
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.block_count
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.connection_count
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.difficulty
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.hashes_per_second
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.info
  .. autoattribute:: bitcoinrpc.connection.BitcoinConnection.is_generate
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.__init__(self, user, password, host='localhost', port=8332)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.backupwallet(self, destination)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getaccount(self, bitcoinaddress)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getaccountaddress(self, account)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getaddressesbyaccount(self, account)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getbalance(self, account=None, minconf=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getblock(self, hash)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getblockcount(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getblockhash(self, index)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getconnectioncount(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getdifficulty(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getgenerate(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.gethashespersec(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getinfo(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getnewaddress(self, account=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getreceivedbyaccount(self, account, minconf=1)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getreceivedbyaddress(self, bitcoinaddress, minconf=1)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.gettransaction(self, txid)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.getwork(self, data=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.listaccounts(self, minconf=1)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.listreceivedbyaccount(self, minconf=1, includeempty=False)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.listreceivedbyaddress(self, minconf=1, includeempty=False)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.listsinceblock(self, block_hash)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.listtransactions(self, account=None, count=10, address=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.move(self, fromaccount, toaccount, amount, minconf=1, comment=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.sendfrom(self, fromaccount, tobitcoinaddress, amount, minconf=1, comment=None, comment_to=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.sendmany(self, fromaccount, todict, minconf=1, comment=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.sendtoaddress(self, bitcoinaddress, amount, comment=None, comment_to=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.setaccount(self, bitcoinaddress, account)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.setgenerate(self, generate, genproclimit=None)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.stop(self)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.validateaddress(self, validateaddress)
  .. automethod:: bitcoinrpc.connection.BitcoinConnection.verifymessage(self, bitcoinaddress, signature, message)