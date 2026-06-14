# mostConfigureEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureEclSequence (long channel, long numIntervals, dword[] state, dword[] duration100us);
```

## Description

The function prepares VN2640 to generate a signal sequence on the ECL. The signal sequence can be started with the mostGenerateEclSeq function.

The sequence is defined in two arrays of dword. The first indicates the level (0: dominant, 1: recessive) of the generators output for each time interval. The second describes the duration for each time interval.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| numIntervals | number of intervals described in the following arrays |
| state | For each time interval 0: dominant1: recessive |
| duration100us | Duration of interval with a resolution of 100 µs. |

## Return Values

See error codes

## Example

```c
on key 's'
{
   // configure a rectangle wave with a period of 20 ms
   const long kEclSequenceLength = 8;
   dword eclSequenceStates[kEclSequenceLength] = { 0, 1, 0, 1, 0, 1, 0, 1};
   dword eclSequenceDuration[kEclSequenceLength] = { 100, 100, 100, 100, 100, 100, 100, 100};
   mostConfigureEclSequence(1, kEclSequenceLength, eclSequenceStates, eclSequenceDuration);
   // start generation of the sequence
   mostGenerateEclSequence(1, 1);
}

OnMostEclSequence(long state)
{
   if(state == 1)
   {
      write ("ECL Sequence Started!");
   }
   else
   {
   write ("ECL Sequence Stopped or Finished!");
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 SP3 | 7.6 SP3 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
