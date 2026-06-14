# J1939TestChkCreate_AbsCycleTimeViolation

> Category: `Obsolete` | Type: `notes`

## Description

long checkID;checkID = J1939TestChkCreate_AbsCycleTimeViolation( 0x0B, 0x0C, 0xEF00, 348, 352, "absCycletimeCallback");J1939TestChkControl_Start(checkID);TestAddConstraint(checkID);TestWaitForTimeout(2000);TestRemoveConstraint(checkID);J1939TestChkControl_Stop(checkID);J1939TestChkControl_Destroy(checkID);

| Deprecated Function Replaced by ChkCreate_MsgAbsCycleTimeViolation |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword destAddr, dword pgn, dword aMinCycleTime, dword aMaxCycleTime |  |  |  |
| )long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword destAddr, dword pgn dword aMinCycleTime, dword aMaxCycleTime, char callback[] ) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword destAddr, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword destAddr, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime, char callback[] ) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword pgn, dword aMinCycleTime, dword aMaxCycleTime ) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dword sourceAddr, dword pgn, dword aMinCycleTime, dword aMaxCycleTime, char callback[] ) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dbNode sendNode, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dbNode sendNode, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime, char callback[] ) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dbNode sendNode, dbNode receiveNode, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime) |  |  |  |  |
| long J1939TestChkCreate_AbsCycleTimeViolation( dbNode sendNode, dbNode receiveNode, dbMsg msg, dword aMinCycleTime, dword aMaxCycleTime, char callback[] ) |  |  |  |  |
| Check Name | J1939 Cycle Time |  |  |  |
| Function | Checks the occurrences of cyclic messages. An event is generated if the time between the transmission of the messages is smaller than minCycleTime or larger than maxCycleTime. Not to be checked limits are set to 0; there must be at least one limit specified. |  |  |  |
| Parameters | pgn parameter group number to wait for |  |  |  |
| msg database message to wait for |  |  |  |  |
| sourceAddr source address of the PG or Null Address (0xFE) for wildcard |  |  |  |  |
| destAddr destination address of the PG or Null Address (0xFE) for wildcard, ignored for broadcast PGs |  |  |  |  |
| aMinCycleTime minimum allowed cycle time in milliseconds, 0 < x < aMaxCycleTime |  |  |  |  |
| aMaxCycleTime maximum allowed cycle time in milliseconds, aMinCycleTime < x < MAX_dword |  |  |  |  |
| callback name of the callback which is called when the check fails or 0, signature: void Callback( long checked ) |  |  |  |  |
| sendNode Send node of a J1939 parameter group. |  |  |  |  |
| receiveNode Receive node of a J1939 parameter group. This parameter is only used for destination specific parameter groups (PDU1 format, for dlc <= 8). |  |  |  |  |
| Return Values | >0: check was created successfully and may be referenced using the returned (handle) value =0: check could not be created and must not be referenced <0: error, see error codes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1-8.2 SP2 | J1939 | — | • |  |
| Example long checkID;checkID = J1939TestChkCreate_AbsCycleTimeViolation( 0x0B, 0x0C, 0xEF00, 348, 352, "absCycletimeCallback");J1939TestChkControl_Start(checkID);TestAddConstraint(checkID);TestWaitForTimeout(2000);TestRemoveConstraint(checkID);J1939TestChkControl_Stop(checkID);J1939TestChkControl_Destroy(checkID); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
