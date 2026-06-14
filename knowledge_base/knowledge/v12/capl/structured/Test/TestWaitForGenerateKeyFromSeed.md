# TestWaitForGenerateKeyFromSeed

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForGenerateKeyFromSeed(byte seedArray[], dword seedArraySize, dword securityLevel, byte keyArray[], dword maxKeyArraySize, dword& keyArraySizeOut, dword appTimeout_ms); // form 1
```

## Description

Generates the security key from the seed using the configured Seed and Key DLL. The call into the DLL may need more time, therefore a test module may want to wait for the result in order not to disturb the real-time execution of the test.

## Return Values

1: Key generation successful

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
