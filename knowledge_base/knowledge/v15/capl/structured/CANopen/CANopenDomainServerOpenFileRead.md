# CANopenDomainServerOpenFileRead

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword CANopenDomainServerOpenFileRead (dword nodeID, dword index, dword subIndex);
```

## Description

Opens the file for a domain data object of a CANopen node for read access.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node ID of the SDO server, i.e. the node that contains the object dictionary with the domain data entry to be read. Value range 1..127. |
| index | Index of the object. Value range 1..65.535. |
| subIndex | Subindex of the object. Value range 0..255. |

## Return Values

The return value is the file handle that must be used for read operations.
If an error occurs, the return value is 0.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 SP2 | 13.0 SP2 | — | — | 5.0 SP2 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
