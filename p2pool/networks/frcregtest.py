from p2pool.bitcoin import networks

PARENT = networks.nets['frcregtest']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'ca28fb0d612bac2f'.decode('hex')
PREFIX = 'd686bfb7e84b4abb'.decode('hex')
P2P_PORT = 29639
MIN_TARGET = 0
MAX_TARGET = 2**256 - 1
PERSIST = False
WORKER_PORT = 29638
BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#p2pool-rfrc'
VERSION_CHECK = lambda v: None if 12010000 <= v else 'Freicoin version too old. Upgrade to v12.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip34', 'bip66', 'locktime', 'blockfinal'])
MINIMUM_PROTOCOL_VERSION = 3200
NEW_MINIMUM_PROTOCOL_VERSION = 3301
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
