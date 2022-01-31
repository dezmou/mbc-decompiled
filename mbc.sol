// SPDX-License-Identifier: MIT
pragma solidity ^0.4.10;

contract MyBlockchainCorner {
    event SoldTile(
        uint256 page,
        uint256 x,
        uint256 y,
        address from,
        address to,
        uint256 price
    );

    event UpdatedTile(uint256 page, uint256 x, uint256 y, address owner, string html, uint256 price);

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
    }

    function setPrice(
        uint256 page,
        uint32 x,
        uint32 y,
        uint256 price
    ) public {
        if (pages[page][x][y].owner != msg.sender) throw;
        pages[page][x][y].price = price;
        UpdatedTile(page, x, y, pages[page][x][y].owner, pages[page][x][y].html, price);
    }
}


// SoldTile(
//     page,
//     x,
//     y,
//     pages[page][x][y].owner,
//     msg.sender,
//     pages[page][x][y].price
// );


// UpdatedTile(uint256,uint256,uint256,address,string,uint256)