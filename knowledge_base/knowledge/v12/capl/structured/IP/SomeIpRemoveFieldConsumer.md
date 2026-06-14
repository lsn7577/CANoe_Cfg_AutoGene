# SomeIpRemoveFieldConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveFieldConsumer( dword cfHandle );
```

## Description

Removes a Field from a Consumed Service Instance. The Field was previously added by SomeIpCreateFieldConsumer.

Afterwards, the callback registered with SomeIpCreateFieldConsumer is no longer called.

## Return Values

0: The function was successfully executed

## Example

```c
variables
{
  CONST DWORD FieldNotificationID = 30;
  CONST DWORD FieldGetterID = 31;
  CONST DWORD FieldSetterID = 32;
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle
  DWORD ceg; // consumed Eventgroup handle
  DWORD cfHandle; // consumed field handle
  DWORD gMcGetter; // getter method call
  DWORD gMcSetter; // setter method call
}

on start()
{
  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,12,1);
  // create Eventgroup
  ceg = SomeIpAddConsumedEventGroup(csi,300);
  // create field consumer as well as getter and setter method calls
  cfHandle = SomeIpCreateFieldConsumer(csi,FieldNotificationID,FieldGetterID,FieldSetterID,"OnFieldNotification");
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

on key 'r'
{
  SomeIpRemoveFieldConsumer (cfHandle);
}
```

## Availability

| Since Version |
|---|
