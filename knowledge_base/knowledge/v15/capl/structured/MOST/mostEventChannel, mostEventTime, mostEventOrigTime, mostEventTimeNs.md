# mostEventChannel, mostEventTime, mostEventOrigTime, mostEventTimeNs

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostEventChannel();
dword mostEventTime();
dword mostEventOrigTime();
float mostEventTimeNs();
```

## Description

long mostEventChannel() returns the channel over which the event arrived.

dword mostEventTime() returns the time stamp of the event (Units: 10 µs).

dword mostEventOrigTime() returns the hardware-generated time stamp of the event (Units: 10 µs).

float mostEventTimeNs() returns the time stamp of the event (Units: 1 ns).

## Return Values

Time stamp

## Example

```c
OnMostNodeAdr(long nodeadr)
{
   write("Node address changed to %04X on channel %d at %fs",
      nodeadr,
      mostEventChannel(),
      mostEventTime() / 100000.0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST150 MOST50 | MOST25 MOST150 MOST50 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
