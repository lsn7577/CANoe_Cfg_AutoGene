# AREthReleaseProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthReleaseProvidedServiceInstance( dword psiHandle );
```

## Description

Deletes a Provided Service Instance that was created by AREthCreateProvidedServiceInstance.

All objects (Eventgroups, Events, Fields, and Methods) are also closed when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the Provided Service Instance to be deleted (see AREthCreateProvidedServiceInstance). |

## Example

```c
on key 't'
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // ... do something here

  // close the provided Service Instance
  AREthReleaseProvidedServiceInstance(psi);

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
