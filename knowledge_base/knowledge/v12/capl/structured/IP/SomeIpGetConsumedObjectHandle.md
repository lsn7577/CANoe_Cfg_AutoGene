# SomeIpGetConsumedObjectHandle

> Category: `IP` | Type: `function`

## Syntax

```c
DWORD SomeIpGetConsumedObjectHandle( char objectSymbolicQualifier[] );
```

## Description

Enables to search for a consumed object which has been created separately.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

```c
variables
{
  DWORD gCev; // consumed event handle
  DWORD gCfNotifier; // consumed field notifier handle
  DWORD gCfGetter; // consumed field getter handle
  DWORD gCfSetter; // consumed field setter handle
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
  gCev = SomeIpGetConsumedObjectHandle ("Service_Test::Event_Test");

  // Register a CAPL callback for this event notification
  SomeIpRegisterCallback(gCev, "OnSomeIpEventReceived");

  // Get handle of the consumed field notification named "Field_Test"
  gCfNotifier = SomeIpGetConsumedObjectHandle ("Field_Test");

  // Register a CAPL callback for this field notification
  SomeIpRegisterCallback(gCfNotifier, "OnSomeIpFieldNotificationReceived");

  // Get handle of the consumed field getter named "Field_Test"
  gCfGetter = SomeIpGetConsumedObjectHandle ("get_Field_Test");

  // Register a CAPL callback for this getter response
  SomeIpRegisterCallback(gCfGetter, "OnSomeIpFieldGetterResponse");

  // Get handle of the consumed field setter named "Field_Test"
  gCfSetter = SomeIpGetConsumedObjectHandle ("set_Field_Test");

  // Register a CAPL callback for this setter response
  SomeIpRegisterCallback(gCfSetter, "OnSomeIpFieldSetterResponse");

  // Start timer
  setTimer(gTimer, 3000);
}

on timer gTimer
{
  // Call the field setter and getter
  SomeIpCallMethod(gCfGetter);
  SomeIpCallMethod(gCfSetter);
  // Restart timer
  setTimer(gTimer, 3000);
}

void OnSomeIpEventReceived( dword cevHandle, dword messageHandle )
{
  write ("Event notification received");
  // do something here
}

void OnSomeIpFieldNotificationReceived( dword cfHandle, dword messageHandle )
{
  write ("Field notification received");
  // do something here
}

void OnSomeIpFieldGetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field getter response received");
  // do something here
}

void OnSomeIpFieldSetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field setter response received");
  // do something here
}
```

## Availability

| Since Version |
|---|
