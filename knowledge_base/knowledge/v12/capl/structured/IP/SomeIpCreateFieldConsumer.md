# SomeIpCreateFieldConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateFieldConsumer( dword csiHandle, long notificationId, long getterId, long setterId, char onFieldNotificationCallback[] );
```

## Description

This function adds a Field Consumer to a Consumed Service Instance that was created by SomeIpCreateConsumedServiceInstance.

When a suitable field notification is received, the passed Notification Callback is called (see <OnSomeIpFieldNotification>).

A Field Consumer can be removed again using the SomeIpRemoveFieldConsumer function.

## Return Values

0 An error occurred. The error can be evaluated using the SomeIpGetLastError function.

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
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,12,1);

  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,300);

  // create field consumer as well as getter and setter method calls
  SomeIpCreateFieldConsumer(csi,FieldNotificationID,FieldGetterID,FieldSetterID,"OnFieldNotification");
  gMcGetter = SomeIpCreateMethodCall(csi,FieldGetterID,"OnFieldGetterResponse");
  gMcSetter = SomeIpCreateMethodCall(csi,FieldSetterID,"OnFieldSetterResponse");
}

void OnFieldNotification(DWORD pfHandle,DWORD messageHandle)
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
