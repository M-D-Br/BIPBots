#BIPs
import tweepy
import time

ckey = '[consumer key from the Twitter API]'
csecret = '[consumer secret from the Twitter API]'
access_token = '[access token from the Twitter API]'
access_token_secret = '[secret access token from the Twitter API]'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


BIPDict = {1: 'BIP Purpose and Guidelines', 2: 'BIP process, revised', 8: 'Version bits with lock-in by height', 
9: 'Version bits with timeout and delay', 10: 'Multi-Sig Transaction Distribution', 
11: 'M-of-N Standard Transactions', 12: 'OP_EVAL', 13: 'Address Format for pay-to-script-hash', 
14: 'Protocol Version and User Agent', 15: 'Aliases', 16: 'Pay to Script Hash', 17: 'OP_CHECKHASHVERIFY (CHV)', 
18: 'hashScriptCheck', 19: 'M-of-N Standard Transactions (Low SigOp)', 20: 'URI Scheme', 21: 'URI Scheme', 
22: 'getblocktemplate - Fundamentals', 23: 'getblocktemplate - Pooled Mining', 30: 'Duplicate transactions', 
31: 'Pong message', 32: 'Hierarchical Deterministic Wallets', 33: 'Stratized Nodes', 34: 'Block v2, Height in Coinbase', 
35: 'mempool message', 36: 'Custom Services', 37: 'Connection Bloom filtering', 38: 'Passphrase-protected private key', 
39: 'Mnemonic code for generating deterministic keys', 40: 'Stratum wire protocol', 41: 'Stratum mining protocol', 
42: 'A finite monetary supply for Bitcoin', 43: 'Purpose Field for Deterministic Wallets', 
44: 'Multi-Account Hierarchy for Deterministic Wallets', 45: 'Structure for Deterministic P2SH Multisignature Wallets', 
47: 'Reusable Payment Codes for Hierarchical Deterministic Wallets', 49: 'Derivation scheme for P2WPKH-nested-in-P2SH based accounts', 
50: 'March 2013 Chain Fork Post-Mortem', 60: 'Fixed Length "version" Message (Relay-Transactions Field)', 61: 'Reject P2P message', 
62: 'Dealing with malleability', 63: 'Stealth Addresses', 64: 'getutxo message', 65: 'OP_CHECKLOCKTIMEVERIFY', 66: 'Strict DER signatures', 
67: 'Deterministic Pay-to-script-hash multi-signature addresses through public key sorting', 68: 'Relative lock-time using consensus-enforced sequence numbers', 
69: 'Lexicographical Indexing of Transaction Inputs and Outputs', 70: 'Payment Protocol', 71: 'Payment Protocol MIME types', 
72: 'bitcoin: uri extensions for Payment Protocol', 73: 'Use "Accept" header for response type negotiation with Payment Request URLs', 
74: 'Allow zero value OP_RETURN in Payment Protocol', 75: 'Out of Band Address Exchange using Payment Protocol Encryption', 
79: 'Bustapay :: a practical coinjoin protocol', 80: 'Hierarchy for Non-Colored Voting Pool Deterministic Multisig Wallets', 
81: 'Hierarchy for Colored Voting Pool Deterministic Multisig Wallets', 83: 'Dynamic Hierarchical Deterministic Key Trees', 
84: 'Derivation scheme for P2WPKH based accounts', 90: 'Buried Deployments', 91: 'Reduced threshold Segwit MASF', 
98: 'Fast Merkle Trees', 99: 'Motivation and deployment of consensus rule changes ([soft/hard]forks)', 101: 'Increase maximum block size', 
102: 'Block size increase to 2MB', 103: 'Block size following technological growth', 104: "'Block75' - Max block size like difficulty", 
105: 'Consensus based block size retargeting algorithm', 106: 'Dynamically Controlled Bitcoin Block Size Max Cap', 107: 'Dynamic limit on the block size', 
109: 'Two million byte size limit with sigop and sighash limits', 111: 'NODE_BLOOM service bit', 112: 'CHECKSEQUENCEVERIFY', 
113: 'Median time-past as endpoint for lock-time calculations', 114: 'Merkelized Abstract Syntax Tree', 115: 'Generic anti-replay protection using Script', 
116: 'MERKLEBRANCHVERIFY', 117: 'Tail Call Execution Semantics', 118: 'SIGHASH_NOINPUT', 120: 'Proof of Payment', 121: 'Proof of Payment URI scheme', 
122: 'URI scheme for Blockchain references / exploration', 123: 'BIP Classification', 124: 'Hierarchical Deterministic Script Templates', 
125: 'Opt-in Full Replace-by-Fee Signaling', 126: 'Best Practices for Heterogeneous Input Script Transactions', 130: 'sendheaders message', 
131: '"Coalescing Transaction" Specification (wildcard inputs)', 132: 'Committee-based BIP Acceptance Process', 133: 'feefilter message', 134: 'Flexible Transactions', 
135: 'Generalized version bits voting', 140: 'Normalized TXID', 141: 'Segregated Witness (Consensus layer)', 142: 'Address Format for Segregated Witness', 
143: 'Transaction Signature Verification for Version 0 Witness Program', 144: 'Segregated Witness (Peer Services)', 
145: 'getblocktemplate Updates for Segregated Witness', 146: 'Dealing with signature encoding malleability', 147: 'Dealing with dummy stack element malleability', 
148: 'Mandatory activation of segwit deployment', 149: 'Segregated Witness (second deployment)', 150: 'Peer Authentication', 151: 'Peer-to-Peer Communication Encryption', 
152: 'Compact Block Relay', 154: 'Rate Limiting via peer specified challenges', 156: 'Dandelion - Privacy Enhancing Routing', 157: 'Client Side Block Filtering', 
158: 'Compact Block Filters for Light Clients', 159: 'NODE_NETWORK_LIMITED service bit', 171: 'Currency/exchange rate information API', 
173: 'Base32 address format for native v0-16 witness outputs', 174: 'Partially Signed Bitcoin Transaction Format', 175: 'Pay to Contract Protocol', 176: 'Bits Denomination', 
178: 'Version Extended WIF', 180: 'Block size/weight fraud proof', 199: 'Hashed Time-Locked Contract transactions', 310: 'Stratum protocol extensions', 
320: 'nVersion bits for general purpose use', 322: 'Generic Signed Message Format'}



def get_first_hash(tag):
  for tweet in api.search(tag):
    return tweet.id

current_id_store = [get_first_hash("#blockchain")]

def get_last_hash(tag):
  for tweet in api.search(tag):
    if tweet.id > max(current_id_store):
       return tweet



def concat(user, dictnum, padding):
    return "@" + str(user) + " " + str(dictnum) + " " + "https://github.com/bitcoin/bips/blob/master/bip-" + str(padding) + ".mediawiki"

while True:
    current = get_last_hash("#BIPBot")
    if current is None:
        pass
    else:
        try:
            body = current.text[-3:].strip()
            identity = current.id
            you = current.user.screen_name
            k = int(body)
            try:
                api.update_status(status=(concat(you, BIPDict[k], body.rjust(4,'0'))), in_reply_to_status_id=identity)
                current_id_store.append(identity)
                print('Post success!')
            except:
                api.update_status(status=("@" + you + " Sorry, that's not a valid BIP."), in_reply_to_status_id=identity)
                current_id_store.append(identity)
                print('Post failure!')
        except:
            api.update_status(status=("@" + you + " Sorry, I couldn't understand you."), in_reply_to_status_id=identity)
            current_id_store.append(identity)
            print('Gibberish!')
    print('Zzzz')
    time.sleep(30)

