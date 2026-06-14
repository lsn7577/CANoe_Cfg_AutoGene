# SomeIpSDReleaseService

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSDReleaseService( dword csiHandle );
```

## Description

The service is unregistered at the node (consumer). The associated Service Discovery message (Find Service) is then no longer sent by the node.

The Service Instance and all assigned Eventgroups, Events, Fields, and Methods are not deleted when the Service Instance is unregistered.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance to be released (see SomeIpCreateConsumedServiceInstance). |

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
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);
  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);
  // create Event Consumer
  cev = SomeIpCreateEventConsumer(csi,32770,"CallbackEvent1");
}

void CallbackEvent1(DWORD cevHandle, DWORD messageHandle)
{
  // this function is called if the Event was sent. Parameters can be evaluated here.
}

on key 'r'
{
  SomeIpSDRequireService (csi);
}

on key 'x'
{
  SomeIpSDReleaseService (csi);
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
