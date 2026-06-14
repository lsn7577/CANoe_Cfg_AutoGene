# SomeIpRemoveEventFromEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveEventFromEventgroup( dword pevgHandle, dword pevHandle );
```

## Description

Removes an Event created by SomeIpAddEvent from an Event Group which was created by SomeIpAddProvidedEventGroup. The Event itself is not deleted.

## Parameters

| Name | Description |
|---|---|
| pevgHandle | Handle of the Event Group from which an Event should be removed (see SomeIpAddProvidedEventGroup). |
| pevHandle | Handle of the Event that should be removed from the Event Group (see SomeIpAddEvent) |

## Example

```c
on key 't'
{
  DWORD aep;  // Application Endpoint handle
  DWORD psi;  // provided service handle
  DWORD peg1; // provided Eventgroup handle
  DWORD peg2; // provided Eventgroup handle
  DWORD pev;  // provided Event handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroups
  peg1 = SomeIpAddProvidedEventGroup(psi,1);
  peg2 = SomeIpAddProvidedEventGroup(psi,1);

  // create Event and add Event to both Eventgroups
  pev = SomeIpAddEvent(psi, 1, "OnPrepareEvent1");
  SomeIpAddEventToEventgroup(peg1, pev);
  SomeIpAddEventToEventgroup(peg2, pev);

  // ensure that Event is sent cyclically
  SomeIpSetProperty(pev,"CycleTimeMs",1000);

  // ... do something here

  // remove Event from Eventgroup 1
  SomeIpRemoveEventFromEventgroup(pev);

  // ... Event is still assigned to Eventgroup 2
  // ... Application Endpoint, provided Service Instance and Eventgroup can still be used here
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
