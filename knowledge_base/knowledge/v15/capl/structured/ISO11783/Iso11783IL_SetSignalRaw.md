# Iso11783IL_SetSignalRaw

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetSignalRaw( dbSignal signal, long value );
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Parameters

| Name | Description |
|---|---|
| signal | signal name from databaseThe signal must be assigned to the node as Tx signal. |
| value | raw value |

## Example

```c
on key 't'
{
Iso11783IL_SetSignalRaw( EEC1::EngSpeed, 12000 );
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
