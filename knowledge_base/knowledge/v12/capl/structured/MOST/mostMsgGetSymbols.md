# mostMsgGetSymbols

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgGetSymbols(mostAmsMessage * msg, char[] fblock, char[] function, char[] optype, long bufferSize)
```

## Description

Determining the symbolic Names of the function block, the function and the Optype from an AMS or control message using the XML function catalog.

## Return Values

0: None of the three symbolic names could be determined.

## Availability

| Since Version |
|---|
