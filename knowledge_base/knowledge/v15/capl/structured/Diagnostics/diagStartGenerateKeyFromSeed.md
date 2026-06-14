# diagStartGenerateKeyFromSeed

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartGenerateKeyFromSeed( byte seedArray[], dword seedArraySize , dword securityLevel); // form 1
long diagStartGenerateKeyFromSeed( byte seedArray[], dword seedArraySize , dword securityLevel , char variant[], char option[]); // form 2
long diagStartGenerateKeyFromSeed(char ecuQualifier[], byte seedArray[] , dword seedArraySize, dword securityLevel); // form 3
long diagStartGenerateKeyFromSeed(char ecuQualifier[], byte seedArray[] , dword seedArraySize, dword securityLevel, char variant[], char option[]); // from 4
```

## Description

Starts generation of the security key from the seed using a Seed & Key DLL. Returns an error if computation could not be started.

The result of the computation is indicated by a call to the function _Diag_GenerateKeyResult. Note that the computation of a security key might take longer than 1 ms, which would cause problems with real-time event processing in CANoe. Therefore the computation is done in the background, i.e. the result is not available immediately. In tester nodes it is possible to use the function TestWaitForGenerateKeyFromSeed. If the computation is guaranteed to take much less than 1 ms, diagGenerateKeyFromSeed may be used.

## Parameters

| Name | Description |
|---|---|
| seedArray | Seed bytes as returned by the ECU. |
| seedArraySize | Number of bytes in the seedArray, as returned by the ECU. |
| securityLevel | Security level for which the key will be created. |
| variant | Variant qualifier as defined in the diagnostic description. In the first form of the function, this value will be the variant configured for the diagnostic description. |
| option | Further options that will be forwarded to the DLL. If not present or an empty string, the value might be derived from the state of the communication, e.g. the diagnostics session the ECU is in. |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP2: form 1, 2 9.0 SP3: form 3, 4 | 8.2 SP2: form 1, 2 9.0 SP3: form 3, 4 | — | — | — | 1.1 SP2: form 1, 2 2.1 SP3: form 3, 4 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
