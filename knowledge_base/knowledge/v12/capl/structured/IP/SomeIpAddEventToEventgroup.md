# SomeIpAddEventToEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
LONG SomeIpAddEventToEventgroup( dword pevgHandle, dword pevHandle );
```

## Description

This function assigns an Event which was created by SomeIpAddEvent to an Event Group which was created by SomeIpAddProvidedEventGroup.

The Event can be removed from the Event Group with SomeIpRemoveEventFromEventGroup.

## Return Values

0: The function was successfully executed

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

| Since Version |
|---|
