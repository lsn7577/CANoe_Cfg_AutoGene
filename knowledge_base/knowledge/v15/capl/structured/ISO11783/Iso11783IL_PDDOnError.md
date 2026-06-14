# Iso11783IL_PDDOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_PDDOnError( long errorCode, dword param );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the interaction layer when an error occurs.

## Parameters

| Name | Description |
|---|---|
| errorCode | error code |
| param | additional parameter, dependent on the error code |

## Return Values

—

## Example

```c
void Iso11783IL_PDDOnError( LONG errorCode, LONG addParam )
{
  char buffer[256];
  Iso11783IL_PDDGetLastErrorText ( elCount(buffer), buffer);
  write( "ERROR: %s", buffer );
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
