# AREthCreateEventConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCreateEventConsumer( dword csiHandle, dword eventId, CHAR onEventCallback[]);
```

## Description

This function adds an Event Consumer to a Consumed Service Instance that was created by AREthCreateConsumedServiceInstance.

When a suitable Event is received, the passed Callback function is called.

An Event Consumer can be removed again using the AREthRemoveEventConsumer function.

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

## Example

```c
void Initialize()
{
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle
  dword cev; // consumed Event handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = AREthCreateEventConsumer(csi,1,"CallbackEvent1");
}

void CallbackEvent1(dword cevHandle, dword messageHandle)
{
  // this function is called if the Event was sent. Parameters can
  // be evaluated here.
}
```

## Availability

| Since Version |
|---|
