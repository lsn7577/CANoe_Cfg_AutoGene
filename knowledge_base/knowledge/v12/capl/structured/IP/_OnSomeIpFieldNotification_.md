# <OnSomeIpFieldNotification>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnSomeIpFieldNotification>( dword cfHandle, dword messageHandle );
```

## Description

This callback function is called by SOME/IP IL when a notification message has been received for the field specified in the pfHandle parameter.

A callback function with this signature must be passed to the CAPL function SomeIpCreateFieldConsumer.

## Return Values

—

## Example

In this example, it is assumed that the utilized field is contained in the FIBEX database that is assigned to the CANoe configuration. The field has the Notification ID 30, the Getter ID 31, and the Setter ID 32. The data type of the field is a standard data type (for example, UINT8).

```c
variables
{
  DWORD gMcGetter; // getter method call
  DWORD gMcSetter; // setter method call
}

void Initialize()
{
  CONST DWORD FieldNotificationID = 30;
  CONST DWORD FieldGetterID       = 31;
  CONST DWORD FieldSetterID       = 32;

  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,12,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,300);

  // create field consumer as well as getter and setter method calls
  SomeIpCreateFieldConsumer(csi,FieldNotificationID,FieldGetterID,FieldSetterID, "OnSomeIpFieldNotification");
  gMcGetter = SomeIpCreateMethodCall(csi,FieldGetterID,"OnFieldGetterResponse");
  gMcSetter = SomeIpCreateMethodCall(csi,FieldSetterID,"OnFieldSetterResponse");
}

void OnSomeIpFieldNotification(DWORD pfHandle,DWORD messageHandle)
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
  SomeIpCallMethod(gMcGetter);
}

on key 's'
{
  // set value of field content (field has common data type so no value path is needed)
  SomeIpSetValueDWord(gMcSetter,"",200);

  // call setter method
  SomeIpCallMethod(gMcSetter);
}
```

## Availability

| Since Version |
|---|
