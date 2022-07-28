const { ethers } = require("ethers");
const { getContractAt } = require("@nomiclabs/hardhat-ethers/internal/helpers");

// Helper method for fetching environment variables from .env
function getEnvVariable(key, defaultValue) {
  if (process.env[key]) {
    return process.env[key];
  }
  if (!defaultValue) {
    throw `${key} is not defined and no default value was provided`;
  }
  return defaultValue;
}

// Helper method for fetching a connection provider to the Ethereum network
function getProvider() {
  return ethers.getDefaultProvider(getEnvVariable("NETWORK", "rinkeby"), {
    rinkeby: {
      url: `https://rinkeby.infura.io/v3/${getEnvVariable(
        "INFURA_PROJECT_ID",
      )}`,
      chainId: 4,
    },
  });
}

// Helper method for fetching a wallet account using an environment variable for the PK
function getAccount() {
  let wallet = ethers.Wallet.fromMnemonic(getEnvVariable("MNEMONIC"));
  wallet = wallet.connect(getProvider());
  return wallet;
}

// Helper method for fetching a contract instance at a given address
export function getContract(contractName, hre) {
  const account = getAccount();
  return getContractAt(
    hre,
    contractName,
    getEnvVariable("NFT_CONTRACT_ADDRESS"),
    account,
  );
}
