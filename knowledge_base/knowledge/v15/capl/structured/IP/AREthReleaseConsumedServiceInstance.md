# AREthReleaseConsumedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthReleaseConsumedServiceInstance(dword csiHandle );
```

## Description

Deletes a Consumed Service Instance that was created by AREthCreateConsumedServiceInstance.

The objects assigned to the Service Instance (Eventgroups, Events, fields, and methods) are deleted when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance to be deleted. |

## Example

```c
on key 'c'
{
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);

  // ... do something here

  // release the consumed Service Instance
  AREthReleaseConsumedServiceInstance(csi);

  // ... Application Endpoint can still be used here
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
