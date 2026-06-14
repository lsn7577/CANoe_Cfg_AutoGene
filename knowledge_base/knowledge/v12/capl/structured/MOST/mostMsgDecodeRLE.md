# mostMsgDecodeRLE

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgDecodeRLE(mostAmsMessage * msg, long fktIds[], long buffersize)
```

## Description

mostMsgDecodeRLE() decodes the data area of a message and saves the function IDs in a list. Run Length Encoding in accordance with MOST Specification 2.4 Para. 2.3.9 is used. This function is suitable for evaluating messages of the FBlock.FktIds.Status type.

## Return Values

>=0: Number of valid function IDs in fktIds[]

## Availability

| Since Version |
|---|
