# OnAREthProcessTxARPDU

> Category: `IP` | Type: `function`

## Syntax

```c
long OnAREthProcessTxARPDU(dword sourceAddress, dword sourcePort, dword destinationAddress, dword destinationPort, dword length, char buffer[], dword headerID );
```

## Description

This callback is called before the interaction layer wants to send an AUTOSAR PDU. This makes it possible to suppress the transmission.

## Return Values

The AUTOSAR PDU is sent by the interaction layer, if the callback sends back 1. Otherwise the transmission is suppressed.

## Availability

| Since Version |
|---|
