abi = [
    {
      "inputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "itemAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "index",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "iname",
          "type": "string"
        },
        {
          "indexed": False,
          "name": "location",
          "type": "string"
        },
        {
          "indexed": False,
          "name": "url",
          "type": "string"
        },
        {
          "indexed": False,
          "name": "ownerAddress",
          "type": "address"
        }
      ],
      "name": "LogNewItem",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "itemAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "LogDeleteItem",
      "type": "event"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "location",
          "type": "string"
        },
        {
          "name": "url",
          "type": "string"
        },
        {
          "name": "itemAddress",
          "type": "address"
        },
        {
          "name": "ownerAddress",
          "type": "address"
        }
      ],
      "name": "addItem",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "getItemCount",
      "outputs": [
        {
          "name": "count",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_itemAddress",
          "type": "address"
        }
      ],
      "name": "removeItem",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "itemAddress",
          "type": "address"
        }
      ],
      "name": "getItem",
      "outputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "url",
          "type": "uint256"
        },
        {
          "name": "location",
          "type": "string"
        },
        {
          "name": "index",
          "type": "uint256"
        },
        {
          "name": "ownerAddress",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "getItemAtIndex",
      "outputs": [
        {
          "name": "itemAddress",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "itemAddress",
          "type": "address"
        },
        {
          "name": "url",
          "type": "string"
        }
      ],
      "name": "addUrl",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    }
]

