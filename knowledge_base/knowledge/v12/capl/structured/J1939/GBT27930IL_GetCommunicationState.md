# GBT27930IL_GetCommunicationState

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_GetCommunicationState( ); // form 1
```

## Description

Defines delay for a state transition.

## Return Values

Current state of charging communication. The following values are defined:
Value
Meaning for the Charger node
Meaning for the BMS node
0
Waiting for start of charging
Waiting for start of charging
1
Sending of CHM
Waiting for the first CHM
2
Sending of CHM; delayed start of CRM (BMS is not recognized) is initiated
Delayed start of BHM is initiated
3
Sending of CRM (BMS is not recognized)
Sending of BHM
4
Sending of CRM (BMS is not recognized); delayed start of CRM (BMS is recognized) is initiated
Sending of BHM; delayed start of BRM is initiated
5
Sending of CRM (BMS is recognized)
Sending of BRM
6
Sending of CRM (BMS is recognized); delayed start of CML is initiated
Sending of BRM; delayed start of BCP is initiated
7
Sending of CML
Sending of BCP
8
Sending of CML; delayed start of CRO (Not ready for charging) is initiated
Sending of BCP; delayed start of BRO (Not ready for charging) is initiated
9
Sending of CRO (Not ready for charging); delayed start of CRO (Ready for charging) is initiated
Sending of BRO (Not ready for charging); delayed start of BRO (Ready for charging) is initiated
10
Sending of CRO (Ready for charging)
Sending of of BRO (Ready for charging)
11
Sending of CRO (Ready for charging); delayed start of CCS is initiated
Sending of of BRO (Ready for charging); delayed start of BCL and BCS is initiated
12
Sending of CCS
Sending of BCL and BCS
13
Sending of CCS; delayed start of CST is initiated
Sending of BCL and BCS, delayed start of BSM is initiated
14
Sending of CST
Sending of BCL, BCS and BSM
15
Sending of CST; delayed start of CSD is initiated
Sending of BCL, BCS and BSM; delayed start of BST is initiated
16
Sending of CSD
Sending of BST
17
Sending of CSD; delayed stop of CSD is initiated
Sending of BST; delayed start of BSD is initiated
18
End of charging
Sending of BSD
19
—
Sending of BSD; delayed stop of BSD is initiated
20
—
End of charging

## Example

```c
—
```

## Availability

| Since Version |
|---|
