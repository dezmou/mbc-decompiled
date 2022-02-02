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

    const compiledOpcode = (await bash(`solc MyBlokchainCorner.sol --optimize --optimize-runs ${optimiseValue} --opcodes`))
    // const pseudoCodeCompiled = (await bash(`python -m panoramix ${compiled}`))
    // const pseudoCodeOriginal = (await bash(`python -m panoramix ${original}`))

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

    if (pseudoCodeOriginal !== pseudoCodeCompiled) {
        console.log("PSEUDO CODE NOT MATCHIN !");
    }

    // console.log(compiledOpcode);

})()


