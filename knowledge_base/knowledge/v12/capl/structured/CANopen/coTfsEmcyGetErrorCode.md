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
