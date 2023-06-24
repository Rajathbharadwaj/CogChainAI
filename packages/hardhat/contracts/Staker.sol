pragma solidity >=0.6.0 <0.7.0;

import "hardhat/console.sol";
import "./ExampleExternalContract.sol";

contract Staker {
  ExampleExternalContract public exampleExternalContract;
  
  mapping(address => uint256) public balances; 
  mapping(address => uint256) public depositTimestamps;

  uint256 public constant rewardRatePerSecond = 0.1 ether; 
  uint256 public withdrawalDeadline = block.timestamp + 120 seconds; 
  uint256 public claimDeadline = block.timestamp + 240 seconds; 
  uint256 public currentBlock = 0;


  constructor(address exampleExternalContractAddress) public {
      exampleExternalContract = ExampleExternalContract(exampleExternalContractAddress);
  }
  
}