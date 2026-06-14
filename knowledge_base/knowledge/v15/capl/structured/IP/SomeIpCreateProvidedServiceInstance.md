# SomeIpCreateProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateProvidedServiceInstance( dword aepHandle, dword serviceId, dword instanceId ); // form 1
dword SomeIpCreateProvidedServiceInstance( dword aepHandle, dword serviceId, dword instanceId, dword majorVersion, dword minorVersion ); // form 2
```

## Description

This function creates a Provided Service Instance and adds it to an Application Endpoint which was created by SomeIpReleaseProvidedServiceInstance.

Objects can be assigned to the Service Instance as follows:

The Service Instance can be deleted again with SomeIpReleaseProvidedServiceInstance.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Handle of the Application Endpoint (see SomeIpOpenLocalApplicationEndpoint) |
| serviceId | Service identifier |
| instanceId | Instance identifier |
| majorVersion | Service interface major version. |
| minorVersion | Service interface minor version. |

## Example

```c
void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle
  DWORD pev; // provided Event handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,1);

  // create Event and add Event to Eventgroup
  pev = SomeIpAddEvent(psi, 1, "OnPrepareEvent1");
  SomeIpAddEventToEventgroup(peg, pev);

  // ensure that Event is sent cyclically
  SomeIpSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(DWORD eventHandle, DWORD messageHandle)
{
  // this function is called before the Event is sent. Parameters can be specified here.
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
