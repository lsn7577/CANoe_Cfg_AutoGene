# AREthCreateFieldConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCreateFieldConsumer( dword csiHandle, long notificationId, long getterId, long setterId, char onFieldNotificationCallback[] );
```

## Description

This function adds a Field Consumer to a Consumed Service Instance that was created by AREthCreateConsumedServiceInstance.

When a suitable field notification is received, the passed Notification Callback is called (see <OnAREthFieldNotification>).

A Field Consumer can be removed again using the AREthRemoveFieldConsumer function.

## Return Values

0 An error occurred. The error can be evaluated using the AREthGetLastError function.

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
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle
  dword ceg; // consumed Eventgroup handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,12,1);

  // create Eventgroup
  ceg = AREthAddConsumedEventGroup(csi,300);

  // create field consumer as well as getter and setter method calls
  AREthCreateFieldConsumer(csi,FieldNotificationID,FieldGetterID,FieldSetterID,"OnFieldNotification");
  gMcGetter = AREthCreateMethodCall(csi,FieldGetterID,"OnFieldGetterResponse");
  gMcSetter = AREthCreateMethodCall(csi,FieldSetterID,"OnFieldSetterResponse");
}

void OnFieldNotification(dword pfHandle,dword messageHandle)
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

| Since Version |
|---|
