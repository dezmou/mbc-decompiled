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
}

;(async () => {
    // const file = fs.readFileSync("./compiled/MyBlockchainCorner.bin-runtime")
    // const file = fs.readFileSync("./compiled/MyEthereumCorner.bin-runtime")
    const compiled = (await bash(`solc MyBlokchainCorner.sol --optimize --bin-runtime`)).split("Binary of the runtime part: \n")[1]
    const pseudoCodeCompiled = (await bash(`python -m panoramix ${compiled}`))
    const pseudoCodeOriginal = (await bash(`python -m panoramix ${original}`))
    // console.log(res);
    console.log(pseudoCodeOriginal);
    console.log(pseudoCodeCompiled);
    console.log(pseudoCodeOriginal === pseudoCodeCompiled);
    // console.log(res);
    // console.log(file.length + " / 6612");

})()


