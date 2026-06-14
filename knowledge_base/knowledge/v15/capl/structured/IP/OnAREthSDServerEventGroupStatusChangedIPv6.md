# OnAREthSDServerEventGroupStatusChangedIPv6

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDServerEventGroupStatusChangedIPv6( dword serviceId, dword majorVersion, dword instanceId, dword eventGroupId, long status, byte newIpAddress[], dword newPort );
```

## Description

This callback function can be implemented in the CAPL program if a Service Server wants to be notified whenever a Subscriber is added.

This function is called when a Client executes a subscribe eventgroup command.

## Parameters

| Name | Description |
|---|---|
| serviceId | ID of the service whose status has changed. |
| instanceId | Instance ID |
| eventGroupId | ID of the Event Group. |
| status | 0: not subscribed 1: subscribed |
| newIpAddress | IPv6 address via which the subscription was received. |
| newPort | Source port via which the subscription was received. |
| majorVersion | Service interface major version. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10 SP4 | — | — | — | 2.2 SP4 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
