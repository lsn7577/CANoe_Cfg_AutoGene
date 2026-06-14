# Iso11783IL_PDDGetLastError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDGetLastError();
```

## Description

Supplies the last error code.

## Return Values

error code of the function most recently executed

## Example

```c
char text[256];

value = Iso11783IL_PDDGetValue ( PD::AppRateSignal, 0;

if (Iso11783IL_PDDGetLastError () != 0) {
  Iso11783IL_PDDGetLastErrorText ( elCount(text), text );
  write( "ERROR: %s", text );
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
