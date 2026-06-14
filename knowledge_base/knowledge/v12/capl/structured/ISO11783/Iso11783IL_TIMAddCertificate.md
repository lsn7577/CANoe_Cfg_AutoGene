# Iso11783IL_TIMAddCertificate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMAddCertificate(byte certificateType, char certificateFilePath[]); // form 1
```

## Description

Loads a certificate file which is used for TIM authentication. If there is already a loaded certificate file for a certificate type these file is overwritten.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | AEF Root certificate |
| 1 | Testlab certificate |
| 2 | Manufacturer certificate |
| 3 | Manufacturer series certificate |
| 4 | Device certificate |
| 5 | CRL signing certificate |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
