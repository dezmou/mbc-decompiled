## Recreating the source code of https://myblockchaincorner.com/ contract. 

When decompiling MyBlockchainCorner.sol with panoramix ( the tool used by etherscan to decompile contract)
It give the very exact pseudo code as when decompiling the original contract.

Having it to compile to the exact same bytecode is another issue I didn't manage to solve. even with trying every compiler possible with every optimization settings.
The bytecodes differences are little and seems always to be compiler optimization stuff.

Even if I managed to compile it to the exact same bytecode I still wouldn't be able to submit the source on etherscan because etherscan only accept compiler > 0.4.11 and this version didn't exist when original contract was deployed.

The original contract is 0x8C051C68D9601771CE96d4c9e971985aeDE480f7