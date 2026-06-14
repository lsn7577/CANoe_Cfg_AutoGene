# TestFRILDisturbPduUpdateBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long TestFRILDisturbPduUpdateBit(char aPduName[], int disturbanceCount, int updateBit);
```

## Description

This function modifies the update bit of a PDU. Different fault injections are possible.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Return Values

0: No error.

## Example

```c
// set the signal update bit of the signal “Signal_A” in PDU “PDU_A” for 100times to 1.
TestFRILDisturbSignalUpdateBit(“PDU_A”, Signal_A , 0, 100, 1);
```

## Availability

| Up to Version |
|---|
