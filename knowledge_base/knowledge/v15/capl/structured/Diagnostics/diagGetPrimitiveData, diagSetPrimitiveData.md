# diagGetPrimitiveData, diagSetPrimitiveData

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetPrimitiveData (diagResponse obj, byte* buffer, DWORD buffersize)
long diagGetPrimitiveData (diagRequest obj, byte* buffer, DWORD buffersize)
long diagSetPrimitiveData (diagResponse obj, byte* buffer, DWORD buffersize)
long diagSetPrimitiveData (diagRequest obj, byte* buffer, DWORD buffersize)
```

## Description

Reads/sets the raw data of the complete service primitive (all data that is transmitted via the transport protocol).

When setting the data the length of the primitive is not changed.

## Parameters

| Name | Description |
|---|---|
| objxt | Diagnostics object |
| buffer | Input/output buffer |
| buffersize | Buffer size |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.0 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
