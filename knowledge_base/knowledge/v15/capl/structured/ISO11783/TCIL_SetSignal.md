# TCIL_SetSignal

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetSignal( dbSignal signal, double value ); // form 1
long TCIL_SetSignal( dbNode tc, dbSignal signal, double value ); // form 2
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Parameters

| Name | Description |
|---|---|
| signal | Signal name from database.The signal must be assigned to the node as Tx signal. |
| value | physical value |
| tc | TC simulation node to apply the function |

## Return Values

—

## Example

```c
void SendLanguageCommand_English()
{
  TCIL_SetSignal( LC_TC::LanguageCodeCmd, 0x6E65 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
