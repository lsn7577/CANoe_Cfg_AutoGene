# coTfsEmcySendMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsEmcySendMessage( dword nodeID, dword emcyCode, dword errorReg, byte inMsCodeBuf[5], dword msCodeBufSize );
```

## Description

This function sends out an emergency message.

## Parameters

| Name | Description |
|---|---|
| nodeID | Node-ID of the node that is sender of the message. |
| emcyCode | Emergency code. |
| errorReg | Error register. |
| inMsCodeBuf[] | Manufacturer-specific code (data field). |
| msCodeBufSize | Size of buffer in byte of inMsCodeBuf. |

## Return Values

Error code

## Example

```c
byte pMsCode[5] = {0,0,0,0,0};
if (coTfsEmcySendMessage(112, 0x8220, 0x20, pMsCode, 5) != 1) {
  write("coTfsSendEmcyMessage failed");
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
