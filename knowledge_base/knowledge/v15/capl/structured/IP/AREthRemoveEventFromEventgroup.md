# AREthRemoveEventFromEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveEventFromEventgroup( dword pevgHandle, dword pevHandle );
```

## Description

Removes an Event created by AREthAddEvent from an Event Group which was created by AREthAddProvidedEventGroup. The Event itself is not deleted.

## Parameters

| Name | Description |
|---|---|
| pevgHandle | Handle of the Event Group from which an Event should be removed (see AREthAddProvidedEventGroup). |
| pevHandle | Handle of the Event that should be removed from the Event Group (see AREthAddEvent) |

## Example

```c
on key 't'
{
  dword aep;  // Application Endpoint handle
  dword psi;  // provided service handle
  dword peg1; // provided Eventgroup handle
  dword peg2; // provided Eventgroup handle
  dword pev;  // provided Event handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroups
  peg1 = AREthAddProvidedEventGroup(psi,1);
  peg2 = AREthAddProvidedEventGroup(psi,1);

  // create Event and add Event to both Eventgroups
  pev = AREthAddEvent(psi, 1, "OnPrepareEvent1");
  AREthAddEventToEventgroup(peg1, pev);
  AREthAddEventToEventgroup(peg2, pev);

  // ensure that Event is sent cyclically
  AREthSetProperty(pev,"CycleTimeMs",1000);

  // ... do something here

  // remove Event from Eventgroup 1
  AREthRemoveEventFromEventgroup(pev);

  // ... Event is still assigned to Eventgroup 2
  // ... Application Endpoint, provided Service Instance and Eventgroup can still be used here
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
