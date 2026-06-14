# GNSSGetCurSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurSpeed();
```

## Description

This function returns the current speed at which the GNSS receiver is moving. If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid.

The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

current speed (in km/h, mph or kn)

## Example

```c
double speed;
GNSSSetUnits( 0 );
speed = GNSSGetCurSpeed();
write(“Speed = %lf km/h”, speed);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
