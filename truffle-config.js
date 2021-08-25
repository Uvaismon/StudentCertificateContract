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
          process.env.ACCOUNT_PRIVATE_KEY,
          `https://rinkeby.infura.io/v3/` + process.env.RINKEBY_KEY
        ),
      network_id: 4,
      gas: 5500000,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
    }
  }
};