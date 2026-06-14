# <OnAfdxError>

> Category: `ADFX` | Type: `function`

## Syntax

```c
void <OnAfdxError> ( int64 timestamp, long channel, long errorType, char[] errorText, char[] errorAttributes );
```

## Description

This callback is called when an AFDX Error Event is received.

## Parameters

| Name | Description |
|---|---|
| timestamp | time stamp of the error event in ns |
| channel | channel number of the error event |
| errorType | 0: AfdxError 1: AfdxWarning 2: AfdxInfo |
| errorText | error text of the error event |
| errorAttributes | error attributes of the error event The attribute string has the following format: DataType;LineHeader;LineData DataType is S: String I: Integer D: Double |

## Return Values

—

## Example

```c
on preStart
{
  AfdxSetErrorHandler( "OnAfdxError");
}
void OnAfdxError( int64 timestamp, long channel, long errorType, char errorText[], char errorAttributes[])
{
  if (errorType == AfdxError)
  {
    write( "<%NODE_NAME%> Afdx Error on channel %d: %s", channel, errorText);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | — | — | — | —✔ |
| Restricted To | — | AFDX | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
