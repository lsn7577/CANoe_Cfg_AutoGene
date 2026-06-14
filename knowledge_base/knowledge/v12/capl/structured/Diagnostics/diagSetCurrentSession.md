# diagSetCurrentSession

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetCurrentSession(long sessionId); // form 1
```

## Description

Sets the diagnostics session currently active in the ECU. This value may be used as optional argument for the computation of a key value from a seed, if configured.

## Return Values

Error code

## Example

```c
Testfunction ComputeKeyInExtendedSession( BYTE seed[], BYTE key[])
{
  DWORD keyLenOut;
  keyLenOut = 0;
  DiagSetCurrentSession( 0x03); // extended session
  // The key computation may use the current session as optional argument
  TestWaitForGenerateKeyFromSeed( seed, elcount( seed), 1, key, elcount(key), keyLenOut, 1000);
}
```

## Availability

| Since Version |
|---|
