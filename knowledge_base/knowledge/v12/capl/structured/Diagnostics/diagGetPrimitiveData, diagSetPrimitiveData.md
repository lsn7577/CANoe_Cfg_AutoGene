# diagGetPrimitiveData, diagSetPrimitiveData

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetPrimitiveData (diagResponse obj, byte* buffer, DWORD buffersize)
```

## Description

Reads/sets the raw data of the complete service primitive (all data that is transmitted via the transport protocol).

When setting the data the length of the primitive is not changed.

## Return Values

Number of bytes copied into the buffer or error code

## Example

```c
// Print the length and first byte of a diagnostic request object
PrintDiagRequestBytes( diagRequest * req)
{
BYTE primitiveRaw[4095];
long size;
size = DiagGetPrimitiveData( req, primitiveRaw, elcount( primitiveRaw));
if( size > 0)
write( "Request = (%d)[%02x ...]", size, primitiveRaw[0]);
else
write( "Request: error %d", size);
}
```

## Availability

| Since Version |
|---|
