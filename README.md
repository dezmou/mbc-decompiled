using this with solidity version 0.4.9

```
solc mbc.sol --bin-runtime -o compiled && node compare.js
```

the goal is to have the exact decompiled pseudo code as decompiled.py (py extension is just for IDE colors)

So it work, I recreated the contract and when I use panoramix to decompile it, it return the very exact pseudo code as the original contract

I am not able to submit it to etherscan because the bytecode contain a metadata hash from the source code ( commentary included) and the compiler version and optimization.

I obviously don't have those information 