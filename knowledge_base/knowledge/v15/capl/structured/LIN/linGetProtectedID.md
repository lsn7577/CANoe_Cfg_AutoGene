# linGetProtectedID

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetProtectedID (long frameID);
```

## Description

With this function it is possible to calculate protected ID for the corresponding LIN frame identifier (i.e. the frame identifier with parity bits).

## Parameters

| Name | Description |
|---|---|
| frameID | LIN frame identifier whose protected ID will be calculated. Value range: 0 .. 63 |

## Return Values

Returns the calculated protected identifier or a value greater than 255 on failure.

## Example

Display in Write Window a protected ID for each LIN frame seen on the bus

```c
on linFrame *
{
dword pid;
pid = linGetProtectedID(this.ID);
writeLineEx(0,0, "Protected ID for LIN frame identifier 0x%x is 0x%x", this.ID, pid);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
