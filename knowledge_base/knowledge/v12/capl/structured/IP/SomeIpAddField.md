# SomeIpAddField

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpAddField( dword psiHandle, long notificationId, long getterId, long setterId );
```

## Description

This function adds a field to a Provided Service Instance that was created by SomeIpCreateProvidedServiceInstance.

Field contents can be set using the corresponding access functions (SomeIpSetValue...). These changes are only applied when the SomeIpCommitField is called.

A field can be removed again using the SomeIpRemoveField function.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

In this example, it is assumed that the utilized field is contained in the FIBEX database that is assigned to the CANoe configuration. The field has the Notification ID 30, the Getter ID 31, and the Setter ID 32. The data type of the field is a standard data type (for example, UINT8).

```c
variables
{
  DWORD gPfld_A; // provided field handle
}

void Initialize()
{
  CONST DWORD FieldNotificationID = 30;
  CONST DWORD FieldGetterID       = 31;
  CONST DWORD FieldSetterID       = 32;

  DWORD aep;   // Application Endpoint handle
  DWORD psi;   // provided service handle
  DWORD peg;   // provided Eventgroup handle

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

on key 'n'
{
  // set value of field content (field has a common data type so no value path is needed)
  SomeIpSetValueDWord(gPfld_A,"",100);

  // commit field content ... notification is sent
  SomeIpCommitField(gPfld_A);
}
```

## Availability

| Since Version |
|---|
