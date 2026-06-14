# SomeIpSetValueDWord

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetValueDWord( dword objectHandle, char valuePath[], dword value );
```

## Description

This function can be used to set a raw value in the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Return Values

0: The function was successfully executed

## Example

```c
void Initialize()
{
  DWORD aep; // application endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided eventgroup handle
  DWORD pev; // provided event handle

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service instance
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // create eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,1);

  // create event and add event to eventgroup
  pev = SomeIpAddEvent(psi, 1, "OnPrepareEvent1");
  SomeIpAddEventToEventgroup(peg, pev);

  // ensure that event is sent cyclically
  SomeIpSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(DWORD eventHandle, DWORD messageHandle)
{
  // this function is called before the event is sent. Parameters
  // can be specified here.
  // set parameter "value1" of struct "param1"
  SomeIpSetValueDWord(messageHandle,"param1.value1",7);
}
```

## Availability

| Since Version |
|---|
