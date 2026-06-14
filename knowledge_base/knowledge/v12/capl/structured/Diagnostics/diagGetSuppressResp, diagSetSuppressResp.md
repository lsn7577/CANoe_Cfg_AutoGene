# diagGetSuppressResp, diagSetSuppressResp

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetSuppressResp (diagRequest req);
```

## Description

Under UDS (Unified Diagnostics Services), in certain requests it is possible to set the "suppressPosRspMsgIndicationBit" ("suppress positive response message indication bit"). This means that the receiver must not send any positive response. These two functions make it possible to poll and set this bit.

## Return Values

1: The bit is set.

## Availability

| Since Version |
|---|
