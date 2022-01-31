// SPDX-License-Identifier: MIT
pragma solidity ^0.4.10;

contract MyBlockchainCorner {
    struct Tile {
        address owner;
        string html;
        uint256 price;
    }
    address private owner;
    uint256 public cost;
    uint256 public percent;
    mapping(uint256 => Tile[4][4]) public pages;

    function contractBalance() returns (uint256) {
        if (owner != msg.sender) throw;
        return address(this).balance;
    }

    function updateCost(uint256 _newCost) public {
        if (owner != msg.sender) throw;
        cost = _newCost;
    }

    function updateOwner(address _owner) public {
        if (owner != msg.sender) throw;
        owner = _owner;
    }

    function updatePercent(uint256 _percent) public {
        if (owner != msg.sender) throw;
        percent = _percent;
    }

    function withdraw() public {
        if (owner != msg.sender) throw;
        owner.transfer(this.balance);
        // owner.call({value: address(this).balance}(""));
    }
}
