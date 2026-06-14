# SomeIpIsOptional

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpIsOptional( dword objectHandle, char memberPath[] );
```

## Description

This function can be used to read out if a parameter or member of the object, specified in the objectHandle parameter, is optional or mandatory.

The value is accessed in this case via symbolic access paths.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to an SOME/IP IL object, which must be completely described in the FIBEX database. The following objects are supported. Messages Fields Method calls: Handle to a method call that was created with SomeIpCreateMethodCall. |
| memberPath | Access path of the parameter or member to be read out. |

## Example

```c
void Initialize()
{
  dword aep; // application endpoint handle
  dword psi; // provided service handle
  dword peg; // provided eventgroup handle
  dword pev; // provided event handle

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

void OnPrepareEvent1(dword eventHandle, dword messageHandle)
{
  WORD isOpt; // return value if parameter or member is optional
  // this function is called before the event is sent. Parameters
  // can be specified here.
  // set parameter "value1" of struct "param1" only if it is mandatory

  // get if member is optional or mandatory
  isOpt = SomeIpIsOptional(messageHandle,"param1.value1");

  if(isOpt == 0)
  {
    SomeIpSetValueDWord(messageHandle,"param1.value1",7);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | — | — | — | 5.0 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
