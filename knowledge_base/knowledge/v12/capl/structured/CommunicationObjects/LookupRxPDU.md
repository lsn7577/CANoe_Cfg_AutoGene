# LookupRxPDU

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
rxPDURef * LookupRxPDU(char[] path)
```

## Description

Searches for the specified rx PDU. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Return Values

The Rx PDU. An uninitialized object if the PDU is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
rxPDURef MirrorState statePDU;
char path[200];
char pduName[50] = "Mirrors::MirrorState";
char receiver[20] = "CANoe";

snprintf(path, elcount(path), "%s[%s]", pduName, receiver);
statePDU = (rxPDURef MirrorState) lookupRxPDU(path);
```

## Availability

| Since Version |
|---|
