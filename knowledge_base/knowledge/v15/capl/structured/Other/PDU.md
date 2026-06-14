# PDU

> Category: `Other` | Type: `function`

## Syntax

```c
PDU short <AUTOSAR short header ID> <PDU var>
PDU long <AUTOSAR long header ID> <PDU var>
PDU <AUTOSAR header ID> <PDU var>
PDU <AUTOSAR PDU name> <PDU var>
PDU * <PDU var>
```

## Description

Can be used to create a PDU object. The object data can be manipulated via the object's selectors. Additional object properties can be read from the selectors.

A PDU object can be sent using the TriggerPDU function.

## Parameters

| Name | Description |
|---|---|
| <PDU var> | String that specifies the variable name of the object. |

## Example

Example 1

Example 2

Example 3

```c
On key 'a'
{
  PDU short 4 myPDU;
  myPDU.signal1 = 25;
  TriggerPDU(myPDU);
}
void foo (PDU* parPDU)
{
  // evaluate PDU
}
void example ()
{
  PDU EngineData myPDU;
  foo (myPDU);
}
on PDU CAN_1::SOMEPDU1
{
  PDU CAN_2::SOMEPDU1 mypdu2;
  mypdu2.Payload = this.Payload;
  triggerPDU(mypdu2);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0: form 1 9.0 SP3: form 1 | 13.0 | — | 14 | 2.1 |
| Restricted To | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs (since version 9.0 SP3) FlexRay AUTOSAR PDUs (since version 9.0 SP3) AFDX FDS (since version 9.0 SP3) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) AFDX FDS (since version 9.0 SP3) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) AFDX FDS (since version 9.0 SP3) | — | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
