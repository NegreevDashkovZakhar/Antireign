import { task } from "hardhat/config";
import { getContract } from "./helpers";

task("setUri", "Sets new base uri for ")
  .addParam("uri", "new contract base uri")
  .setAction(async function (taskArguments, hre) {
    const contract = await getContract("PixelTroopCard", hre);
    const transactionResponse = await contract.setBaseUri(taskArguments.uri, {
      gasLimit: 500_000,
    });
    console.log(`Transaction Hash: ${transactionResponse.hash}`);
  });
