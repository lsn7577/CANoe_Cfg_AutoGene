# AREthAddEventToEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthAddEventToEventgroup( dword pevgHandle, dword pevHandle );
```

## Description

This function assigns an Event which was created by AREthAddEvent to an Event Group which was created by AREthAddProvidedEventGroup.

The Event can be removed from the Event Group with AREthRemoveEventFromEventGroup.

## Return Values

0: The function was successfully executed

## Example

```c
void Initialize()
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle
  dword peg; // provided Eventgroup handle
  dword pev; // provided Event handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);

  // create Event and add Event to Eventgroup
  pev = AREthAddEvent(psi, 1, "OnPrepareEvent1");
  AREthAddEventToEventgroup(peg, pev);

  // ensure that Event is sent cyclically
  AREthSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(dword eventHandle, dword messageHandle)
{
  // this function is called before the Event is sent. Parameters can be specified here.
}
```

## Availability

| Since Version |
|---|
