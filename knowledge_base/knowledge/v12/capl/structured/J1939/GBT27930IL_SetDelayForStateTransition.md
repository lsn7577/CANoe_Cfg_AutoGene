# GBT27930IL_SetDelayForStateTransition

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetDelayForStateTransition(double stateTransition, double delay); // form 1
```

## Description

Defines delay for a state transition.

## Parameters

| Name | Type | Description |
|---|---|---|
| Value | Meaning for the Charger node | Meaning for the BMS node |
| 0 | Stop sending of CHM and start sending of CRM (BMS is not recognized) | Start sending of BHM |
| 1 | Stop sending of CRM (BMS is not recognized) and start sending of CRM (BMS is recognized) | Stop sending of BHM and start sending of BRM |
| 2 | Stop sending of CRM (BMS is recognized) and start sending of CML | Stop sending of BRM and start sending of BCP |
| 3 | Stop sending of CML and start sending of CRO (Not ready for charging) | Stop sending of BCP and start sending of BRO (Not ready for charging) |
| 4 | Stop sending of CRO (Not ready for charging) and start sending of CRO (Ready for charging) | Stop sending of BRO (Not ready for charging) and start sending of BRO (Ready for charging) |
| 5 | Stop sending of CRO (Ready for charging) and start sending of CCS | Stop sending of BRO (Ready for charging) and start sending of BCL and BCS |
| 6 | Stop sending of CCS and start sending of CST. | In addition to sending BCL and BCS, start sending BSM. If configured, BMV and BMT are also sent. |
| 7 | Stop sending of CST and start sending of CSD | Stop sending of BCL, BCS and BSM and start sending of BST |
| 8 | Stop sending of CSD, end of charging | Stop sending of BST and start sending of BSD |
| 9 | — | Stop sending of BSD, end of charging |

## Example

```c
variables
{
  enum DelayTransition
  {
    first_bhm = 0,
    bhm_to_brm,
    brm_to_bcp,
    bcp_to_broNotReady,
    broNotReady_to_broReady,
    broReady_to_bcl_bcs,
    bcl_bcs_to_bcl_bcs_bcm
  };
}

on start
{
  GBT27930IL_InitAsBMS();

  GBT27930IL_SetDelayForStateTransition(first_bhm,               3000);
  GBT27930IL_SetDelayForStateTransition(bhm_to_brm,              3300);
  GBT27930IL_SetDelayForStateTransition(brm_to_bcp,              3600);
  GBT27930IL_SetDelayForStateTransition(bcp_to_broNotReady,      3900);
  GBT27930IL_SetDelayForStateTransition(broNotReady_to_broReady, 4200);
  GBT27930IL_SetDelayForStateTransition(broReady_to_bcl_bcs,     4500);
  GBT27930IL_SetDelayForStateTransition(bcl_bcs_to_bcl_bcs_bcm,  4800);
}
```

## Availability

| Since Version |
|---|
