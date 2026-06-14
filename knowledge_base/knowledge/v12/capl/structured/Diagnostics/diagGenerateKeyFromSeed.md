# diagGenerateKeyFromSeed

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGenerateKeyFromSeed ( byte seedArray[], dword seedArraySize, dword securityLevel, char variant[], char ipOption[], byte keyArray[], dword maxKeyArraySize, dword& keyActualSizeOut); // form 1
```

## Description

Creates a key to execute secured diagnostic functions within devices.

The key will be defined with the Seed of the device.If the computation takes more than 1 ms, diagStartGenerateKeyFromSeed in combination with the callback _Diag_GenerateKeyResult should be used.

## Return Values

At success 0 will be returned, otherwise an error code will be returned.
For further error analysis you can use the callback function _diag_GetError.

## Example

This example shows schematically the use of DiagGenerateKeyFromSeed and the Callback function in a CAPL test module.

```c
Variables
{
  ...
  //actual size of Seed and Key Arrays depend on ECU
  byte gSeedArray[2];
  int gSeedArraySize    = 2;
  int gSecurityLevel    = 0x20;
  char gVariant[200]    = "Variant1";
  char gOption[200]     = "option";
  byte gKeyArray[255];
  int  gMaxKeyArraySize = 255;
  dword gActualSizeOut     = 0;
  char gDebugBuffer[2000];
  diagRequest SecurityAccess::SecuritySeed::Request gSeedReq;
  diagResponse SecurityAccess::SecuritySeed::Request gSeedResp;
  diagRequest SecurityAccess::SecurityKey::Send gKeyReq;
  ...
}

//Unlock ECU by calling customer specific SeedKey DLL (e.g. in a CAPL test module)
{
  ...
  //Request seed from ECU
  diagSendRequest(gSeedReq);
  //Wait until request has been sent completely
  testWaitForDiagRequestSent(gSeedReq, 1000);
  //Wait for response and write seed from response parameter to array
  testWaitForDiagResponse(gSeedReq, 1000);
  diagGetLastResponse (gSeedReq, gSeedResp);
  diagGetParameterRaw (gSeedResp, "Seed", gSeedArray, elcount(gSeedArray));
  //Calculate key
  // _Diag_GetError is called when an error occurs
  if( 0 == diagGenerateKeyFromSeed (gSeedArray, gSeedArraySize, gSecurityLevel, gVariant, gOption, gKeyArray, gMaxKeyArraySize, gActualSizeOut))
  {
    //Write result to diagnostic request
    diagSetParameterRaw(gKeyReq, "Key", gKeyArray, gActualSizeOut);
    //Send Key to unlock ECU
    testWaitForDiagRequestSent(gKeyReq, 1000);
  }

//Callback function for error handling (optional)
_diag_GetError (char buffer[])
{
  //called if error in diagGenerateKeyFromSeed occurs
  snprintf(gDebugBuffer,elcount(gDebugBuffer),"%s", buffer);
  write("CALLBACK %s", gDebugBuffer);
}
```

## Availability

| Since Version |
|---|
