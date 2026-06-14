# frPDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frPDU <FIBEX PDU name> <PDU var>; // form 1
frPDU MsgChannel<num>.< FIBEX PDU name> <PDU var>; // form 2
frPDU <PDU var>; // form 3
```

## Description

This can be used to create a FlexRay PDU object. The object data can be manipulated via the object's selectors. Additional object properties can be read from the selectors.

The object is then registered using the frSetSendPDU and transmitted using the frUpdatePDU functions.

## Parameters

| Name | Description |
|---|---|
| <FIBEX PDU name> | String that corresponds to a PDU name in the database. The parameters needed to uniquely identify the PDU are taken from the corresponding PDU definition in the database. |
| <PDU var> | String that specifies the variable name of the object. |
| MsgChannel<num> | Specifies the transmission channel/cluster <num> must be a whole number (e.g. 1, 2, 3, ...) that specifies the channel number of the corresponding FlexRay interface. |

## Example

Example 1

For an example see function frUpdatePDU.

Example 2

This is an example for forwarding the payload to other functions.

Example 3

This is an example for using the PDU object as a function parameter.

Example 4

This is an example for using the PDU object in arrays.

Caution!

All objects of an array must be initialized with an appropriate PDU definition!

```c
void foo (byte[] data, int count)
{
  // evaluate the contents of the data array
}

void example ()
{
  frPDU EngineData myPDU;
  foo (myPDU.FR_Payload, myPDU.FR_PDULength);
}
variables
{
  frPDU EngineData myPDU;
}

void foo (FrPDU * pdu)
{
  // evaluate or set the contents of the PDU object
}

void example ()
{
  foo (myPDU);
}
variables
{
  frPDU EngineData pdu1;

  // All objects are equal:
   frPDU EngineData frPDUArray1[10];

  // All objects may be different:
  frPDU * frPDUArray2[2] = { EngineStatus, pdu1 };
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0: form 1 7.5: enhanced for usage in arrays and as function parameter: form 1 | 6.1: form 1 7.5: enhanced for usage in arrays and as function parameter: form 1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
