# SomeIpReleaseConsumedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
LONG SomeIpReleaseConsumedServiceInstance(dword csiHandle );
```

## Description

Deletes a Consumed Service Instance that was created by SomeIpCreateConsumedServiceInstance.

The objects assigned to the Service Instance (Eventgroups, Events, fields, and methods) are deleted when the Service Instance is closed. If the Service Instance is newly created, all objects must also be newly created.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'c'
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // ... do something here

  // release the consumed Service Instance
  SomeIpReleaseConsumedServiceInstance(csi);

  // ... Application Endpoint can still be used here
}
```

## Availability

| Since Version |
|---|
