# Iso11783PDDSetLogTrigger

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetLogTrigger( dword ecuHandle, dword command, ulong ddi, ulong elNum, ulong value );
```

## Description

A measurement command can be executed with this function. It can be used in the callback function Iso11783PDDOnDefaultLogRequest to activate the default logging.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU, must previously has been created with Iso11783CreateECU. |
| command | Measurement command: 4: Time Interval 5: Distance Interval 6: Minimum within Threshold 7: Maximum within Threshold 8: Change Threshold |
| ddi | Data Dictionary Identifier, 0x0000..0xFFFF |
| elNum | Element number, 0x000..0xFFF |
| command | value |
| Time Interval | time in ms |
| Distance Interval | distance in mm |
| Minimum within ThresholdMaximum within ThresholdChange Threshold | value of the process variable |

## Return Values

error code

## Example

```c
void Iso11783PDDOnDefaultLogRequest 
 ( dword ecuHandle )
{
Iso11783PDDSetLogTrigger
 ( ecuHandle, 4, 0x0100, 0, 1000 );
Iso11783PDDSetLogTrigger
 ( ecuHandle, 4, 0x0101, 0, 1000 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
