# AREthRemoveField

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveField( dword pfHandle );
```

## Description

This function removes a field from a Provided Service Instance.

The notification callback registered with AREthAddField is no longer called after this function is called. The field notification is no longer sent by the AUTOSAR Eth IL, and the AUTOSAR Eth IL will no longer respond to Field Setter and Field Getter methods.

## Parameters

| Name | Description |
|---|---|
| pfHandle | Handle of the field that was created by AREthAddField. |

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
