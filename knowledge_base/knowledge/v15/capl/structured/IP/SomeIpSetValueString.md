# SomeIpSetValueString

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetValueString( dword objectHandle, char valuePath[], char value[] ); // form 1
long SomeIpSetValueString( dword objectHandle, char valuePath[], char value[], long valueLength); // form 2
```

## Description

This function can be used to set a string in the object specified in the objectHandle parameter.

Enum data types can be set with one of their symbolic values using this function.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to a SOME/IP IL object, which must be completely described in the FIBEX database.The following objects are supported: Messages Fields Method calls: Handle to a method call that was created with SomeIpCreateMethodCall. |
| valuePath | Path of the value to be set.For specification of complex paths, a corresponding syntax must be adhered to. |
| value | New value (this string must be specified as null-terminated string). See BOM in SOME/IP UTF8 and UTF16 strings |
| valueLength | Length of the input string in characters. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
