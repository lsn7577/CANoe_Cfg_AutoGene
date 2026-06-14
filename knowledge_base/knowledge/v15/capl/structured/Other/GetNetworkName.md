# GetNetworkName

> Category: `Other` | Type: `function`

## Syntax

```c
long GetNetworkName(dword busType, dword channelNumber, char name[]);
```

## Description

Retrieves the name assigned in the Simulation Setup for a specific channel.

## Parameters

| Name | Description |
|---|---|
| busType | Bus Type of the channel. The predefined enum BusType should be used for the value of this parameter. |
| channelNumer | Number of the channel for the specified bus. Channel numbering starts with 1. |
| name | Receives the name for the channel. |

## Example

```c
  stack char networkName[50];
 
stack long ret;
ret = GetNetworkName(eCAN, 1, networkName);
write("Name of CAN 1 is: %s", networkName);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
