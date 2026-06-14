# GBT27930IL_SetCommunicationState

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetCommunicationState(double newState); // form 1
long GBT27930IL_SetCommunicationState(dbNode node, double newState); // form 2
```

## Description

Defines the new state of charging communication.

## Parameters

| Name | Type | Description |
|---|---|---|
| Value | Meaning for the Charger node | Meaning for the BMS node |
| 0 | Waiting for start of charging | Waiting for start of charging |
| 20 |  | Delayed start of CHM is initiated |
| 1 | Sending of CHM | Waiting for the first CHM |
| 2 | Sending of CHM; delayed start of CRM (BMS is not recognized) is initiated | Delayed start of BHM is initiated |
| 3 | Sending of CRM (BMS is not recognized) | Sending of BHM |
| 4 | Sending of CRM (BMS is not recognized); delayed start of CRM (BMS is recognized) is initiated | Sending of BHM; delayed start of BRM is initiated |
| 5 | Sending of CRM (BMS is recognized) | Sending of BRM |
| 6 | Sending of CRM (BMS is recognized); delayed start of CML is initiated | Sending of BRM; delayed start of BCP is initiated |
| 7 | Sending of CML | Sending of BCP |
| 8 | Sending of CML; delayed start of CRO (Not ready for charging) is initiated | Sending of BCP; delayed start of BRO (Not ready for charging) is initiated |
| 9 | Sending of CRO (Not ready for charging); delayed start of CRO (Ready for charging) is initiated | Sending of BRO (Not ready for charging); delayed start of BRO (Ready for charging) is initiated |
| 10 | Sending of CRO (Ready for charging) | Sending of BRO (Ready for charging) |
| 11 | Sending of CRO (Ready for charging); delayed start of CCS is initiated | Sending of BRO (Ready for charging); delayed start of BCL is initiated |
| 30 |  | Sending of BCL |
| 31 |  | Sending of BCL; delayed start of BCS is initiated |
| 12 | Sending of CCS | Sending of BCL and BCS |
| 13 | Sending of CCS; delayed start of CST is initiated. Is skipped when BMS initializes the end of charging. | Sending of BCL and BCS, delayed start of BSM is initiated |
| 14 | Sending of CST | Sending of BCL, BCS and BSM |
| 15 | Sending of CST; delayed start of CSD is initiated | Sending of BCL, BCS and BSM; delayed start of BST is initiated. Is used when Charger initializes the end of charging. |
| 16 | Sending of CSD; delayed stop of CSD is initiated | Sending of BST. Is used when BMS initiates the end of charging. |
| 17 | End of charging | Sending of BST; delayed start of BSD is initiated |
| 18 | — | Sending of BSD; delayed stop of BSD is initiated |
| 19 | — | End of charging |
| 20 | — | — |
| 50 | Sending of CEM | Sending of CEM |
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
