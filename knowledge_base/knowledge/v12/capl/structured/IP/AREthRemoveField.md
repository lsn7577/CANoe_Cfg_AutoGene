# AREthRemoveField

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveField( dword pfHandle );
```

## Description

This function removes a field from a Provided Service Instance.

The notification callback registered with AREthAddField is no longer called after this function is called. The field notification is no longer sent by the AUTOSAR Eth IL, and the AUTOSAR Eth IL will no longer respond to Field Setter and Field Getter methods.

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
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);
  // create Service Instance
  psi = AREthCreateProvidedServiceInstance(aep,12,1);
  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,300);
  // create field and add field to Eventgroup
  gPfld_A = AREthAddField(psi, FieldNotificationID, FieldGetterID, FieldSetterID);
  AREthAddFieldToEventGroup(peg,gPfld_A);
}

on key 'r'
{
  AREthRemoveField (gPfld_A);
}
```

## Availability

| Since Version |
|---|
