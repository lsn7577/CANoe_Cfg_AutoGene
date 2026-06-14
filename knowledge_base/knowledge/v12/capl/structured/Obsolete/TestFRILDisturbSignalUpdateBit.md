# TestFRILDisturbSignalUpdateBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long TestFRILDisturbSignalUpdateBit(char aPduName[], char aSignalName[], long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

This function modifies the update bit of a signal. Different fault injections are possible.

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
