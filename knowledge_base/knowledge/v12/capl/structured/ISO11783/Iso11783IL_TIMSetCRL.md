# Iso11783IL_TIMSetCRL

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetCRL(byte crlType, char crlFilePath[]); // form 1
```

## Description

Loads a Certificate Revocation List file which is used for TIM authentication. If there is already a loaded certificate file for a certificate type these file is overwritten.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Certificate Revocation List for Testlab, Manufacturer, manufacturer series, TIM client and TIM server certificates. |
| 1 | Certificate Revocation List for the CRL signing CA certificates. |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
