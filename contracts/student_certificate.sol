pragma solidity >= 0.5.0;

contract StudentCertificate {

    mapping(uint => string) certificate_hash;
    address owner;

    modifier onlyOwner {
        if (msg.sender != owner)
            revert("Permission denied.");
        _;
    }

    constructor() {
        owner = msg.sender;
    }
    
    function get_hash(uint certificate_id) public view returns(string memory) {
        return certificate_hash[certificate_id];
    }

    function add_hash(uint certificate_id, string memory hash) public onlyOwner{
        certificate_hash[certificate_id] = hash;
    }

}