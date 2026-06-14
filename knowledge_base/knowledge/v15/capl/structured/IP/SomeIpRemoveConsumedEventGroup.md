# SomeIpRemoveConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
LONG SomeIpRemoveConsumedEventGroup( dword cevgHandle );
```

## Description

Removes an Event Group from a Consumed Service Instance. The Event Group was previously added by SomeIpAddConsumedEventGroup.

The Events, fields, and methods assigned to the Event Group are not deleted when the Eventgroup is closed.

## Parameters

| Name | Description |
|---|---|
| cevgHandle | Handle of the Consumed Event Group. |

## Example

```c
on key 'c'
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);

  // ... do something here

  // release the consumed Service Instance
  SomeIpRemoveConsumedEventGroup(ceg);

  // ... Application Endpoint and provided Service Instance can still be used here
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
