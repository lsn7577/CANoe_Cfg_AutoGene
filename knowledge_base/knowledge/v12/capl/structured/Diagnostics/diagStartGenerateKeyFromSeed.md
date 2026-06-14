# diagStartGenerateKeyFromSeed

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartGenerateKeyFromSeed( byte seedArray[], dword seedArraySize , dword securityLevel); // form 1
```

## Description

Starts generation of the security key from the seed using a Seed & Key DLL. Returns an error if computation could not be started.

The result of the computation is indicated by a call to the function _Diag_GenerateKeyResult. Note that the computation of a security key might take longer than 1 ms, which would cause problems with real-time event processing in CANoe. Therefore the computation is done in the background, i.e. the result is not available immediately. In tester nodes it is possible to use the function TestWaitForGenerateKeyFromSeed. If the computation is guaranteed to take much less than 1 ms, diagGenerateKeyFromSeed may be used.

## Return Values

0:If computation was startedotherwise: Error code

## Example

Unlock ECU after pressing <u>.

```c
_Diag_GenerateKeyResult( long result, BYTE computedKey[])
{
  diagRequest SendKeyLevel1 rqSendKey;

  if( 0 != result)
  {
    write( "Error: computing key returned %d", result);
    return;
  }

  // Success, i.e. a key was computed, so send it to the ECU

  rqSendKey.SetParameterRaw( "Key", computedKey, elcount( computedKey));
  rqSendKey.SendRequest();
}

On DiagResponse RequestSeedLevel1
{
  BYTE seed[4];
  count = this.GetParameterRaw( "Seed", seed, elcount(seed));
  // _Diag_GetError is called when an error occurs
  DiagStartGenerateKeyFromSeed( seed, elcount( seed), 1);
}

_Diag_GetError (char buffer[])
{
  //called if error in DiagGenerateKeyFromSeed occurs
  write("Diagnostic Error: %s", buffer);
}

On key 'u'  // unlock
{
  diagRequest RequestSeedLevel1 rqRequestSeed;
  rqRequestSeed.SendRequest();
}
```

## Availability

| Since Version |
|---|
