# Iso11783IL_SetSignal

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetSignal( dbSignal signal, double value );
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Parameters

| Name | Description |
|---|---|
| signal | signal name from databaseThe signal must be assigned to the node as Tx signal. |
| value | physical value |

## Example

```c
on key 't'
{
Iso11783IL_SetSignal( EEC1::EngSpeed, 1200.0 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
