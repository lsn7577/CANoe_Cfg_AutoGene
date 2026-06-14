# DoIP_DataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_DataInd( byte buffer[], dword count, dword ecuAddress, dword testerAddress);
```

## Description

This callback is called from the DoIP layer when new data is received.

## Parameters

| Name | Description |
|---|---|
| buffer | Buffer containing the received data. |
| count | Size of the received data in bytes. |
| ecuAddress | Logical DoIP address of the ECU the data was sent to |
| testerAddress | Logical DoIP address of the tester that sent/received the data. (Note: before 8.2 SP4 the value of testerAddress is 0 always.) |

## Return Values

—

## Example

```c
void DoIP_DataInd( byte buffer[], dword count,
                   dword ecuAddress, dword testerAddress)
{
   // gateway processing here…
   // pass data up to the diagnostics layer
   Diag_DataInd( buffer, count, 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
