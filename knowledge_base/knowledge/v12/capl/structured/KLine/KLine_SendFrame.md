# KLine_SendFrame

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SendFrame( byte data[], dword count)
```

## Description

Send data on the active K-Line communication channel.

The K-Line header is generated automatically due to header settings.

In a tester node, you can achieve this functionality by setting the diagnostics request to the byte sequence directly (with DiagResize and DiagSetPrimitiveData).

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
_Diag_DataRequest( BYTE data[], dword count, long furtherSegments)
{
   long status;
   status = KLine_SendFrame( data, count);
   write( "KLine_SendFrame returns %d for sending %d bytes", status, count);
}
```

## Availability

| Since Version |
|---|
