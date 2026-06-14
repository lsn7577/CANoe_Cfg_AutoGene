# AREthRemoveProvidedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveProvidedEventGroup( dword pevgHandle );
```

## Description

Removes an Event Group from a Provided Service Instance. The Event Group was previously added by AREthAddProvidedEventGroup.

The Events and Fields assigned to the Event Group are not deleted when the Event Group is closed.

## Parameters

| Name | Description |
|---|---|
| pevgHandle | Handle of the Event Group (see AREthAddProvidedEventGroup). |

## Example

```c
on key 't'
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle
  dword peg; // provided Eventgroup handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);

  // ... do something here

  // remove the Eventgroup
  AREthRemoveProvidedEventGroup(peg);

  // ... Application Endpoint and provided Service Instance can still be used here
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
