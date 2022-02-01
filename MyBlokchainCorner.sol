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

    event UpdatedTile(
        uint256 page,
        uint256 x,
        uint256 y,
        address owner,
        string html,
        uint256 price
    );

    struct Tile {
        address owner;
        string html;
        uint256 price;
    }
    address private owner;
    uint256 public cost;
    uint256 public percent = 5;
    mapping(uint256 => Tile[4][4]) public pages;

    function MyBlockchainCorner() public {
        owner = msg.sender;
    }

    function() public payable {}

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
        UpdatedTile(
            page,
            x,
            y,
            pages[page][x][y].owner,
            pages[page][x][y].html,
            price
        );
    }

    function setHtml(
        uint256 page,
        uint32 x,
        uint32 y,
        string html
    ) external {
        if (pages[page][x][y].owner != msg.sender) throw;
        pages[page][x][y].html = html;
        UpdatedTile(
            page,
            x,
            y,
            pages[page][x][y].owner,
            html,
            pages[page][x][y].price
        );
    }

    function buyTile(
        uint256 page,
        uint32 x,
        uint32 y,
        string html
    ) public payable {
        Tile tile = pages[page][x][y];
        if (tile.owner == 0) {
            if (msg.value < cost) throw;
            SoldTile(page, x, y, this, msg.sender, cost);
        } else {
            if (tile.owner == msg.sender) throw;
            if (tile.price == 0) throw;
            if (msg.value < tile.price) throw;
            SoldTile(page, x, y, tile.owner, msg.sender, tile.price);
            tile.owner.transfer((tile.price * percent) / 100);
        }
        pages[page][x][y].owner = msg.sender;
        tile.html = html;
        tile.price = 0;
    }
}
