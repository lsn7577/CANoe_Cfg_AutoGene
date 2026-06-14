# CANopenDomainServerSetFileContents

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword CANopenDomainServerSetFileContents (dword nodeID, dword index, dword subIndex, char[] filename, dword[] errCode);
```

## Description

Sets the contents of a domain data object file of a CANopen node.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node ID of the SDO server, i.e. the node that contains the object dictionary with the domain data entry to be read. Value range 1..127. |
| index | Index of the object. Value range 1..65.535. |
| subIndex | Subindex of the object. Value range 0..255. |
| filename | Name of the file which will be used for the domain data entry. |
| errCode | 0: Ok. 1: No file selected for the domain data object in the CANopen Setup window. 2: Object entry does not exist. 3: The file does not exist or cannot be opened. |

## Return Values

—

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
