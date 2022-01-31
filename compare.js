const fs = require("fs");
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
    const file = fs.readFileSync("./compiled/mbc.sol:MyBlockchainCorner.bin-runtime")
    const res = (await bash(`python -m panoramix ${file}`))
    console.log(res);
})()


