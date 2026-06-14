# Iso11783IL_TIMOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnError(long errorCode, dword addParam)
```

## Description

This callback function is called from the ISO11783 IL if an error occurred while TIM nodes are simulated.

## Parameters

| Name | Description |
|---|---|
| errorCode | Current error code. |
| addParam | Additional parameter depending on the error code. |

## Example

```c
void Iso11783IL_TIMOnError( long errorCode, dword addParam )
{
  char buffer[256];
  Iso11783IL_GetLastErrorText ( elCount(buffer), buffer);
  write( "Iso11783IL_TIMOnError: Error %i (%f): %s", errorCode,timeNowFloat()/100000.0, buffer );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
