# AfdxSetErrorHandler

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetErrorHandler( char callback[] );
```

## Description

Use this function to register a CAPL callback to handle AFDX error events.

## Return Values

0 or error code

## Example

Node System – PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  AfdxSetErrorHandler( "OnAfdxError");
}
void OnAfdxError( int64 time, long channel, long errorType, char errorText[], char errorAttributes[])
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
