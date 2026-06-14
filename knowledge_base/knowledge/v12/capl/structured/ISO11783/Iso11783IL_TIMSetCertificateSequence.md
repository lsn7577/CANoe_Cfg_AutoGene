# Iso11783IL_TIMSetCertificateSequence

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetCertificateSequence(dword certificateType1, dword certificateType2, dword certificateType3, dword certificateType4); // form 1
```

## Description

Sets the sequence of requested certificates.

Use this function to change the sequence of requested certificates. By default the following sequence is used:

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 1 | Testlab certificate |
| 2 | Manufacturer certificate |
| 3 | Manufacturer series certificate |
| 4 | Device certificate |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
