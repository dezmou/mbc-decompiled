const fs = require("fs");
const original = require("./original")
const { exec } = require("child_process");

const bash = (command) => {
    return new Promise(resolve => {
        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
            }
            resolve(stdout)
        });
    })
};

; (async () => {
    // const file = fs.readFileSync("./compiled/MyBlockchainCorner.bin-runtime")
    // const file = fs.readFileSync("./compiled/MyEthereumCorner.bin-runtime")
    const optimiseValue = 14;
    const compiled = (await bash(`solc MyBlokchainCorner.sol --optimize --optimize-runs ${optimiseValue} --bin-runtime`)).split("Binary of the runtime part: \n")[1]

    const [pseudoCodeCompiled, pseudoCodeOriginal] = await Promise.all([
        bash(`python -m panoramix ${compiled}`),
        bash(`python -m panoramix ${original}`)
    ])

    fs.writeFileSync("test_original.py", pseudoCodeOriginal, "utf-8");
    fs.writeFileSync("test_compiled.py", pseudoCodeCompiled, "utf-8");

    console.log("ORIGINAL : ", original.length);
    console.log(original);
    console.log()
    console.log("COMPILED : ", compiled.length);
    console.log(compiled);
    fs.writeFileSync("compared.txt", `${original}\n\n${compiled}`, "utf-8")

    console.log(pseudoCodeCompiled);

    const getUnwrapBuyTileAsm = async (binary, funcHash) => {
        let wrapper = "";
        const asm = (await bash(`echo "${binary.replace("\n", "")}" | evmasm -d`)).split("\n")
        let i = -1;
        do { i += 1 } while (asm[i].indexOf(funcHash) === -1)
        i += 2;
        const wrapperBegin = `00000${asm[i].split("0x")[1]}`;
        do { i += 1 } while (asm[i].indexOf(wrapperBegin) === -1)
        do {
            wrapper += `${asm[i]}\n`;
            i += 1
        } while (asm[i].indexOf("STOP") === -1 && asm[i].indexOf("RETURN") === -1)
        wrapper += `${asm[i]}\n`;
        return wrapper;
    }

    const [compiledWrapedBuyTile, originalWrapedBuyTile] = await Promise.all([
        getUnwrapBuyTileAsm(compiled, "0xc6030f4d"),
        getUnwrapBuyTileAsm(original, "0xc6030f4d"),
    ])

    console.log("Original wrapper :");
    console.log(originalWrapedBuyTile);
    console.log("Compiled  wrapper :");
    console.log(compiledWrapedBuyTile);



    if (pseudoCodeOriginal !== pseudoCodeCompiled) {
        console.log("PSEUDO CODE NOT MATCHIN !");
    }

})()


