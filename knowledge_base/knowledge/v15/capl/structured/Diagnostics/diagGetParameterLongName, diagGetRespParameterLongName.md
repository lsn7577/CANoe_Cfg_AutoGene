# diagGetParameterLongName, diagGetRespParameterLongName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterLongName (diagResponse obj, dword paramNo, char buffer[], dword buffersize);
long diagGetParameterLongName (diagRequest obj, dword paramNo, char buffer[], dword buffersize);
long diagGetRespParameterLongName (diagRequest obj, dword paramNo, char buffer[], dword buffersize);
long diagGetParameterLongName (diagResponse obj, char paramPath[], char buffer[], dword buffersize);
long diagGetParameterLongName (diagRequest obj, char paramPath[], char buffer[], dword buffersize);
long diagGetRespParameterLongName (diagRequest obj, char paramPath[], char buffer[], dword buffersize);
```

## Description

Copies the long name of a diagnostic parameter into the buffer, honoring the character encoding configured in the diagnostic description. The text is converted into the encoding used in the CAPL program.

There are two ways to identify the parameter:

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostic object. |
| paramNo | Which parameter in the object, beginning with 0. |
| paramPath | Parameter in the object, identified by its qualifier (path). |
| buffer | Output buffer. Character encoding of the CAPL file will be honored. |
| bufferSize | Buffer size. |

## Return Values

Length of path written to buffer, may be truncated.
Error code

## Example

```c
// Write the parameter paths, names and symbolic values of a response object to the Write Window
DumpResponseParameterPaths( DiagResponse * resp)
{
  WORD i;
  char path[100];

  resp.GetObjectPath( path, elcount( path));
  write( "Object: %s", path);

  i = 0;
  while( resp.GetParameterPath( i, path, elcount( path)) > 0)
  {
    char parameterSymbol[200];
    char name[200];
    resp.GetParameter( path, parameterSymbol, elcount( parameterSymbol));
    DiagGetParameterLongName( resp, path, name, elcount(name));
    write( "%2i %-50s %-20s = %s", i, path, name, parameterSymbol);
    ++i;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP3 | 10.0 SP3 | — | — | — | 2.2 SP2 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
