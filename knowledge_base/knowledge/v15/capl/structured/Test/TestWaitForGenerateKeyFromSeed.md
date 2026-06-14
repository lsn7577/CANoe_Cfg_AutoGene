# TestWaitForGenerateKeyFromSeed

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForGenerateKeyFromSeed(byte seedArray[], dword seedArraySize, dword securityLevel, byte keyArray[], dword maxKeyArraySize, dword& keyArraySizeOut, dword appTimeout_ms); // form 1
long TestWaitForGenerateKeyFromSeed(byte seedArray[], dword seedArraySize, dword securityLevel, char variant[], char option[], byte keyArray[], dword maxKeyArraySize, dword& keyArraySizeOut, dword appTimeout_ms); // form 2
long TestWaitForGenerateKeyFromSeed(char ecuQualifier[], byte seedArray[], dword seedArraySize, dword securityLevel, byte keyArray[], dword maxKeyArraySize, dword& keyArraySizeOut, dword appTimeout_ms); // form 3
long TestWaitForGenerateKeyFromSeed(char ecuQualifier[], byte seedArray[], dword seedArraySize, dword securityLevel, char variant[], char option[], byte keyArray[], dword maxKeyArraySize, dword& keyArraySizeOut, dword appTimeout_ms); // form 4
```

## Description

Generates the security key from the seed using the configured Seed and Key DLL. The call into the DLL may need more time, therefore a test module may want to wait for the result in order not to disturb the real-time execution of the test.

## Parameters

| Name | Description |
|---|---|
| seedArray | Seed as returned from the ECU. |
| seedArraySize | Length of the seed returned from the ECU. |
| securityLevel | Which security level shall be unlocked? |
| variant | Optional argument indicating the current ECU variant. In the first form this value does not have to be provided by the CAPL program, but it is taken from the diagnostic description configuration. |
| option | Optional argument giving additional information influencing the key computation, e.g. the diagnostics session currently active. In the first form this value does not have to be provided by the CAPL program, but it is taken from the current ECU status, if configured and set. |
| keyArray | The result of the computation is written into this array. |
| maxKeyArraySize | Maximum key length allowed. |
| keyArraySizeOut | Actual size of the key returned by the DLL. |
| appTimeout_ms | Maximum time (in ms) the function waits for the computation function in the DLL to return. If the DLL needs longer than this, a timeout is reported. |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2: form 1, 2 9.0 SP3: form 3, 4 | — | — | — | 1.1: from 1, 2 2.1 SP3: from 3, 4 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
