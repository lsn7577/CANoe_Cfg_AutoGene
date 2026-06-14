# <OnC2xTransmitPacket>

> Category: `Car2x` | Type: `function`

## Syntax

```c
void <OnC2xTransmitPacket>(long packet); // form 1
long <OnC2xTransmitPacket>(long packet); // form 2
```

## Description

This callback is invoked before a database defined packet is transmitted (by this network node).

Within this callback the Token functions from the Packet API and all Signal functions from the Car2x IL API can be used.

Modifications are persistent between invocations of the callback.

When using the form 2 of the callback it is possible to skip the current transmission by returning a 0.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the packet |

## Return Values

Form 1

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1 10.0: form 2 | — | — | — | 2.1 SP3: form 1 2.2: form 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
