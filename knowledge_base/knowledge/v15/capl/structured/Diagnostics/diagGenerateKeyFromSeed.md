# diagGenerateKeyFromSeed

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGenerateKeyFromSeed ( byte seedArray[], dword seedArraySize, dword securityLevel, char variant[], char ipOption[], byte keyArray[], dword maxKeyArraySize, dword& keyActualSizeOut); // form 1
long DiagGenerateKeyFromSeed(char ecuQualifier[], byte seedArray[] , dword seedArraySize, dword securityLevel, char variant[], char option[] , byte keyArray[], dword maxKeyArraySize, dword& keyActualSizeOut); // form 2
```

## Description

Creates a key to execute secured diagnostic functions within devices.

The key will be defined with the Seed of the device.If the computation takes more than 1 ms, diagStartGenerateKeyFromSeed in combination with the callback _Diag_GenerateKeyResult should be used.

## Parameters

| Name | Description |
|---|---|
| seedArray | Seed for the definition of the key. |
| seedArraySize | Number of bytes in the SeedArray. |
| securityLevel | Security level for which the key will be created. |
| variant | Variant of the diagnostic description. |
| ipOption | Optional parameter that will be forwarded to the customer function. If not used, an empty string " " must be given here.Further options that will be forwarded to the DLL. If not present or an empty string, the value might be derived from the state of the communication, e.g. the diagnostic session the ECU is in. |
| keyArray | Key that is created with the customer DLL. |
| maxKeyArraySize | The maximum allowed number of bytes in the keyArray. |
| keyActualSizeOut | Actual used bytes in the keyArray. |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0: form 1 9.0 SP3: form 2 | 5.1: form 1 9.0 SP3: form 2 | — | — | — | 1.0: form 1 2.1 SP3: form 2 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
