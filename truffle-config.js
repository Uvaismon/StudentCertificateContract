const HDWalletProvider = require("truffle-hdwallet-provider");

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "5777",
    },
    rinkeby: {
      provider: () =>
        new HDWalletProvider(
          '1c0164ad06573657d2acaf250a6d7c55b30eb12562d2408cdfb618a108d0c295',
          'https://rinkeby.infura.io/v3/afb8a4a2e1274b8db453e3d621f137b3'
        ),
      network_id: 4,
      gas: 2100000,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
      from: '0x92BE98536C2DA43E09c1753069348C69601788e0',
    }
  }
};