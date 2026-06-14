# SomeIpAddFieldToEventgroup

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpAddFieldToEventgroup( dword pevgHandle, dword pfHandle );
```

## Description

This function assigns a Field which was created by SomeIpAddField to an Event Group which was created by SomeIpAddProvidedEventGroup.

The Field can be removed from the Event Group with SomeIpRemoveFieldFromEventGroup.

## Parameters

| Name | Description |
|---|---|
| pevgHandle | Handle of the Event Group that should be assigned to an Event (see SomeIpAddProvidedEventGroup). |
| pfHandle | Handle of the Field that should be assigned to the Event Group (see SomeIpAddField). |

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
  SomeIpAddFieldToEventgroup(peg,gPfld_A);
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
