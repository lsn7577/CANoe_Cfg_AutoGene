# SomeIpSetValueString

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetValueString( dword objectHandle, char valuePath[], char value[] );
```

## Description

This function can be used to set a string in the object specified in the objectHandle parameter.

Enum data types can be set with one of their symbolic values using this function.

## Return Values

0: The function was successfully executed

## Example

In this example, it is assumed that a service with ID 10 (instance ID 1) is contained in the FIBEX database that is assigned to the CANoe configuration. The service provides an Event that transfers in the structured parameter param 1 the date Error_Message.

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
  // this function is called before the event is sent. Parameters can be specified here.

  // set parameter "Error_Message" of struct "param1"
  SomeIpSetValueString(messageHandle,"param1.Error_Message","Error Text");
}
```

## Availability

| Since Version |
|---|
