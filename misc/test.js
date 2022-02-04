const { EVM } = require("evm")
const original = require("./original")

const chien = new EVM(original)
console.log(chien.decompile());
