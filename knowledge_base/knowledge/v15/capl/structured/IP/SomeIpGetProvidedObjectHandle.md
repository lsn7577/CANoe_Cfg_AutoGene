# SomeIpGetProvidedObjectHandle

> Category: `IP` | Type: `function`

## Syntax

```c
DWORD SomeIpGetProvidedObjectHandle( char objectSymbolicQualifier[] );
```

## Description

Enables to search for a provided object which has been created separately.

## Parameters

| Name | Description |
|---|---|
| objectSymbolicQualifier | Symbolic qualifier identifying uniquely a FIBEX 4.1 database object. For syntax see Symbolic Database Access by SOME/IP. |

## Example

```c
on start
{
  // That the following code works there must be in the FIBEX 4.1
  // database a node providing under an unreliable endpoint
  // (UDP socket) the following objects:
  //  - A service instance named "Service_Test"
  //  - An event group named "All" belonging to "Service_Test"
  //  - An event named "Event_Test" belonging to "All"
  //  - A field named "Field_Test" belonging to "All" and having a notifier, a getter and a setter
  //  - A node consuming the event group "All"

  DWORD psi; // provided service instance handle
  DWORD peg; // provided event group handle
  DWORD pev; // provided event handle
  DWORD pfNotifier; // provided field notifier handle
  DWORD pfGetter; // provided field getter handle
  DWORD pfSetter; // provided field setter handle

  // Get handle of the provided service instance named "Service_Test"
  psi = SomeIpGetProvidedObjectHandle("Service_Test");

  // Get handle of the provided event group named "All"
  peg = SomeIpGetProvidedObjectHandle ("Service_Test::All");

  // Modifiy the unicast/multicast threshold that for one 
  // subscriber the event and field notification are sent
  // per unicast
  SomeIpSetProperty(peg,"UnicastLimit", 1);

  // Get handle of the provided event "Event_Test"
  pev = SomeIpGetProvidedObjectHandle ("Event_Test");

  // Sent the provided event "Event_Test" cyclically every 1 s
  SomeIpSetProperty(pev,"CycleTimeMs",1000);

  // Get handle of the provided field notification named "Field_Test"
  pfNotifier = SomeIpGetProvidedObjectHandle ("Field_Test");

  // Sent the providedfield notification named "Field_Test" cyclically every 2 s
  SomeIpSetProperty(pfNotifier,"CycleTimeMs",2000);

  // Get handle of the provided field getter named "Field_Test"
  pfGetter = SomeIpGetProvidedObjectHandle ("get_Field_Test");

  // Register a CAPL callback for this getter request
  SomeIpRegisterCallback(pfGetter, "OnSomeIpFieldGetterRequest");

  // Get handle of the provided field setter named "Field_Test"
  pfSetter = SomeIpGetProvidedObjectHandle ("set_Field_Test");

  // Register a CAPL callback for this setter request
  SomeIpRegisterCallback(pfSetter, "OnSomeIpFieldSetterRequest");
}

void OnSomeIpFieldGetterRequest(dword methodHandle,dword messageHandle,dword messageResponseHandle)
{
  write ("Field getter request received");
  // do something here
}

void OnSomeIpFieldSetterRequest(dword methodHandle,dword messageHandle,dword messageResponseHandle)
{
  write ("Field setter request received");
  // do something here
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
