# TestJoinPDUEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinPDUEvent (dbPDU aPDU, dword flags1); // form 1
long TestJoinPDUEvent (char aPDUName[], dword flags2); // form 2
long TestJoinPDUEvent (dword aHeaderID, dword flags3); // form 3
long TestJoinPDUEvent (dword flags4); // form 4
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aPDU | PDU to be awaited as it is defined in the database.Default value: wait for any PDU. |
| aPDUName | Name of a PDU to be awaited as it is defined in the database. Possibly the TX node’s name can be given as a prefix, e.g. <TXNodeName>::<PDUName>. |
| Note If the header ID is not unique, the function will return on the PDU that is first found in the database. In those cases it is better to use the PDU name. |  |
| flags3 | The lowest bit denotes whether the long or short header ID is to be resolved: 0: the short Header-ID is used. 1: the long header ID is used. All other bits are reserved and should be set to 0. |
| flags1, flags2, flags4 | Reserved and should be set to 0. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP1 | 13.0 | — | — | 2.1 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
