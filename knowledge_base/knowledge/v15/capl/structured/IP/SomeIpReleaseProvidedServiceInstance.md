# SomeIpReleaseProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpReleaseProvidedServiceInstance( dword psiHandle );
```

## Description

Deletes a Provided Service Instance that was created by SomeIpCreateProvidedServiceInstance.

All objects (Eventgroups, Events, Fields, and Methods) are also closed when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the Provided Service Instance to be deleted (see SomeIpCreateProvidedServiceInstance). |

## Example

```c
on key 't'
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // ... do something here

  // close the provided Service Instance
  SomeIpReleaseProvidedServiceInstance(psi);

  // ... Application Endpoint can still be used here
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
