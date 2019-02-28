from mastodon import Mastodon
import re
import time

num = [1,2,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,49,50,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,90,91,98,99,101,102,103,104,105,106,107,109,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,130,131,132,133,134,135,140,141,142,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,171,173,174,175,176,178,180,199,310,320,322]
title = ["BIP Purpose and Guidelines", 
     "BIP process, revised", 
     "Version bits with lock-in by height", 
     "Version bits with timeout and delay",
     "Multi-Sig Transaction Distribution",
     "M-of-N Standard Transactions",
     "OP_EVAL",
     "Address Format for pay-to-script-hash",
     "Protocol Version and User Agent",
     "Aliases",
     "Pay to Script Hash",
     "OP_CHECKHASHVERIFY (CHV)",
     "hashScriptCheck",
     "M-of-N Standard Transactions (Low SigOp)",
     "URI Scheme",
     "URI Scheme",
     "getblocktemplate - Fundamentals",
     "getblocktemplate - Pooled Mining",
     "Duplicate transactions",
     "Pong message",
     "Hierarchical Deterministic Wallets",
     "Stratized Nodes",
     "Block v2, Height in Coinbase",
     "mempool message",
     "Custom Services",
     "Connection Bloom filtering",
     "Passphrase-protected private key",
     "Mnemonic code for generating deterministic keys",
     "Stratum wire protocol",
     "Stratum mining protocol",
     "A finite monetary supply for Bitcoin",
     "Purpose Field for Deterministic Wallets",
     "Multi-Account Hierarchy for Deterministic Wallets",
     "Structure for Deterministic P2SH Multisignature Wallets",
     "Reusable Payment Codes for Hierarchical Deterministic Wallets",
     "Derivation scheme for P2WPKH-nested-in-P2SH based accounts",
     "March 2013 Chain Fork Post-Mortem",
     'Fixed Length "version" Message (Relay-Transactions Field)',
     'Reject P2P message',
     'Dealing with malleability',
     'Stealth Addresses',
     'getutxo message',
     'OP_CHECKLOCKTIMEVERIFY',
     'Strict DER signatures',
     'Deterministic Pay-to-script-hash multi-signature addresses through public key sorting',
     'Relative lock-time using consensus-enforced sequence numbers',
     'Lexicographical Indexing of Transaction Inputs and Outputs',
     'Payment Protocol',
     'Payment Protocol MIME types',
     'bitcoin: uri extensions for Payment Protocol',
     'Use "Accept" header for response type negotiation with Payment Request URLs',
     'Allow zero value OP_RETURN in Payment Protocol',
     'Out of Band Address Exchange using Payment Protocol Encryption',
     'Bustapay :: a practical coinjoin protocol',
     'Hierarchy for Non-Colored Voting Pool Deterministic Multisig Wallets',
     'Hierarchy for Colored Voting Pool Deterministic Multisig Wallets',
     'Dynamic Hierarchical Deterministic Key Trees',
     'Derivation scheme for P2WPKH based accounts',
     'Buried Deployments',
     'Reduced threshold Segwit MASF',
     'Fast Merkle Trees',
     'Motivation and deployment of consensus rule changes ([soft/hard]forks)',
     'Increase maximum block size',
     'Block size increase to 2MB',
     'Block size following technological growth',
     "'Block75' - Max block size like difficulty",
     'Consensus based block size retargeting algorithm',
     'Dynamically Controlled Bitcoin Block Size Max Cap',
     'Dynamic limit on the block size',
     'Two million byte size limit with sigop and sighash limits',
     'NODE_BLOOM service bit',
     'CHECKSEQUENCEVERIFY',
     'Median time-past as endpoint for lock-time calculations',
     'Merkelized Abstract Syntax Tree',
     'Generic anti-replay protection using Script',
     'MERKLEBRANCHVERIFY',
     'Tail Call Execution Semantics',
     'SIGHASH_NOINPUT',
     'Proof of Payment',
     'Proof of Payment URI scheme',
     'URI scheme for Blockchain references / exploration',
     'BIP Classification',
     'Hierarchical Deterministic Script Templates',
     'Opt-in Full Replace-by-Fee Signaling',
     'Best Practices for Heterogeneous Input Script Transactions',
     'sendheaders message',
     '"Coalescing Transaction" Specification (wildcard inputs)',
     'Committee-based BIP Acceptance Process',
     'feefilter message',
     'Flexible Transactions',
     'Generalized version bits voting',
     'Normalized TXID',
     'Segregated Witness (Consensus layer)',
     'Address Format for Segregated Witness',
     'Transaction Signature Verification for Version 0 Witness Program',
     'Segregated Witness (Peer Services)',
     'getblocktemplate Updates for Segregated Witness',
     'Dealing with signature encoding malleability',
     'Dealing with dummy stack element malleability',
     'Mandatory activation of segwit deployment',
     'Segregated Witness (second deployment)',
     'Peer Authentication',
     'Peer-to-Peer Communication Encryption',
     'Compact Block Relay',
     'Rate Limiting via peer specified challenges',
     'Dandelion - Privacy Enhancing Routing',
     'Client Side Block Filtering',
     'Compact Block Filters for Light Clients',
     'NODE_NETWORK_LIMITED service bit',
     'Currency/exchange rate information API',
     'Base32 address format for native v0-16 witness outputs',
     'Partially Signed Bitcoin Transaction Format',
     'Pay to Contract Protocol',
     'Bits Denomination',
     'Version Extended WIF',
     'Block size/weight fraud proof',
     'Hashed Time-Locked Contract transactions',
     'Stratum protocol extensions',
     'nVersion bits for general purpose use',
     'Generic Signed Message Format'
     ]

BIP_Dict = dict(zip(num,title))

mastodon = Mastodon(
access_token = '[access token]',
api_base_url = '[mastodon instance]')

def check_for_notif():
 if len(mastodon.notifications()) < 1:
  return False
 else:
    return True
print(check_for_notif())

while True:
 while check_for_notif() == True:
  to_reply_to = dict(mastodon.notifications()[0]['status'])
  current_id = to_reply_to['id']
  BIP_string_test = to_reply_to['content'][-9:-4]
  print('bloop!')
  
  try:
   BIP_num = int(BIP_string_test.split()[1])
   str_BIP_num = (str(BIP_num)).rjust(4,'0')
   mastodon.status_post('BIP {}: {}\nhttps://github.com/bitcoin/bips/blob/master/bip-{}.mediawiki'.format(BIP_num,BIP_Dict[BIP_num],str_BIP_num), in_reply_to_id=current_id)
   mastodon.notifications_clear()
   print('Status Posted!')
  except:
   mastodon.status_post("That doesn't exist.", in_reply_to_id=current_id)
   mastodon.notifications_clear()
 time.sleep(30)