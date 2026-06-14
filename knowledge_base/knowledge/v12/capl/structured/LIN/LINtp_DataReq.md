# LINtp_DataReq

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_DataReq(byte data[], long numData, long NAD);
```

## Description

Send the given data. Once all data has been sent, the callback LINtp_DataCon is called. If there has been an error, LINtp_ErrorInd is called.

## Return Values

—

## Example

```c
BYTE data[20];
LINtp_DataReq( data, elcount(data), 0x12);
```

## Availability

| Since Version |
|---|
