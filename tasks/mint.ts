import { task } from "hardhat/config";
import { getContract } from "./rinkebyHelpers";

task("mint", "Mints from the NFT contract")
  .addParam("address", "The address to receive a token")
  .setAction(async function (taskArguments, hre) {
    const contract = await getContract("PixelTroopCard", hre);
    const transactionResponse = await contract.mint({
      gasLimit: 500_000,
      value: 100000000000,
    });
    console.log(`Transaction Hash: ${transactionResponse.hash}`);
  });
