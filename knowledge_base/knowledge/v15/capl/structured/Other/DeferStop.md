# DeferStop

> Category: `Other` | Type: `function`

## Syntax

```c
void DeferStop(dword maxDeferTime);
```

## Description

Defers measurement stop.

The function can be called in the on preStop handler or even at an earlier time instance. Measurement is deferred until CompleteStop is called in the same node or the simulation time has advanced by the amount given in parameter maxDeferTime since the arrival of a stop request (and call of the on preStop handler).

DeferStop enables waiting for completion of activities that have to be carried out before measurement stop takes effect, e.g. a reset of an attached ECU.

## Parameters

| Name | Description |
|---|---|
| maxDeferTime | Indicates the time interval in milliseconds after which completion of pre-stop activities is indicated automatically if it has not yet been done explicitly via CompleteStop. |

## Return Values

—

## Example

```c
on preStop
{
   message ShutdownReq m;
   output(m);
   DeferStop(1000);
}
on message ShutdownAck
{
   CompleteStop();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 7.1 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
