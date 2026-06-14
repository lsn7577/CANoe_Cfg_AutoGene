# AREthGetConsumedObjectHandle

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetConsumedObjectHandle( char objectSymbolicQualifier[] );
```

## Description

Enables to search for a consumed object which has been created separately.

## Parameters

| Name | Description |
|---|---|
| objectSymbolicQualifier | Symbolic qualifier identifying uniquely a FIBEX 4.1 database object. For syntax see Symbolic Database Access SOME/IP. |

## Example

```c
variables
{
  dword gCev; // consumed event handle
  dword gCfNotifier; // consumed field notifier handle
  dword gCfGetter; // consumed field getter handle
  dword gCfSetter; // consumed field setter handle
  msTimer gTimer;
}

on start
{
  // That the following code works there must be in the FIBEX 4.1
  // database a node consuming under an unreliable endpoint
  // (UDP socket) the following objects:
  //  - A service instance named "Service_Test"
  //  - An event group named "All" belonging to "Service_Test"
  //  - An event named "Event_Test" belonging to "All"
  //  - A field named "Field_Test" belonging to "All" and     having a notifier, a getter and a setter
  //  - A node providing the event group "All"

  // Get handle of the consumed event named "Event_Test"
  gCev = AREthGetConsumedObjectHandle ("Service_Test::Event_Test");

  // Register a CAPL callback for this event notification
  AREthRegisterCallback(gCev, "OnAREthEventReceived");

  // Get handle of the consumed field notification named "Field_Test"
  gCfNotifier = AREthGetConsumedObjectHandle ("Field_Test");

  // Register a CAPL callback for this field notification
  AREthRegisterCallback(gCfNotifier, "OnAREthFieldNotificationReceived");

  // Get handle of the consumed field getter named "Field_Test"
  gCfGetter = AREthGetConsumedObjectHandle ("get_Field_Test");

  // Register a CAPL callback for this getter response
  AREthRegisterCallback(gCfGetter, "OnAREthFieldGetterResponse");

  // Get handle of the consumed field setter named "Field_Test"
  gCfSetter = AREthGetConsumedObjectHandle ("set_Field_Test");

  // Register a CAPL callback for this setter response
  AREthRegisterCallback(gCfSetter, "OnAREthFieldSetterResponse");

  // Start timer
  setTimer(gTimer, 3000);
}

on timer gTimer
{
  // Call the field setter and getter
  AREthCallMethod(gCfGetter);
  AREthCallMethod(gCfSetter);
  // Restart timer
  setTimer(gTimer, 3000);
}

void OnAREthEventReceived( dword cevHandle, dword messageHandle )
{
  write ("Event notification received");
  // do something here
}

void OnAREthFieldNotificationReceived( dword cfHandle, dword messageHandle )
{
  write ("Field notification received");
  // do something here
}

void OnAREthFieldGetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field getter response received");
  // do something here
}

void OnAREthFieldSetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field setter response received");
  // do something here
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
