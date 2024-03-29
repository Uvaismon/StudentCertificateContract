pragma solidity >= 0.5.0;

contract StudentCertificate {

    mapping(uint => string) certificate_hash;
    address owner;
    mapping(address => uint8) admin;

    modifier onlyOwner {
        if (msg.sender != owner)
            revert("Permission denied. Only owner can perform this operation.");
        _;
    }

    modifier onlyAdmin {
        if(admin[msg.sender] == 0)
            revert("Permission denied. Only admin can perform this operation");
        _;
    }
    
    modifier onlyNewCertificate(uint certificate_id) {
        if(bytes(certificate_hash[certificate_id]).length != 0)
            revert("Certificate hash already exists");
        _;
    }

    constructor() public {
        owner = msg.sender;
        admin[owner] = 1;
    }

    function add_admin(address admin_address) public onlyOwner {
        admin[admin_address] = 1;
    }

    function remove_admin(address admin_address) public onlyOwner {
        admin[admin_address] = 0;
    }
    
    function get_hash(uint certificate_id) public view returns(string memory) {
        return certificate_hash[certificate_id];
    }

    function add_hash(uint certificate_id, string memory hash) public onlyAdmin onlyNewCertificate(certificate_id) {
        certificate_hash[certificate_id] = hash;
    }

    function get_owner() public view returns(address) {
        return owner;
    }

}