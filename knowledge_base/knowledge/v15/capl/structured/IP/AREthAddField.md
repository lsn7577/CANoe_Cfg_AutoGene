# AREthAddField

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddField( dword psiHandle, long notificationId, long getterId, long setterId );
```

## Description

This function adds a field to a Provided Service Instance that was created by AREthCreateProvidedServiceInstance.

Field contents can be set using the corresponding access functions (AREthSetValue...). These changes are only applied when the AREthCommitField is called.

A field can be removed again using the AREthRemoveField function.

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the Provided Service Instance that was created with AREthCreateConsumerServiceInstance. |
| notificationId | Identifier of the field notification.If the field does not support a notifier, the value -1 must be specified here. |
| getterId | Identifier of the Field Getter method. If a consumer calls the getter method, the field content is returned by default. If this default behavior is to be changed, a method with the getterId must be created (see also AREthAddMethod and <OnAREthMethodRequest>). If the field does not support a getter method, the value -1 must be specified here. |
| setterId | Identifier of the Field Setter method. If a consumer calls the setter method, the field content is overwritten by default and the new field content is then sent via a response. If this default behavior is to be changed, a method with the getterId must be created (see also AREthAddMethod and <OnAREthMethodRequest>). If the field does not support a setter method, the value -1 must be specified here. |

## Example

In this example, it is assumed that the utilized field is contained in the FIBEX database that is assigned to the CANoe configuration. The field has the Notification ID 30, the Getter ID 31, and the Setter ID 32. The data type of the field is a standard data type (for example, UINT8).

```c
variables
{
  dword gPfld_A; // provided field handle
}

void Initialize()
{
  CONST dword FieldNotificationID = 30;
  CONST dword FieldGetterID       = 31;
  CONST dword FieldSetterID       = 32;

  dword aep;   // Application Endpoint handle
  dword psi;   // provided service handle
  dword peg;   // provided Eventgroup handle

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

on key 'n'
{
  // set value of field content (field has a common data type so no value path is needed)
  AREthSetValueDWord(gPfld_A,"",100);

  // commit field content ... notification is sent
  AREthCommitField(gPfld_A);
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
