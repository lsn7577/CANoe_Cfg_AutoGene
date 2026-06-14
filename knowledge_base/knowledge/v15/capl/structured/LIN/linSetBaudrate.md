# linSetBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
void linSetBaudrate(long baudrate); // form 1
Void linSetBaudrate(long minBaudrate, long maxBaudrate); // form 2
```

## Description

With this function it is possible to change the baud rate during the measurement.

It is also possible to activate automatic baud rate detection in a specified range.

## Parameters

| Name | Description |
|---|---|
| baudrate | Baudrate to be set [in bit/sec]. Value range: 200 Baud – 30500 Baud |
| minBaudrate | The lower border of the automatic baud rate detection range. Value range: 200 Baud – maxBaudrate |
| maxBaudrate | The upper border of the automatic baud rate detection range. Value range: minBaudrate – 30500 Baud |

## Return Values

—

## Example

Change baud rate on keyboard event

```c
on key 'w'
{
linSetBaudrate(9600);  // change baudrate to 9600 bit/sec
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
