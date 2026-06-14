# J1939TestChkCreate_ACLViolation

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by ChkCreate_J1939AddressClaimViolation |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long J1939TestChkCreate_ACLViolation( dbNode sender, dword timeout, dword options ) |  |  |  |
| Check Name | J1939 Address Claiming |  |  |  |
| Function | Observes the Address Claiming of a node. The specified node must respond to a Request for ACL. Optionally the check allows sending other messages, only if an ACL message (0xEE00) of the node is received first. |  |  |  |
| Parameters | sender send node from the database |  |  |  |
| timeout timeout in [ms] |  |  |  |  |
| options bit 0: before the ACL and 250ms afterwards, the node is allowed to send messages bit 1: allow ACL messages from non-configured nodes bit 2: the node is allowed to claim another address than configured |  |  |  |  |
| Return Values | >0: check was created successfully and may be referenced using the returned (handle) value =0: check could not be created and must not be referenced <0: error, see error codes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1-8.2 SP2 | J1939 | — | • |  |
| Example long aclCheck;aclCheck = J1939TestChkCreate_ACLViolation( EMS, 205, 0x01 );J1939TestChkControl_Start(aclCheck);TestAddConstraint(aclCheck); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
