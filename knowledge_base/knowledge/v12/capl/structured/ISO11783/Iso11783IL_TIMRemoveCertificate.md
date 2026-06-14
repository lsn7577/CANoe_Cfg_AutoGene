# Iso11783IL_TIMRemoveCertificate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMRemoveCertificate(byte certificateType); // form 1
```

## Description

Removes a certificate file which has been loaded Iso11783IL_TIMAddCertificate.

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
