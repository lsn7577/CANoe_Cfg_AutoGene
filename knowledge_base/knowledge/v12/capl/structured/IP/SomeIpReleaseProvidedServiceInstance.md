# SomeIpReleaseProvidedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpReleaseProvidedServiceInstance( dword psiHandle );
```

## Description

Deletes a Provided Service Instance that was created by SomeIpCreateProvidedServiceInstance.

All objects (Eventgroups, Events, Fields, and Methods) are also closed when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Return Values

0: The function was successfully executed.

## Example

```c
on key 't'
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // ... do something here

  // close the provided Service Instance
  SomeIpReleaseProvidedServiceInstance(psi);

  // ... Application Endpoint can still be used here
}
```

## Availability

| Since Version |
|---|
