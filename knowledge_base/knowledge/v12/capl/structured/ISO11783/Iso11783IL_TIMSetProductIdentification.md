# Iso11783IL_TIMSetProductIdentification

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetProductIdentification(char identification[]); // form 1
```

## Description

Sets the content of message Product identification (see ISO11783-12 B.10).

If the Product identification message is in the Tx list of the TIM node and a request for PGN 65242 (FC8Dh) is received then the Product identification message is sent using the data of parameter identification.

## Return Values

0: Property has been set successfully

## Example

```c
Iso11783IL_TIMSetProductIdentification (“1234567890ABC*Brand B*1962i*”);
```

## Availability

| Since Version |
|---|
