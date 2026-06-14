# <OnAREthFieldNotification>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnAREthFieldNotification>( dword cfHandle, dword messageHandle );
```

## Description

This callback function is called by AUTOSAR Eth IL when a notification message has been received for the field specified in the pfHandle parameter.

A callback function with this signature must be passed to the CAPL function AREthCreateFieldConsumer.

## Parameters

| Name | Description |
|---|---|
| cfHandle | Handle of the field that triggered the callback. |
| messageHandle | Message handle of the SOME/IP field notification. |

## Return Values

—

## Example

In this example, it is assumed that the utilized field is contained in the FIBEX database that is assigned to the CANoe configuration. The field has the Notification ID 30, the Getter ID 31, and the Setter ID 32. The data type of the field is a standard data type (for example, UINT8).

```c
variables
{
  dword gMcGetter; // getter method call
  dword gMcSetter; // setter method call
}

void Initialize()
{
  CONST dword FieldNotificationID = 30;
  CONST dword FieldGetterID       = 31;
  CONST dword FieldSetterID       = 32;

  dword aep; // application endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,12,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,300);

  // create field consumer as well as getter and setter method calls
  AREthCreateFieldConsumer(csi,FieldNotificationID,FieldGetterID,FieldSetterID, "OnAREthFieldNotification");
  gMcGetter = AREthCreateMethodCall(csi,FieldGetterID,"OnFieldGetterResponse");
  gMcSetter = AREthCreateMethodCall(csi,FieldSetterID,"OnFieldSetterResponse");
}

void OnAREthFieldNotification(dword pfHandle,dword messageHandle)
{
  write ("Field Notification Received");

  // do something here
}

void OnFieldGetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field Getter Response Received");

  // do something here
}

void OnFieldSetterResponse(dword methodCallHandle, dword messageResponseHandle )
{
  write ("Field Setter Response Received");

  // do something here
}

on key 'g'
{
  // call getter method
  AREthCallMethod(gMcGetter);
}

on key 's'
{
  // set value of field content (field has common data type so no value path is needed)
  AREthSetValueDWord(gMcSetter,"",200);

  // call setter method
  AREthCallMethod(gMcSetter);
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
