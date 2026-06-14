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

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the Provided Service Instance that was created with SomeIpCreateConsumerServiceInstance. |
| notificationId | Identifier of the field notification.If the field does not support a notifier, the value -1 must be specified here. |
| getterId | Identifier of the Field Getter method. If a consumer calls the getter method, the field content is returned by default. If this default behavior is to be changed, a method with the getterId must be created (see also SomeIpAddMethod and <OnSomeIpMethodRequest>). If the field does not support a getter method, the value -1 must be specified here. |
| setterId | Identifier of the Field Setter method. If a consumer calls the setter method, the field content is overwritten by default and the new field content is then sent via a response. If this default behavior is to be changed, a method with the getterId must be created (see also SomeIpAddMethod and <OnSomeIpMethodRequest>). If the field does not support a setter method, the value -1 must be specified here. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
