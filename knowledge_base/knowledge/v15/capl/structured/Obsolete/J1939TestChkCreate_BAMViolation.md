# J1939TestChkCreate_BAMViolation

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by ChkCreate_J1939BAM, ChkStart_J1939BAM |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long J1939TestChkCreate_BAMViolation(dword min, dword max, dword options); |  |  |  |
| long J1939TestChkCreate_BAMViolation(dword min, dword max, dword options, char caplCallback[]); |  |  |  |  |
| long J1939TestChkCreate_BAMViolation(dword senderAddr, dword min, dword max, dword options); |  |  |  |  |
| long J1939TestChkCreate_BAMViolation(dword senderAddr, dword min, dword max, dword options, char caplCallback[]); |  |  |  |  |
| long J1939TestChkCreate_BAMViolation(dbNode sender, dword min, dword max, dword options); |  |  |  |  |
| long J1939TestChkCreate_BAMViolation(dbNode sender, dword min, dword max, dword options, char caplCallback[]); |  |  |  |  |
| Check Name | J1939 BAM (Check Description) |  |  |  |
| Function | Observes the BAM transport protocol. It is possible to observer all BAM transmissions or only the transmission of a specific send node. |  |  |  |
| Parameters | sender send node from database, optional |  |  |  |
| senderAddr sender address, optional |  |  |  |  |
| min minimum distance [ms] (Default 50ms) |  |  |  |  |
| max maximum distance [ms] (Default 200ms) |  |  |  |  |
| options not used, always 0 |  |  |  |  |
| callback name of the callback which is called when the check fails, signature: void Callback( long checked ) |  |  |  |  |
| Return Values | >0: check was created successfully and may be referenced using the returned (handle) value =0: check could not be created and must not be referenced <0: error, see error codes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1-8.2 SP5 | J1939 | — | • |  |
| Example long bamCheck;bamCheck = J1939TestChkCreate_BAMViolation( EMS, 50, 200, 0x00 );J1939TestChkControl_Start(bamCheck);TestAddConstraint(bamCheck); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
