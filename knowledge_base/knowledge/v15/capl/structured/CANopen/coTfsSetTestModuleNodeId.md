# coTfsSetTestModuleNodeId

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetTestModuleNodeId( dword nodeId );
```

## Description

The function set the node-ID of the tester. This is particularly necessary for the application profile. The function has to be called before the first use of SDOs.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node-ID of the tester, if application profile 447 is used the valid range is 1..16. |

## Return Values

Error code

## Example

```c
coTfsSetTestModuleNodeId(15); // set node-ID to 15
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
