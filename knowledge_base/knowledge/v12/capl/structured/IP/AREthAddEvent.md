# AREthAddEvent

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddEvent( dword psiHandle, dword eventId, char onPrepareEventCallback[] );
```

## Description

This function adds an Event to a Provided Service Instance that was created by AREthCreateProvidedServiceInstance.

AREthTriggerEvent is used to trigger sending of the Event. Then, the CAPL Callback function <OnAREthPrepareEvent> is called, and the application has the opportunity to change or update the values of the SOME/IP Event.

An Event can be removed again using the AREthRemoveEvent function.

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

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
