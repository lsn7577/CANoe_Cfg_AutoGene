# SomeIpRemoveFieldFromEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveFieldFromEventgroup( dword pevgHandle, dword pfHandle );
```

## Description

Removes a field created by SomeIpAddField from an Event Group which was created by SomeIpAddProvidedEventGroup. The field itself is not deleted.

## Return Values

0: The function was successfully executed

## Example

```c
variables
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle
  DWORD pev; // provided Event handle
}

on start()
{
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

on key 'r'
{
  SomeIpRemoveFieldFromEventGroup (peg, pev);
}
```

## Availability

| Since Version |
|---|
