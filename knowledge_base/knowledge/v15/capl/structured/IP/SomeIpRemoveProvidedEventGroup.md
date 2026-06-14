# SomeIpRemoveProvidedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveProvidedEventGroup( dword pevgHandle );
```

## Description

Removes an Event Group from a Provided Service Instance. The Event Group was previously added by SomeIpAddProvidedEventGroup.

The Events and Fields assigned to the Event Group are not deleted when the Event Group is closed.

## Parameters

| Name | Description |
|---|---|
| pevgHandle | Handle of the Event Group (see SomeIpAddProvidedEventGroup). |

## Example

```c
on key 't'
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,1);

  // ... do something here

  // remove the Eventgroup
  SomeIpRemoveProvidedEventGroup(peg);

  // ... Application Endpoint and provided Service Instance can still be used here
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
