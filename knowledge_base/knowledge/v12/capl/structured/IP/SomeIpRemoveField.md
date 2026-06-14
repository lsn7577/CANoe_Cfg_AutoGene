# SomeIpRemoveField

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveField( DWORD pfHandle );
```

## Description

This function removes a field from a Provided Service Instance.

The notification callback registered with SomeIpAddField is no longer called after this function is called. The field notification is no longer sent by the SOME/IP IL, and the SOME/IP IL will no longer respond to Field Setter and Field Getter methods.

## Return Values

0: The function was successfully executed.

## Example

```c
variables
{
  DWORD gPfld_A; // provided field handle
}

on start()
{
  CONST DWORD FieldNotificationID = 30;
  CONST DWORD FieldGetterID = 31;
  CONST DWORD FieldSetterID = 32;

  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  psi = SomeIpCreateProvidedServiceInstance(aep,12,1);
  // create Eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,300);
  // create field and add field to Eventgroup
  gPfld_A = SomeIpAddField(psi, FieldNotificationID, FieldGetterID, FieldSetterID);
  SomeIpAddFieldToEventGroup(peg,gPfld_A);
}

on key 'r'
{
  SomeIpRemoveField (gPfld_A);
}
```

## Availability

| Since Version |
|---|
