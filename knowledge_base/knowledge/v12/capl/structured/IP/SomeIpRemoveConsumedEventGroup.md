# SomeIpRemoveConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
LONG SomeIpRemoveConsumedEventGroup( dword cevgHandle );
```

## Description

Removes an Event Group from a Consumed Service Instance. The Event Group was previously added by SomeIpAddConsumedEventGroup.

The Events, fields, and methods assigned to the Event Group are not deleted when the Eventgroup is closed.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'c'
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);

  // ... do something here

  // release the consumed Service Instance
  SomeIpRemoveConsumedEventGroup(ceg);

  // ... Application Endpoint and provided Service Instance can still be used here
}
```

## Availability

| Since Version |
|---|
