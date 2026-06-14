# J1939TestChkCreate_RTSCTSViolation

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by ChkCreate_J1939RTSCTS, ChkStart_J1939RTSCTS |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long J1939TestChkCreate_RTSCTSViolation(dword senderAddr, dword receiverAddr, dword timeouts[5], dword options); |  |  |  |
| long J1939TestChkCreate_RTSCTSViolation(dword senderAddr, dword receiverAddr, dword timeouts[5], dword options, char caplCallback[]); |  |  |  |  |
| long J1939TestChkCreate_RTSCTSViolation(dword timeouts[5], dword options); |  |  |  |  |
| long J1939TestChkCreate_RTSCTSViolation(dword timeouts[5], dword options, char caplCallback[]); |  |  |  |  |
| long J1939TestChkCreate_RTSCTSViolation(dbNode sender, dbNode receiver, dword timeouts[5], dword options); |  |  |  |  |
| long J1939TestChkCreate_RTSCTSViolation(dbNode sender, dbNode receiver, dword timeouts[5], dword options, char caplCallback[]); |  |  |  |  |
| Check Name | J1939 RTS/CTS (Check Description) |  |  |  |
| Function | Observes the RTS/CTS transport protocol. It is possible to observer all RTS/CTS transmissions or only the transmission of a specific send node. |  |  |  |
| Parameters | sender send node from database, optional |  |  |  |
| receiver received node from database, optional |  |  |  |  |
| senderAddr sender address |  |  |  |  |
| receiverAddr receiver address |  |  |  |  |
| timeouts array with 5 timeout values [T1, T2, T3, T4, Th] with a zero based index [ms]. |  |  |  |  |
| options Bit 0 - 1 = abort directly after RTS is allowed |  |  |  |  |
| caplCallback name of the callback which is called when the check fails, signature: void Callback( long checked ) |  |  |  |  |
| Return Values | >0: check was created successfully and may be referenced using the returned (handle) value =0: check could not be created and must not be referenced <0: error, see error codes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1-8.2 SP5 | J1939 | — | • |  |
| Example long rtsCheck;dword timeouts[5] = { 750, 1250, 1250, 1050, 500};rtsCheck = J1939TestChkCreate_RTSCTSViolation( timeouts, 0 );J1939TestChkControl_Start(rtsCheck);TestAddConstraint(rtsCheck); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
