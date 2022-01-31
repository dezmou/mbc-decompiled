// SPDX-License-Identifier: MIT
pragma solidity ^0.4.9;

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
    // Tile[][4][4] public pages;
    // mapping(uint256 => mapping(uint32 => mapping(uint32 => Tile))) public pages;

    // function pages(
    //     uint256 page,
    //     uint256 x,
    //     uint256 y
    // ) public returns(uint256) {
    //     if (x >= 4) throw;
    //     if (y >= 4) throw;
    //     Tile chien = tiles[page][uint32(x)][uint32(y)];
    //     // Tile chien = tiles[page][uint32(x)][uint32(y)];
    //     // return chien.chiengruel;
    //     return chien.chiengruel;
    // }

    function updateCost(uint256 _newCost) public {
        if (owner != msg.sender) throw;
        cost = _newCost;
    }

    function updatePercent(uint256 _percent) public {
        if (owner != msg.sender) throw;
        percent = _percent;
    }
}
