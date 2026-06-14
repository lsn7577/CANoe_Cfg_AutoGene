# SomeIpRemoveEvent

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveEvent( dword pevHandle );
```

## Description

Removes an Event from a Provided Service Instance. The Event was previously added by SomeIpAddEvent.

Afterwards, the callback registered with SomeIpAddEvent is no longer called. The Event is no longer sent by the SOME/IP IL.

## Return Values

0: The function was successfully executed

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

  // remove the Event
  SomeIpRemoveEvent(pev);

  // ... Event is removed from both Eventgroups and is not sent anymore
  // ... Application Endpoint, provided Service Instance and Eventgroup can still be used here
}
```

## Availability

| Since Version |
|---|
