# VTIL_ESC, VTIL_ESCMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ESC( ); // form 1
long VTIL_ESC(dbNode vt); // form 2
long VTIL_ESCMsg(dbNode workingSetMaster, dword objectId, dword errorCodes); // form 3
long VTIL_ESCMsg (dbNode vt, dbNode workingSetMaster, dword objectId, dword errorCodes); // form 4
```

## Description

The VTIL_ESC methods simulate the press of the ESC means of the Virtual Terminal. As a result, the VT ESC message with the Object ID, where input was aborted, is sent.

The VTIL_ESCMsg methods send the VT ESC message (without triggering any event in the Virtual Terminal).

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| workingSetMaster | Working Set Master which provides the object pool. |
| objectId | Object ID where input was aborted. |
| errorCodes | bit 0 = 1: No input field is selected (this bit is only used when the VT has a permanent ESC means) bit 1..3: Undefined, set to 0 recommended bit 4 = 1: Any other error |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 2 9.0 SP5: form 3, 4 | 13.0 | — | — | 2.1: form 1 2.1 SP2: form 1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
