# GBT27930IL_SetMaxAllowedMissingTimeForMsg

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetMaxAllowedMissingTimeForMsg(dword msgCode, dword maxAllowedMissingTime); // form 1
long GBT27930IL_SetMaxAllowedMissingTimeForMsg(dbNode node, dword msgCode, dword maxAllowedMissingTime); // form 2
```

## Description

For simulated BMS node: defines the maximum time during which the specified message from the Charger may be missing. After this time the simulated BMS stops charging and starts sending the BEM message.

For simulated Charger node: defines the maximum time during which the specified message from the BMS may be missing. After this time the simulated Charger stops charging and starts sending the CEM message.

## Parameters

| Name | Type | Description |
|---|---|---|
| Value | Meaning for BMS Node | Meaning for Charger Node |
| 0 | CRM (BMS is not recognized) | — |
| 1 | CRM (BMS is recognized) | BRM |
| 2 | CML | BCP |
| 3 | CRO (not ready for charging) | BRO (not ready for charging) |
| 4 | CRO (ready for charging) | BRO (ready for charging) |
| 5 | CCS | BCL |
| 6 | CST | BCS |
| 7 | CSD | BST |
| 8 | CHM | BSD |
| maxAllowedMissingTime |  | Time in milliseconds. If the respective message is missing longer than defined, the simulated node switches to sending the BEM or CEM message with the corresponding content. |
| node |  | Simulation node to apply the function |

## Example

Example 1 (simulated BMS node, form 1)

Example 2 (simulated Charger node, form 1)

```c
variables
{
  enum AllowedMissingTimeOfChargerMsgs
  {
    crm_not_recognized  = 0,
    crm_recognized      = 1,
    cml                 = 2,
    cro_not_ready       = 3,
    cro_ready           = 4,
    ccs                 = 5,
    cst                 = 6,
    csd                 = 7,
    chm                 = 8
  };
}

SetMaxAllowedMissingTimeOfChargerMsgs()
{
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(chm,                60000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(crm_not_recognized, 30000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(crm_recognized,      5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(cml,                 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(cro_not_ready,       5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(cro_ready,          60000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(ccs,                 1000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(cst,                 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(csd,                10000);
}
enum AllowedMissingTimeOfBmsMsgs
{
    brm        = 0,
    bcp        = 1,
    broNotReady= 2,
    broReady   = 3,
    bcl        = 4,
    bcs        = 5,
    bst        = 6,
    bsd        = 7
  };

SetMaxAllowedMissingTimeOfBmsMsgs()
{
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(brm        ,5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(bcp        , 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(broNotReady, 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(broReady   , 60000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(bcl        , 1000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(bcs        , 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(bst        , 5000);
  GBT27930IL_SetMaxAllowedMissingTimeForMsg(bsd        , 10000);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | J1939 and Smart Charging Simulation BMS and Charger nodes | J1939 and Smart Charging Simulation BMS and Charger nodes | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
