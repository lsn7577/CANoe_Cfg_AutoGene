# SomeIpCreateConsumedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateConsumedServiceInstance( dword aepHandle, dword serviceId, dword instanceId ); // form 1
dword SomeIpCreateConsumedServiceInstance( dword aepHandle, dword serviceId, dword instanceId, dword majorVersion, dword minorVersion ); // form 2
```

## Description

This function creates a Consumed Service Instance and adds it to an Application Endpoint which was created by SomeIpOpenLocalApplicationEndpoint.

Objects can be assigned to the Service Instance as follows:

SomeIpReleaseConsumedServiceInstance can be used to delete the Service Instance again.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Handle of the Application Endpoint. |
| serviceId | Service identifier |
| instanceId | Instance identifier |
| majorVersion | Service interface major version. |
| minorVersion | Service interface minor version. |

## Example

```c
void Initialize()
{
  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle

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
  // this function is called if the Event was sent. Parameters can
  // be evaluated here.
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 8.5 SP4: form 2 | — | — | — | 2.0 SP2: form 1 2.0 SP3: form 2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
