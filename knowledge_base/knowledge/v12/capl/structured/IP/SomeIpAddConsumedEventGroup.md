# SomeIpAddConsumedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpAddConsumedEventGroup( dword csiHandle, dword eventGroupId );
```

## Description

This function adds an Event Group to a Consumed Service Instance that was created by SomeIpCreateConsumedServiceInstance.

Objects of the Event Group can be registered as follows:

An Event Group can be removed again usign the SomeIpRemoveConsumedEventGroup function.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

```c
void Initialize()
{
  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,10,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,1);

  // create Event Consumer
  cev = SomeIpCreateEventConsumer(csi,32770,"CallbackEvent1");
}

  void CallbackEvent1(DWORD cevHandle, DWORD messageHandle)
{
  // this function is called if the Event was sent. Parameters can
  // be evaluated here.
}
```

## Availability

| Since Version |
|---|
