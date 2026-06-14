# SOMEIP_UnsubscribeEventGroup

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SOMEIP_UnsubscribeEventGroup(consumedEventGroupRef * eventGroup); // from 1
long SOMEIP_UnsubscribeEventGroup(consumedServiceRef * service, char[] eventGroupName); // form 2
```

## Description

Unsubscribes for a service event group if SOME/IP binding is used. Note that this is more low-level; usually its more convenient to call consumedEventGroupRef::SOMEIPReleaseEventGroup on the event group.

## Parameters

| Name | Description |
|---|---|
| eventGroup | Event group which shall be unsubscribed. |
| service | Service which contains the event group. |
| eventGroupName | Name of the event group. |

## Example

```c
SOMEIP_UnsubscribeEventGroup(MirrorAdjustment.consumerSide[0,0].AllEvents);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | — | — | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
