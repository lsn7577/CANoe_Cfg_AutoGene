# LookupServiceConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
serviceConsumerRef * LookupServiceConsumer(char[] path);
```

## Description

Searches for the specified service consumer. The path must be complete including namespaces and endpoint: (Namespace::)+Service[consumer].

You can downcast the result to a concrete type, see the example.

## Parameters

| Name | Description |
|---|---|
| path | Path of the service consumer. |

## Return Values

The service consumer. An uninitialized object if the service consumer is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
serviceConsumerRef MirrorAdjustment mirrorSvc;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";

snprintf(path, elcount(path), "%s[%s]", service, consumer);
mirrorSvc = (serviceConsumerRef MirrorAdjustment) lookupServiceConsumer(path);
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
