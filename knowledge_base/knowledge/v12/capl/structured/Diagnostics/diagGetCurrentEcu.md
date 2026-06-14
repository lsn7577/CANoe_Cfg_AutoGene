# diagGetCurrentEcu

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCurrentEcu (char[] qualifier, dword bufferLen)
```

## Description

Gets the qualifier of the ECU for which the last event was processed, especially if a response was received from this ECU. This function can be used to determine the ECU that responded to a functional request.

In a diagnostics event handler in the measurement setup this function will return the target of request primitives and the source of response primitives (the other communication partner is always a tester).

## Return Values

Error code or length of the name provided.

## Example

```c
// diagnostic event handler
on diagResponse *
{
  char ecu[100];
  diagGetCurrentEcu( ecu, elcount(ecu));
  write( "Received response from %s", ecu);
}

// Test module
testcase TC1
{
  char ecu[100];
  diagRequest Service1 req1;
  diagSetTarget( "FunctionalGroup1");
  diagSendNetwork( req1);
  while( 1 == TestWaitForDiagResponse( req1, 1000))
  {
    diagGetCurrentEcu( ecu, elcount( ecu));
    write( "Received response from %s", ecu);
  }
}
```

## Availability

| Since Version |
|---|
