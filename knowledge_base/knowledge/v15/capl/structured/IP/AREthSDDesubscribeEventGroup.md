# AREthSDDesubscribeEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSDDesubscribeEventGroup( dword cevgHandle );
```

## Description

The Event Group is unregistered at the node (consumer). The existing subscription is terminated (Stop Subscribe Eventgroup is sent). The associated Service Discovery message (Subscribe Eventgroup) is then no longer sent by the node.

The Event Group and all assigned Events, fields, and methods are not deleted when unregistered.

## Parameters

| Name | Description |
|---|---|
| cevgHandle | Handle of the Consumed Event Group (see AREthAddConsumedEventGroup). |

## Example

```c
variables
{
  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle
}

on start()
{
  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);
  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);
 // create Event Consumer
  cev = AREthCreateEventConsumer(csi,1,"CallbackEvent1");
}

void CallbackEvent1(DWORD cevHandle, DWORD messageHandle)
{
  // this function is called if the Event was sent. Parameters can be evaluated here.
}

on key 'd'
{
  AREthSDDesubscribeEventGroup (ceg);
  write("Event Group is no longer subscribed");
}

on key 's'
{
  AREthSDSubscribeEventgroup(ceg,1);
  write("Event Group will now be subscribed again");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
