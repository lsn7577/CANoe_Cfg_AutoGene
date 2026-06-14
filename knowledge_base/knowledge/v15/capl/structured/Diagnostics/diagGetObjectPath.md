# diagGetObjectPath

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetObjectPath (diagResponse obj, char buffer[], dword buffersize)
long diagGetObjectPath (diagRequest obj, char buffer[], dword buffersize)
```

## Description

Delivers the qualifier path of the object that must be specified upon generation.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| buffer | Input/output buffer |
| buffersize | Buffer size |

## Return Values

Length of path written to buffer, may be truncated.
Error code

## Example

```c
DumpReqParameterPaths( DiagRequest * req)
{
  DumpParameterPaths( req, 0);
}

DumpRespParameterPaths( DiagRequest * req)
{
  DumpParameterPaths( req, 1);
}

DumpParameterPaths( DiagRequest * req, long bDumpResponse)
{
  WORD i;
  char parameterPath[100];

  req.GetObjectPath( parameterPath, elcount( parameterPath));
  write( "Request is: %s", parameterPath);
  if( bDumpResponse)
    write( "Response parameters:");
  else
    write( "Request parameters:");

  i = 0;
    while( bDumpResponse && req.GetRespParameterPath( i, parameterPath, elcount( parameterPath)) > 0
    ||!bDumpResponse && req.GetParameterPath( i, parameterPath, elcount( parameterPath)) > 0)
  {
    write( "%2i %s", i, parameterPath);
    ++i;
  }
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
