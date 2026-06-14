# AREthSDRequireService

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSDRequireService( dword csiHandle );
```

## Description

A service that was unregistered at the node (consumer) using the AREthSDReleaseService function can be registered again with this function. The associated Service Discovery message (Find Service) is then sent if necessary.

## Return Values

0: The function was successfully executed

## Example

```c
variables
{
  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cev; // consumed Event handle
}

on start()
{
  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,10,1);
  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,1);
  // create Event Consumer
  cev = AREthCreateEventConsumer(csi,1,"CallbackEvent1");
}

void CallbackEvent1(DWORD cevHandle, DWORD messageHandle)
{
  // this function is called if the Event was sent. Parameters can be evaluated here.
}

on key 'r'
{
  AREthSDRequireService (csi);
}

on key 'x'
{
  AREthSDReleaseService(csi);
}
```

## Availability

| Since Version |
|---|
