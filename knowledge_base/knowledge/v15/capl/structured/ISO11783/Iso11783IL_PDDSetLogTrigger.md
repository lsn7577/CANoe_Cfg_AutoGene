# Iso11783IL_PDDSetLogTrigger

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetLogTrigger( dword command, ulong ddi, ulong elNum, ulong value ); // form 1
long Iso11783IL_PDDSetLogTrigger( dbNode implement, dword command, ulong ddi, ulong elNum, ulong value ); // form 2
```

## Description

A measurement command can be executed with this function. It can be used in the callback function Iso11783IL_PDDOnDefaultLogRequest to activate the default logging.

## Parameters

| Name | Description |
|---|---|
| command | measurement command: 4: Time Interval 5: Distance Interval 6: Minimum within Threshold 7: Maximum within Threshold 8: Change Threshold |
| ddi | Data Dictionary Identifier, 0x0000..0xFFFF |
| elNum | element number, 0x000..0xFFF |
| Command | Value |
| Time Interval | time in ms |
| Distance Interval | distance in mm |
| Minimum within ThresholdMaximum within ThresholdChange Threshold | value of the process variable |
| implement | Simulation node to apply the function. |

## Example

```c
void Iso11783IL_PDDOnDefaultLogRequest ( )
{
Iso11783IL_PDDSetLogTrigger( 4, 0x0100, 0, 1000 );
Iso11783IL_PDDSetLogTrigger( 4, 0x0101, 0, 1000 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
