# GPIBGetError

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBGetError (void);
```

## Description

Returns the error variable. It is meaningful only when the ERR bit in the status word is set

## Example

```c
// “40” is not a valid GPIB address
GPIBDevChangePrimAddr(devDescr, 40);
if ( ( 1 << 15) & GPIBGetStatus() )
{
   write("ERR bit set in status word");
   if ( 4 == GPIBGetError() )
   {
      write("error is EARG: Invalid argument to function call");
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 SP2 |
| Restricted To | — | GPIB | — | — | — | GPIB |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
