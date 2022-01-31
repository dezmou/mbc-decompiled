using this with solidity version 0.4.9

```
solc mbc.sol --bin-runtime -o compiled && node compare.js
```

the goal is to have the exact decompiled pseudo code as decompiled.py