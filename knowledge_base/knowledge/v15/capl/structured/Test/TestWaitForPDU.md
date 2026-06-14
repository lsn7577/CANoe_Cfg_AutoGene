# TestWaitForPDU

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForPDU (dbPDU aPDU, dword flags1, dword aTimeout); // form 1
long TestWaitForPDU (char aPDUName[], dword flags2, dword aTimeout); // form 2
long TestWaitForPDU (dword aHeaderID, dword flags3, dword aTimeout); // form 3
long TestWaitForPDU (dword flags4, dword aTimeout); // form 4
long TestWaitForPDU (dbPDU aPDU, dword flags1, dword vlanId, dword aTimeout); // form 5
long TestWaitForPDU (char aPDUName[], dword flags2, dword vlanId, dword aTimeout); // form 6
long TestWaitForPDU (dword aHeaderID, dword flags3, dword vlanId, dword aTimeout); // form 7
```

## Description

Waits for the occurrence of the specified PDU. Should the PDU not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no PDU is specified the wait condition is resolved on any PDU.

## Parameters

| Name | Description |
|---|---|
| aPDU | PDU to be awaited as it is defined in the database. |
| aPDUName | Name of a PDU to be awaited as it is defined in the database. Possibly the TX node’s name can be given as a prefix, e.g. <TXNodeName>::<PDUName>. |
| Note If the header ID is not unique, the function will return on the PDU that is first found in the database. In those cases it is better to use the PDU name. |  |
| flags3 | The lowest bit denotes whether the long or short header ID is to be resolved: 0: the short Header-ID is used. 1: the long header ID is used. All other bits are reserved and should be set to 0. |
| flags1, flags2, flags4 | Reserved and should be set to 0. |
| vlanId | VlanID of the specified PDU. |
| aTimeout | Maximum time that should be waited [ms].Transmission of 0: no timeout controlling |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP1: form 1-4 14: form 5-7 | 13.0 | — | — | 2.1 SP2: form 1-4 5.0 SP3: form 5-7 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
