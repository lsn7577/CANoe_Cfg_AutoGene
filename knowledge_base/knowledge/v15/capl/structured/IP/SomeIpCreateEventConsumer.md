# SomeIpCreateEventConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateEventConsumer( dword csiHandle, dword eventId, CHAR onEventCallback[]);
```

## Description

This function adds an Event Consumer to a Consumed Service Instance that was created by SomeIpCreateConsumedServiceInstance.

When a suitable Event is received, the passed Callback function is called.

An Event Consumer can be removed again using the SomeIpRemoveEventConsumer function.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance that was created with SomeIpCreateConsumedServiceInstance. |
| eventId | Identifier of the Event. |
| onEventCallback | The function name that should be called when a suitable Event is received, see <OnSomeIpEventReceived>. |

## Example

```c
void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle

  // open Application Endpoint
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
  // this function is called if the Event was sent. Parameters can
  // be evaluated here.
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
