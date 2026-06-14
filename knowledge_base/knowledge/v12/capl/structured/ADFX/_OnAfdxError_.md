# <OnAfdxError>

> Category: `ADFX` | Type: `function`

## Syntax

```c
void <OnAfdxError> ( int64 timestamp, long channel, long errorType, char[] errorText, char[] errorAttributes );
```

## Description

This callback is called when an AFDX Error Event is received.

## Return Values

—

## Example

Node System - preStart in CAPL Browser

Node Callback Function in CAPL Browser

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

| Since Version |
|---|
