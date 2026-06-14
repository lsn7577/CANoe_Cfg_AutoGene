# SomeIpRemoveEventConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpRemoveEventConsumer( dword cevHandle );
```

## Description

Removes an Event from a Consumed Service Instance. The Event was previously added by SomeIpCreateEventConsumer.

Afterwards, the callback registered with SomeIpCreateEventConsumer is no longer called.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'c'
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = SomeIpCreateEventConsumer(csi,32770,"CallbackEventA1");

  // ... do something here

  // release the consumed Service Instance
  SomeIpRemoveEventConsumer(cev);

  // ... Application Endpoint, provided Service Instance and consumed Eventgroup can still be used here
}
```

## Availability

| Since Version |
|---|
