import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'ed999cf6'.decode('hex')
P2P_PORT = 28639
ADDRESS_VERSION = 111
RPC_PORT = 28638
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'freicoin' in (yield bitcoind.rpc_help())
        ))
SUBSIDY_FUNC = lambda height: 50*100000000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'rFRC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Freicoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Freicoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.freicoin'), 'freicoin.conf')
BLOCK_EXPLORER_URL_PREFIX = '#'
ADDRESS_EXPLORER_URL_PREFIX = '#'
TX_EXPLORER_URL_PREFIX = '#'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
