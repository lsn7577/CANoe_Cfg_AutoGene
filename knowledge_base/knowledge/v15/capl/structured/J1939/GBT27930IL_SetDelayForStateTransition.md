# GBT27930IL_SetDelayForStateTransition

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetDelayForStateTransition(double stateTransition, double delay); // form 1
long GBT27930IL_SetDelayForStateTransition(dbNode node , double stateTransition, double delay); // form 2
```

## Description

Defines delay for a state transition.

## Parameters

| Name | Type | Description |
|---|---|---|
| Value | Meaning for the Charger node | Meaning for the BMS node |
| 11 |  | After the K3 and K4 are closed (resp. GBT27930IL_StartChargingSimulation() is called): Start sending of CHM |
| 0 | After the appearance of the BHM: Stop sending of CHM and start sending of CRM (BMS is not recognized) | After the appearance of the CHM: Start sending of BHM |
| 1 | After the appearance of the BRM: Stop sending of CRM (BMS is not recognized) and start sending of CRM (BMS is recognized) | After the appearance of the CRM (BMS is not recognized): Stop sending of BHM and start sending of BRM |
| 2 | After the appearance of the BCP: Stop sending of CRM (BMS is recognized) and start sending of CML | After the appearance of the CRM (BMS is recognized): Stop sending of BRM and start sending of BCP |
| 3 | After the appearance of the BRO (Ready for charging): Stop sending of CML and start sending of CRO (Not ready for charging) | After the appearance of the CML: Stop sending of BCP and start sending of BRO (Not ready for charging) |
| 4 | After the sending of CRO (Not ready for charging) is started: Stop sending of CRO (Not ready for charging) and start sending of CRO (Ready for charging) | After the sending of BRO (Not ready for charging) is started: Stop sending of BRO (Not ready for charging) and start sending of BRO (Ready for charging) |
| 5 | After the appearance of the BCS: Stop sending of CRO (Ready for charging) and start sending of CCS | After the appearance of the CRO (Not ready for charging): Stop sending of BRO (Ready for charging) and start sending of BCL |
| 15 |  | After the sending of BCL is started: In addition to sending BCL, start sending BCS |
| 6 | After the appearance of the BST: Stop sending of CCS and start sending of CST. This is used when the BMS suspends charging. | After the appearance of the CCS: In addition to sending BCL and BCS, start sending BSM. If configured, BMV and BMT are also sent. |
| 16 |  | After the appearance of the CST: Stop sending of BST and start sending of BSD. This is used when the BMS suspends charging. |
| 7 | After the appearance of the BSD: Stop sending of CST and start sending of CSD | After the appearance of the CST: Stop sending of BCL, BCS and BSM and start sending of BST. This is used when the Charger suspends charging. |
| 8 | After the sending of the CSD is started: Stop sending of CSD, end of charging | After the sending of the BST is started: Stop sending of BST and start sending of BSD. This is used when the Charger suspends charging. |
| 9 |  | After the sending of the BSD is started: Stop sending of BSD, end of charging |
| delay |  | Time (in ms) for which the state transition is to be delayed. |
| node |  | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
