# Iso11783IL_TIMConnectSysVarToSynchronizationPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectSysVarToSynchronizationPoint(dbNode counterpart, char[] sysVarNameWithPath); // form 1
long Iso11783IL_TIMConnectSysVarToSynchronizationPoint(byte counterpartAddress, char[] sysVarNameWithPath); // form 2
long Iso11783IL_TIMConnectSysVarToSynchronizationPoint(dbNode participant, dbNode counterpart, char[] sysVarNameWithPath); // form 3
long Iso11783IL_TIMConnectSysVarToSynchronizationPoint(dbNode participant, byte counterpartAddress, char[] sysVarNameWithPath); // form 4
```

## Description

Connects the synchronization point of a TIM client/server connection to a system variable. Possible values of the system variables are:

To release connection between the system variable, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| counterpart | TIM counterpart of the client/server connection. |
| counterpartAddress | Address of the TIM counterpart of the client/server connection. Value range: 0..253 |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |
| participant | Simulation node (TIM server or TIM client) to apply the function. |

## Example

```c
Iso11783IL_TIMConnectSysVarToSynchronizationPoint (TIMClient, "Server::SynchPoint");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
