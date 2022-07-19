// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "../node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdFeed;

    constructor(address _priceFeedAddress) {
        usdEntryFee = 50 * (10**18);
        ethUsdFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function getEntryPrice() public view returns (uint256) {
        (
            /*uint80 roundID*/,
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = ethUsdFeed.latestRoundData();
        
        uint256 adjustedPrice = uint256(price) * 10**10;
        uint256 entryCost = (usdEntryFee * 10 ** 18) / adjustedPrice;

        return entryCost;
    
    }


    function enter() public payable {
        //$50 minimum
        require(msg.value >= getEntryPrice(), "Not enough Eth!");
        players.push(payable(msg.sender));
    }

    function startLottery() public {}
    
    function endLottery() public {}
}