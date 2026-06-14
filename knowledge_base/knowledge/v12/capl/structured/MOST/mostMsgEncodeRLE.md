# mostMsgEncodeRLE

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgEncodeRLE(mostAmsMessage * msg, long fktIds[], long size)
```

## Description

mostMsgEncodeRLE() encodes a list of function IDs and saves it in the data area of a message. Run Length Encoding in accordance with MOST Specification 2.4 Para. 2.3.9 is used. This function is suitable for compiling messages of the FBlock.FktIds.Status type.

## Return Values

See error codes

## Availability

| Since Version |
|---|
