# AREthSDDesubscribeEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSDDesubscribeEventGroup( dword cevgHandle );
```

## Description

The Event Group is unregistered at the node (consumer). The existing subscription is terminated (Stop Subscribe Eventgroup is sent). The associated Service Discovery message (Subscribe Eventgroup) is then no longer sent by the node.

The Event Group and all assigned Events, fields, and methods are not deleted when unregistered.

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

on key 'd'
{
  AREthSDDesubscribeEventGroup (ceg);
  write("Event Group is no longer subscribed");
}

on key 's'
{
  AREthSDSubscribeEventgroup(ceg,1);
  write("Event Group will now be subscribed again");
}
```

## Availability

| Since Version |
|---|
