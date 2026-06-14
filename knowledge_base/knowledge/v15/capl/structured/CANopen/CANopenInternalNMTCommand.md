# CANopenInternalNMTCommand

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenInternalNMTCommand(dword nodeId, dword NMTCommand );
```

## Description

Performs an NMT command inside a simulated CANopen node.

## Parameters

| Name | Description |
|---|---|
| nodeID | ID of the simulated CANopen node. |
| NMTCommand | Value of the NMT command to be executed: 0x01: Start node 0x02: Stop node 0x80: Enter pre-operational 0x81: Reset node 0x82: Reset communication |

## Return Values

The data as qword.

## Example

```c
CANopenInternalNMTCommand(2, 1); //Start node 2

}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
