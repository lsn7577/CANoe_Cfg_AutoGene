# J1939TestChkCreate_RTSCTSViolation

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_RTSCTSViolation(dword senderAddr, dword receiverAddr, dword timeouts[5], dword options);
```

## Description

Observes the RTS/CTS transport protocol. It is possible to observer all RTS/CTS transmissions or only the transmission of a specific send node.

## Example

```c
long rtsCheck;
dword timeouts[5] = { 750, 1250, 1250, 1050, 500};

rtsCheck = J1939TestChkCreate_RTSCTSViolation( timeouts, 0 );

J1939TestChkControl_Start(rtsCheck);
TestAddConstraint(rtsCheck);
```

## Availability

| Up to Version |
|---|
