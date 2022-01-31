// SPDX-License-Identifier: MIT
pragma solidity ^0.4.9;

contract MyBlockchainCorner {
    address private owner;
    uint256 public cost;
    uint256 public percent;

    function pages(
        uint256 page,
        uint256 x,
        uint256 y
    ) public {
        if (x >= 4) throw;
        if (y >= 4) throw;
        // require(x < 4);
        // require(y < 4);
    }

    function updateCost(uint256 _newCost) public {
        if (owner != msg.sender) throw;
        cost = _newCost;
    }
}
