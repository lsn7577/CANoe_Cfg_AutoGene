# J1939ILSetSignalRaw

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetSignalRaw(dbSignal signal, long value ); // form 1
long J1939ILSetSignalRaw(dbNode node, dbSignal signal, long value ); // form 2
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Parameters

| Name | Description |
|---|---|
| signal | signal name from databaseThe signal must be assigned to the node as Tx signal. |
| value | raw value |
| node | Simulation node to apply the function |

## Example

```c
on key 't'
{
J1939ILSetSignalRaw( EEC1::EngSpeed, 12000 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
