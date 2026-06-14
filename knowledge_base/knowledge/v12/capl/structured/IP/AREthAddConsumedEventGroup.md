# AREthAddConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddConsumedEventGroup( dword csiHandle, dword eventGroupId );
```

## Description

This function adds an Event Group to a Consumed Service Instance that was created by AREthCreateConsumedServiceInstance.

Objects of the Event Group can be registered as follows:

An Event Group can be removed again usign the AREthRemoveConsumedEventGroup function.

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

## Example

```c
void Initialize()
{
  dword aep; // application endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle
  dword cev; // consumed Event handle

  // open application endpoint
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
