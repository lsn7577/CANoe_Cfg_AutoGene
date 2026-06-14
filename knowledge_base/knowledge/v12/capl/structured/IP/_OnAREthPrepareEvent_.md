# <OnAREthPrepareEvent>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnAREthPrepareEvent>( dword pevHandle, dword messageHandle );
```

## Description

A callback function with this signature must be passed to the CAPL function AREthAddEvent.

The callback is called before sending. The values of the SOME/IP message can be changed or updated before sending.

## Return Values

—

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
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  psi = AREthCreateProvidedServiceInstance(aep,10,1);
  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);
  // create Event and add Event to Eventgroup
  pev = AREthAddEvent(psi, 1, "OnPrepareEvent1 ");
  AREthAddEventToEventgroup(peg, pev);
  // ensure that Event is sent cyclically
  AREthSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1 (DWORD eventHandle, DWORD messageHandle)
{
  // this function is called before the Event is sent. Parameters can be specified here.
}
```

## Availability

| Since Version |
|---|
