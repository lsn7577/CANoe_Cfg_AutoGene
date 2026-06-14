# AREthRemoveEventConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthRemoveEventConsumer( dword cevHandle );
```

## Description

Removes an Event from a Consumed Service Instance. The Event was previously added by AREthCreateEventConsumer.

Afterwards, the callback registered with AREthCreateEventConsumer is no longer called.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'c'
{
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle
  dword cev; // consumed Event handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = AREthCreateEventConsumer(csi,1,"CallbackEventA1");

  // ... do something here

  // release the consumed Service Instance
  AREthRemoveEventConsumer(cev);

  // ... Application Endpoint, provided Service Instance and consumed Eventgroup can still be used here
}
```

## Availability

| Since Version |
|---|
