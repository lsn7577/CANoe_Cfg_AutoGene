# AREthAddConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddConsumedEventGroup( dword csiHandle, dword eventGroupId );
```

## Description

This function adds an Event Group to a Consumed Service Instance that was created by AREthCreateConsumedServiceInstance.

Objects of the Event Group can be registered as follows:

An Event Group can be removed again usign the AREthRemoveConsumedEventGroup function.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance. |
| eventGroupId | Identifier of the Event Group. |

## Example

```c
void Initialize()
{
  dword aep; // application endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle
  dword cev; // consumed Event handle

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = AREthCreateEventConsumer(csi,1,"CallbackEvent1");
}

  void CallbackEvent1(dword cevHandle, dword messageHandle)
{
  // this function is called if the Event was sent. Parameters can
  // be evaluated here.
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
