# LookupTxPDU

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txPDURef * LookupTxPDU(char[] path);
```

## Description

Searches for the specified tx PDU. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Parameters

| Name | Description |
|---|---|
| path | Path of the Tx PDU. |

## Return Values

The tx PDU. An uninitialized object if the PDU is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
txPDURef MirrorState statePDU;
char path[200];
char pduName[50] = "Mirrors::MirrorState";
char sender[20] = "LeftMirror";

snprintf(path, elcount(path), "%s[%s]", pduName, sender);
statePDU = (txPDURef MirrorState) lookupTxPDU(path);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
