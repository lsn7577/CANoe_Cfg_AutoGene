# Iso11783IL_TIMSetPrivateKey

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetPrivateKey(char privateKeyFilePath[]); // form 1
```

## Description

Loads an ECC private key file which is used for TIM authentication. If there is already a private key then it is overwritten.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
