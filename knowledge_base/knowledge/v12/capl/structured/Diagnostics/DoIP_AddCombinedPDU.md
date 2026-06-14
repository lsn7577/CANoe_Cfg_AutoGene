# DoIP_AddCombinedPDU

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_AddCombinedPDU(dword payloadType, byte payload[], dword payloadLen);
```

## Description

Append another well-formed PDU to the PDU combination buffer for later sending with DoIP_SendPDUCombination. The currently configured protocol version byte will be used for the PDU.

## Return Values

-10: Invalid parameter: the payload type or PDU given is too large.

## Availability

| Since Version |
|---|
