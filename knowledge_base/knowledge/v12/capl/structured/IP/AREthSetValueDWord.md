# AREthSetValueDWord

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSetValueDWord( dword objectHandle, char valuePath[], dword value );
```

## Description

This function can be used to set a raw value in the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Return Values

0: The function was successfully executed

## Example

```c
void Initialize()
{
  dword aep; // application endpoint handle
  dword psi; // provided service handle
  dword peg; // provided eventgroup handle
  dword pev; // provided event handle

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service instance
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // create eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);

  // create event and add event to eventgroup
  pev = AREthAddEvent(psi, 1, "OnPrepareEvent1");
  AREthAddEventToEventgroup(peg, pev);

  // ensure that event is sent cyclically
  AREthSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(dword eventHandle, dword messageHandle)
{
  // this function is called before the event is sent. Parameters
  // can be specified here.
  // set parameter "value1" of struct "param1"
  AREthSetValueDWord(messageHandle,"param1.value1",7);
}
```

## Availability

| Since Version |
|---|
