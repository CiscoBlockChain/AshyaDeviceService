'''pragma solidity ^0.4.19;


import "./AshyaRegistry.sol";

contract AshyaDevice {
    uint price = 0.0010 ether;
    string name; /* the name of this device */
    string location; /* my location where this device is */
    string url; /* my URL where people can find more information about me */
    string[] public urls; /* list of URLs that I can send data to */
    address public owner;
    AshyaRegistry registry;

    /* only the device owner can register the device. */
    modifier OwnerOnly() {
      require(msg.sender == owner);
      _;
    }

    /* people who want to use this device will need to pay */
    modifier CheckPrice()
    {
        require(msg.value >= price);
        _;
    }

    function AshyaDevice(string _name, string _location, string _url) public {
      owner = msg.sender;
      name = _name;
      location = _location;
      url = _url;
    }

    function registerDevice(address registryAddress)
             public
             payable
             OwnerOnly() {
        registry = AshyaRegistry(registryAddress);

        registry.addItem.value(0.0010 ether)(name,location,url);
    }


    function addURL(string newUrl)public payable CheckPrice(){
        urls.push(newUrl);
    }

    function getURLCount()public constant returns(uint count) {
        return urls.length;

    }
}
    '''