# AREthRemoveConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthRemoveConsumedEventGroup( dword cevgHandle );
```

## Description

Removes an Event Group from a Consumed Service Instance. The Event Group was previously added by AREthAddConsumedEventGroup.

The Events, fields, and methods assigned to the Event Group are not deleted when the Eventgroup is closed.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'c'
{
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);

  // ... do something here

  // release the consumed Service Instance
  AREthRemoveConsumedEventGroup(ceg);

  // ... Application Endpoint and provided Service Instance can still be used here
}
```

## Availability

| Since Version |
|---|
