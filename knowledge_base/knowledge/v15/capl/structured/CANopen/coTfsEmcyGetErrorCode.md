# coTfsEmcyGetErrorCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsEmcyGetErrorCode( dword nodeID, dword outCanId[1], dword outTimeStamp[1], dword outEmcyCode[1], dword outErrorReg[1], byte outMsCodeBuf[5], dword msCodeBufSize );
```

## Description

This function transmits as return value the number of received emergency messages for the CANopen® node labeled with nodeID.

Each emergency message can only be called up once. The return value contains the number of received messages including the emergency message returned with the function call. All data pointers are only valid if there is at least one message present.

It is possible to omit the nodeID parameter. In this case, the internally-stored value set with coTfsSetNodeId is used.

## Parameters

| Name | Description |
|---|---|
| nodeID | The function transmits emergency messages from the selected node-ID. If node-ID is set to 0, the messages of all nodes are transmitted. |
| outCanId | CAN-ID data field. |
| outTimeStamp | Data field on the time stamp of the transmitted emergency message in ms. |
| outEmcyCode | Emergency code data field. |
| outErrorReg | Error register data field. |
| outMsCodeBuf[] | Manufacturer-specific error code (data field). |
| msCodeBufSize | Size of buffer in byte of outMsCodeBuf. |

## Return Values

Number of available emergency messages.

## Example

```c
dword nodeId , pOutCANID[1], pTimeStamp[1], pEmcyCode[1], pErrorReg[1], retValue;
byte pMsgCode[5];
nodeId = 112;

if (coTfsEmcyGetErrorCode(nodeId, pOutCANID, pTimeStamp, pEmcyCode, pErrorReg, pMsgCode, 5) != 0) {
  write("emergency message received");
  write("nodeID=0x%X; CAN ID 0x%X, timestamp=%d, emcyCode = 0x%X, errorRegister = 0x%X", nodeId, pOutCANID[0], pTimeStamp[0], pEmcyCode[0], pErrorReg[0]);
  write("manufacturer specific code = 0x%X %X %X %X %X", pMsgCode[0], pMsgCode[1], pMsgCode[2], pMsgCode[3], pMsgCode[4]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
