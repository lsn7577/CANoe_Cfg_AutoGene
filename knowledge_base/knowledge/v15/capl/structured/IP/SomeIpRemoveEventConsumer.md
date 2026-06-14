# SomeIpRemoveEventConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpRemoveEventConsumer( dword cevHandle );
```

## Description

Removes an Event from a Consumed Service Instance. The Event was previously added by SomeIpCreateEventConsumer.

Afterwards, the callback registered with SomeIpCreateEventConsumer is no longer called.

## Parameters

| Name | Description |
|---|---|
| cevHandle | Handle of the Event to be removed (see SomeIpCreateEventConsumer). |

## Example

```c
on key 'c'
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = SomeIpCreateEventConsumer(csi,32770,"CallbackEventA1");

  // ... do something here

  // release the consumed Service Instance
  SomeIpRemoveEventConsumer(cev);

  // ... Application Endpoint, provided Service Instance and consumed Eventgroup can still be used here
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
