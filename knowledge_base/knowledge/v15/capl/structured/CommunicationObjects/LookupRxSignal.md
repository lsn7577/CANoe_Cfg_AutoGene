# LookupRxSignal

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
rxSignalRef * LookupRxSignal(char[] path);
```

## Description

Searches for the specified rx signal. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Parameters

| Name | Description |
|---|---|
| path | Path of the Rx signal. |

## Return Values

The rx signal. An uninitialized object if the signal is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
rxSignalRef long errorSignal;
char path[200];
char signalName[50] = "Mirrors::ErrorSignal";
char receiver[20] = "CANoe";

snprintf(path, elcount(path), "%s[%s]", signalName, receiver);
errorSignal = (rxSignalRef long) lookupRxSignal(path);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
