from bitcoinlib.services.bitcoind import BitcoindClient
from pprint import pprint
import time

NETWORK = 'regtest'
RPC_CORE_URL = 'http://core:1234@localhost:18443'
RPC_ONGRID_URL = 'http://ongrid:1234@localhost:18453'
RPC_DEFINME_URL = 'http://definme:1234@localhost:18463'


def main():
    core = BitcoindClient(base_url=RPC_CORE_URL, network=NETWORK)
    ongrid = BitcoindClient(base_url=RPC_ONGRID_URL, network=NETWORK)
    definme = BitcoindClient(base_url=RPC_DEFINME_URL, network=NETWORK)
    print('Current blockheight is %d' % core.proxy.getblockcount())
    core_addr = core.proxy.getnewaddress()
    print('Mine 1 blocks and generate regtest coins to address %s' % core_addr)
    res = core.proxy.generatetoaddress(101, core_addr)
    print(f'addresses: {res}')
    print('Current blockheight is %d' % core.proxy.getblockcount())
    ongrid_addr = ongrid.proxy.getnewaddress()
    definme_addr = definme.proxy.getnewaddress()
    print('Send 10 rBTC to ongrid address %s' % ongrid_addr)
    print('Send 10 rBTC to definme address %s' % definme_addr)
    core.proxy.settxfee(0.00002500)
    ongrid_txid = core.proxy.sendtoaddress(ongrid_addr, 10)
    definme_txid = core.proxy.sendtoaddress(definme_addr, 10)
    print('Resulting ongrid txid: %s' % ongrid_txid)
    print('Resulting definme txid: %s' % definme_txid)
    ongrid_tx = core.proxy.gettransaction(ongrid_txid)
    definme_tx = core.proxy.gettransaction(definme_txid)
    pprint(ongrid_tx)
    pprint(definme_tx)
    print('------------------------')
    # pprint(ongrid.proxy.signrawtransactionwithkey(ongrid_tx['hex'], [core.proxy.dumpprivkey(core_addr), ongrid.proxy.dumpprivkey(ongrid_addr)]))
    # print(core.getbalance([core_addr]))


if __name__ == '__main__':
    main()
