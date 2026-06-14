# DoIP_SetTesterAdapter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetTesterAdapter(char adapter[]);
```

## Description

Sets the network interface to be used by the DoIP layer. This function must be called in on preStart.

## Parameters

| Name | Description |
|---|---|
| adapter | The name of the network adapter. |

## Return Values

—

## Example

```c
// Set the network adapter
char buffer[256];
DiagGetCommParameter( "DoIP.TESTER_Adapter", 0, buffer, elcount( buffer));
DoIP_SetTesterAdapter( buffer);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
