# SomeIpCreateConsumedServiceInstance

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateConsumedServiceInstance( dword aepHandle, dword serviceId, dword instanceId ); // form 1
```

## Description

This function creates a Consumed Service Instance and adds it to an Application Endpoint which was created by SomeIpOpenLocalApplicationEndpoint.

Objects can be assigned to the Service Instance as follows:

SomeIpReleaseConsumedServiceInstance can be used to delete the Service Instance again.

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
