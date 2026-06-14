# coTfsEmcyResetList

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsEmcyResetList( void );
long coTfsEmcyResetList( dword nodeID );
```

## Description

This function deletes the internal list on which occurring emergency messages are stored.

It is possible to omit the nodeID parameter. In this case, the internally-stored value set with coTfsSetNodeId is used.

## Parameters

| Name | Description |
|---|---|
| nodeID | All messages of the associated node-ID are deleted; for nodeID=0, all emergency messages of all nodes are deleted. |

## Return Values

Error code

## Example

```c
coTfsEmcyResetList(2);
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
