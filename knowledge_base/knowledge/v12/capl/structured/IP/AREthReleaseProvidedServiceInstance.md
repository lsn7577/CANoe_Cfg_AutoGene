# AREthReleaseProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthReleaseProvidedServiceInstance( dword psiHandle );
```

## Description

Deletes a Provided Service Instance that was created by AREthCreateProvidedServiceInstance.

All objects (Eventgroups, Events, Fields, and Methods) are also closed when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Return Values

0: The function was successfully executed.

## Example

```c
on key 't'
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // ... do something here

  // close the provided Service Instance
  AREthReleaseProvidedServiceInstance(psi);

  // ... Application Endpoint can still be used here
}
```

## Availability

| Since Version |
|---|
