# coTfsHeartbeatProducer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsHeartbeatProducer( dword duration, dword producerTime, dword tolerance );
```

## Description

This function activates the heartbeat producer of the DUT Device Under Test. For this the object 0x1017 with producerTime is described via a SDO write access. After this, the regularity of the heartbeat message is checked and then the heartbeat producer is switched off again (0x1017 = 0). The test duration must be greater than the permitted time deviation.

At least two heartbeat messages of the DUT are awaited, even if the test duration is set shorter.

## Parameters

| Name | Description |
|---|---|
| duration | Test duration in ms, how long the regularity of the heartbeat producer should be tested. |
| producerTime | Heartbeat producer time in ms. |
| tolerance | Permitted time deviation of the DUT in ms. It is recommended that you use an even value. The tolerated time-frame within which a message is still accepted is: x - (tolerance/2) <= x <= x + (tolerance/2) |

## Return Values

Error code

## Example

```c
if (coTfsHeartbeatProducer( 3000, 500, 10) != 1) { // duration, producerTime, tolerance
  write("heartbeat producer test failed");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
