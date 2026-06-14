# AREthCreateProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCreateProvidedServiceInstance( dword aepHandle, dword serviceId, dword instanceId );
```

## Description

This function creates a Provided Service Instance and adds it to an Application Endpoint which was created by AREthReleaseProvidedServiceInstance.

Objects can be assigned to the Service Instance as follows:

The Service Instance can be deleted again with AREthReleaseProvidedServiceInstance.

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
