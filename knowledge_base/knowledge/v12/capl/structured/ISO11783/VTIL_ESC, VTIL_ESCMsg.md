# VTIL_ESC, VTIL_ESCMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ESC( ); // form 1
```

## Description

The VTIL_ESC methods simulate the press of the ESC means of the Virtual Terminal. As a result, the VT ESC message with the Object ID, where input was aborted, is sent.

The VTIL_ESCMsg methods send the VT ESC message (without triggering any event in the Virtual Terminal).

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
