# mostSetRetryParameter, mostGetRetryParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetRetryParameter(long channel, long id, long value);
long mostGetRetryParameter(long channel, long id);
```

## Description

The functions provide access to the transceiver chip parameters for message transmission. The number of low-level transmission attempts and delay between attempts can be set and retrieved.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| ID | Meaning VN26x0(MOST25) VN2640(MOST150) OptoLyzer G2 3150o(MOST150) |
| 0 | Transmission attempts on the control channel. 1..255 1..16 1..16 |
| 1 | Time between send retries on the control channel. 3..255 3..31 3..15 |
| 2 | Transmission attempts on the asynchronous channel. — 1..16 1..16 |
| 3 | Time between send retries on the asynchronous channel. — 0..255 0..255 |
| value | Value to be set. |

## Example

```c
// configure MOST transceiver for 5 low-level transmission attempts on Control channel
mostSetRetryParameter(1, 0, 5);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 7.1 SP4 | — | — | — | —✔ |
| Restricted To | MOST25, MOST150 | MOST25, MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
