abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_location",
				"type": "string"
			},
			{
				"name": "_url",
				"type": "string"
			}
		],
		"name": "addItem",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
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
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
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
				"name": "location",
				"type": "string"
			},
			{
				"name": "url",
				"type": "string"
			},
			{
				"name": "index",
				"type": "uint256"
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
	}
]