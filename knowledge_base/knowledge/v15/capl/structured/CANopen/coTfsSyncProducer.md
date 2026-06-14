# coTfsSyncProducer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSyncProducer( void );
```

## Description

The call of this function starts a sync test that lasts 5 s. The sync producer in the DUT Device Under Test generates a sync message every 100 ms. The tolerance is ±10 ms. At the end of the test, the successful switch-off of the sync producer is checked.

This test does not support devices, which use the sync counter. Use the function coTfsSyncProducerDetail instead.

## Return Values

Error code

## Example

```c
coTfsSyncProducer();
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
