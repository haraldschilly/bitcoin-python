# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Connect to Bitcoin server via JSON-RPC.
"""
from bitcoinrpc.proxy import JSONRPCException, AuthServiceProxy
from bitcoinrpc.exceptions import _wrap_exception
from bitcoinrpc.data import ServerInfo,AccountInfo,AddressInfo,TransactionInfo,AddressValidation,WorkItem

def checked(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return f(*args, **kwds)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
    return wrapper

class BitcoinConnection(object):
    """
    A BitcoinConnection object defines a connection to a bitcoin server.
    It is a thin wrapper around a JSON-RPC API connection.
    """
    @checked
    def __init__(self, user, password, host='localhost', port=8332):
        """
        Create a new bitcoin server connection.

        Arguments to this constructor:

        - ``user`` -- Authenticate as user.
        - ``password`` -- Authentication password.
        - ``host`` -- Bitcoin JSON-RPC host.
        - ``port`` -- Bitcoin JSON-RPC port.
        """
        url = 'http://%s:%s@%s:%s/' % (user, password, host, port)
        self.proxy = AuthServiceProxy(url)

    @checked
    def stop(self):
        """
        Stop bitcoin server.
        """
        self.proxy.stop()

    @checked
    def getblock(self, hash):
        """
        Returns the data of the block with the given ``hash``.
        """
        return self.proxy.getblock(hash)

    @checked
    def getblockcount(self):
        """
        Returns the number of blocks in the longest block chain.
        """
        return self.proxy.getblockcount()

    @checked
    def getblockhash(self, index):
        """
        Returns hash of block in best-block-chain at index.

        - ``index`` -- index of the block

        """
        return self.proxy.getblockhash(index)

    @checked
    def getblocknumber(self):
        """
        Returns the block number of the latest block in the longest block chain.
        """
        return self.proxy.getblocknumber()

    @checked
    def getconnectioncount(self):
        """
        Returns the number of connections to other nodes.
        """
        return self.proxy.getconnectioncount()

    @checked
    def getdifficulty(self):
        """
        Returns the proof-of-work difficulty as a multiple of the minimum difficulty.
        """
        return self.proxy.getdifficulty()

    @checked
    def getgenerate(self):
        """
        Returns ``True`` or ``False``, depending on whether generation is enabled.
        """
        return self.proxy.getgenerate()

    @checked
    def setgenerate(self, generate, genproclimit=None):
        """
        Enable or disable generation (mining) of coins.

        Arguments:

        - ``generate`` -- is ``True`` or ``False`` to turn generation on or off.
        - ``genproclimit`` -- Number of processors that are used for generation, -1 is unlimited.

        """
        if genproclimit is None:
            return self.proxy.setgenerate(generate)
        else:
           return self.proxy.setgenerate(generate, genproclimit)

    @checked
    def gethashespersec(self):
        """
        Returns a recent hashes per second performance measurement while generating.
        """
        return self.proxy.gethashespersec()

    @checked
    def getinfo(self):
        """
        Returns an :class:`~bitcoinrpc.data.ServerInfo` object containing various state info.
        """
        return ServerInfo(**self.proxy.getinfo())

    @checked
    def getnewaddress(self, account=None):
        """
        Returns a new bitcoin address for receiving payments.

        Arguments:

        - ``account`` -- If account is specified (recommended), it is added to the address book
          so that payments received with the address will be credited to it.

        """
        if account is None:
            return self.proxy.getnewaddress()
        else:
            return self.proxy.getnewaddress(account)

    @checked
    def getaccountaddress(self, account):
        """
        Returns the current bitcoin address for receiving payments to an account.

        Arguments:

        - ``account`` -- Account for which the address should be returned.

        """
        return self.proxy.getaccountaddress(account)

    @checked
    def setaccount(self, bitcoinaddress, account):
        """
        Sets the account associated with the given address.

        Arguments:

        - ``bitcoinaddress`` -- Bitcoin address to associate.
        - ``account`` -- Account to associate the address to.
        """
        return self.proxy.setaccount(bitcoinaddress, account)

    @checked
    def getaccount(self, bitcoinaddress):
        """
        Returns the account associated with the given address.

        Arguments:

        - ``bitcoinaddress`` -- Bitcoin address to get account for.
        """
        return self.proxy.getaccount(bitcoinaddress)

    @checked
    def getaddressesbyaccount(self, account):
        """
        Returns the list of addresses for the given account.

        Arguments:

        - `account` -- Account to get list of addresses for.
        """
        return self.proxy.getaddressesbyaccount(account)

    @checked
    def sendtoaddress(self, bitcoinaddress, amount, comment=None, comment_to=None):
        """
        Sends ``amount`` from the server's available balance to ``bitcoinaddress``.

        Arguments:

        - ``bitcoinaddress`` -- Bitcoin address to send to.
        - ``amount`` -- Amount to send (float, rounded to the nearest 0.01).
        - ``comment`` -- Comment for transaction.
        - ``comment_to`` -- Comment for to-address. (``comment`` needs to be specified, too!)
        """
        if comment is None:
            return self.proxy.sendtoaddress(bitcoinaddress, amount)
        elif comment_to is None:
            return self.proxy.sendtoaddress(bitcoinaddress, amount, comment)
        else:
            return self.proxy.sendtoaddress(bitcoinaddress, amount, comment, comment_to)

    @checked
    def getreceivedbyaddress(self, bitcoinaddress, minconf=1):
        """
        Returns the total amount received by a bitcoin address in transactions with at least a
        certain number of confirmations.

        Arguments:

        - ``bitcoinaddress`` -- Address to query for total amount.
        - ``minconf`` -- Number of confirmations to require, defaults to 1.
        """
        return self.proxy.getreceivedbyaddress(bitcoinaddress, minconf)

    @checked
    def getreceivedbyaccount(self, account, minconf=1):
        """
        Returns the total amount received by addresses with an account in transactions with
        at least a certain number of confirmations.

        Arguments:

        - ``account`` -- Account to query for total amount.
        - ``minconf`` -- Number of confirmations to require, defaults to 1.
        """
        return self.proxy.getreceivedbyaccount(account, minconf)

    @checked
    def gettransaction(self, txid):
        """
        Get detailed information about transaction

        Arguments:

        - ``txid`` -- Transactiond id for which the info should be returned

        """
        return TransactionInfo(**self.proxy.gettransaction(txid))

    @checked
    def listsinceblock(self, block_hash):
        """
        Lists :class:`~data.TransactionInfo` since given ``block_hash``.
        """
        res = self.proxy.listsinceblock(block_hash)
        res['transactions'] = [TransactionInfo(**x) for x in res['transactions']]
        return res

    @checked
    def listreceivedbyaddress(self, minconf=1, includeempty=False):
        """
        Returns a list of addresses.

        Each address is represented with a :class:`~bitcoinrpc.data.AddressInfo` object.

        Arguments:

        - ``minconf`` -- Minimum number of confirmations before payments are included.
        - ``includeempty`` -- Whether to include addresses that haven't received any payments.
        """
        return [AddressInfo(**x) for x in self.proxy.listreceivedbyaddress(minconf, includeempty)]

    @checked
    def listaccounts(self, minconf=1):
        """
        Returns a list of account names.

        Arguments:

        - ``minconf`` -- Minimum number of confirmations before payments are included.
        """
        return [x for x in self.proxy.listaccounts(minconf)]

    @checked
    def listreceivedbyaccount(self, minconf=1, includeempty=False):
        """
        Returns a list of accounts.

        Each account is represented with a :class:`~bitcoinrpc.data.AccountInfo` object.

        Arguments:

        - ``minconf`` -- Minimum number of confirmations before payments are included.
        - ``includeempty`` -- Whether to include addresses that haven't received any payments.
        """
        return [AccountInfo(**x) for x in self.proxy.listreceivedbyaccount(minconf, includeempty)]

    @checked
    def listtransactions(self, account=None, count=10, address=None):
        """
        Returns a list of the last transactions for an account.

        Each transaction is represented with a :class:`~bitcoinrpc.data.TransactionInfo` object.

        Arguments:

        - ``account`` -- If this parameter is specified, returns the balance in the account. (default: "")
        - ``count`` -- Number of transactions to return. (default: 10)
        - ``address`` -- Receive address to consider

        """
        if account is None: account = ""
        return [TransactionInfo(**x) for x in
             self.proxy.listtransactions(account, count)
             if address is None or x["address"] == address]

    @checked
    def backupwallet(self, destination):
        """
        Safely copies the ``wallet.dat`` file to ``destination``, which can be a directory or a path with filename.

        Arguments:

        - ``destination`` -- directory or path with filename to backup wallet to.
        """
        return self.proxy.backupwallet(destination)

    @checked
    def validateaddress(self, validateaddress):
        """
        Validate a bitcoin address and return information for it.

        The information is represented by a :class:`~bitcoinrpc.data.AddressValidation` object.

        Arguments:

        - ``validateaddress`` -- Address to validate.
        """
        return AddressValidation(**self.proxy.validateaddress(validateaddress))

    @checked
    def getbalance(self, account=None, minconf=None):
        """
        Get the current balance, either for an account or the total server balance.

        Arguments:

        - ``account`` -- If this parameter is specified, returns the balance in the account.
        - ``minconf`` -- Minimum number of confirmations required for transferred balance.
        """
        args = []
        if account:
            args.append(account)
            if minconf is not None:
                args.append(minconf)
        return self.proxy.getbalance(*args)

    @checked
    def move(self, fromaccount, toaccount, amount, minconf=1, comment=None):
        """
        Move from one account in your wallet to another.

        Arguments:

        - ``fromaccount`` -- Source account name.
        - ``toaccount`` -- Destination account name.
        - ``amount`` -- Amount to transfer.
        - ``minconf`` -- Minimum number of confirmations required for transferred balance.
        - ``comment`` -- Comment to add to transaction log.
        """
        if comment is None:
            return self.proxy.move(fromaccount, toaccount, amount, minconf)
        else:
            return self.proxy.move(fromaccount, toaccount, amount, minconf, comment)

    @checked
    def sendfrom(self, fromaccount, tobitcoinaddress, amount, minconf=1, comment=None, comment_to=None):
        """
        Sends amount from account's balance to bitcoinaddress. This method will fail
        if there is less than amount bitcoins with minconf confirmations in the account's
        balance (unless account is the empty-string-named default account; it
        behaves like the sendtoaddress method). Returns transaction ID on success.

        Arguments:

        - ``fromaccount`` -- Account to send from.
        - ``tobitcoinaddress`` -- Bitcoin address to send to.
        - ``amount`` -- Amount to send (float, rounded to the nearest 0.01).
        - ``minconf`` -- Minimum number of confirmations required for transferred balance.
        - ``comment`` -- Comment for transaction.
        - ``comment_to`` -- Comment for to-address.
        """
        if comment is None:
            return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf)
        elif comment_to is None:
            return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf, comment)
        else:
            return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf, comment, comment_to)

    @checked
    def sendmany(self, fromaccount, todict, minconf=1, comment=None):
        """
        Sends specified amounts from account's balance to bitcoinaddresses. This method will fail 
        if there is less than total amount bitcoins with minconf confirmations in the account's 
        balance (unless account is the empty-string-named default account; Returns transaction ID
        on success.

        Arguments:

        - ``fromaccount`` -- Account to send from.
        - ``todict`` -- Dictionary with Bitcoin addresses as keys and amounts as values.
        - ``minconf`` -- Minimum number of confirmations required for transferred balance.
        - ``comment`` -- Comment for transaction.
        """
        if comment is None:
            return self.proxy.sendmany(fromaccount, todict, minconf)
        else:
            return self.proxy.sendmany(fromaccount, todict, minconf, comment)

    @checked
    def verifymessage(self, bitcoinaddress, signature, message):
        """
        Verifies a signature given the bitcoinaddress used to sign,
        the signature itself, and the message that was signed.
        Returns ``True`` if the signature is valid, and ``False`` if it is invalid.

        Arguments:

        - ``bitcoinaddress`` -- the bitcoinaddress used to sign the message
        - ``signature`` -- the signature to be verified
        - ``message`` -- the message that was originally signed
        """
        return self.proxy.verifymessage(bitcoinaddress,signature,message)

    @checked
    def getwork(self, data=None):
        """
        Get work for remote mining, or submit result.
        If data is specified, the server tries to solve the block
        using the provided data and returns :const:`True` if it was successful.
        If not, the function returns formatted hash data (:class:`~bitcoinrpc.data.WorkItem`)
        to work on.

        Arguments:

        - ``data`` -- Result from remote mining.
        """
        if data is None:
            # Only if no data provided, it returns a WorkItem
            return WorkItem(**self.proxy.getwork())
        else:
            return self.proxy.getwork(data)
