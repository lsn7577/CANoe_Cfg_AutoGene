# SomeIpAddEvent

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpAddEvent( dword psiHandle, dword eventId, char onPrepareEventCallback[] );
```

## Description

This function adds an Event to a Provided Service Instance that was created by SomeIpCreateProvidedServiceInstance.

SomeIpTriggerEvent is used to trigger sending of the Event. Then, the CAPL Callback function <OnSomeIpPrepareEvent> is called, and the application has the opportunity to change or update the values of the SOME/IP Event.

An Event can be removed again using the SomeIpRemoveEvent function.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

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
