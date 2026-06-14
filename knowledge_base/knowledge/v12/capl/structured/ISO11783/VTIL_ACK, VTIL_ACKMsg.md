# VTIL_ACK, VTIL_ACKMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ACK(dword duration ); // form 1
```

## Description

Simulates the press of the ACK means of the Virtual Terminal. As a result, the Soft Key Activation message is immediately sent to the active Working Set with key activation code = pressed, then every 200 ms with the key activation code = still held and after the duration with the key activation code = released.

The VTIL_ACKMsg methods only send the Soft Key Activation message to the active Working Set (without triggering any event in the Virtual Terminal). In the sent Soft Key Activation messages the object ID of the Key object is always 0xFFFF and the key number is always 0.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
