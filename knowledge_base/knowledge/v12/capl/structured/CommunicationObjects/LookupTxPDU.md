# LookupTxPDU

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txPDURef * LookupTxPDU(char[] path)
```

## Description

Searches for the specified tx PDU. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Return Values

The tx PDU. An uninitialized object if the PDU is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
txPDURef MirrorState statePDU;
char path[200];
char pduName[50] = "Mirrors::MirrorState";
char sender[20] = "LeftMirror";

snprintf(path, elcount(path), "%s[%s]", pduName, sender);
statePDU = (txPDURef MirrorState) lookupTxPDU(path);
```

## Availability

| Since Version |
|---|
