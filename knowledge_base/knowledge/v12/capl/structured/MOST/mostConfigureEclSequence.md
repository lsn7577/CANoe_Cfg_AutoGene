# mostConfigureEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureEclSequence (long channel, long numIntervals, dword[] state, dword[] duration100us)
```

## Description

The function prepares VN2640 to generate a signal sequence on the ECL. The signal sequence can be started with the mostGenerateEclSeq function.

The sequence is defined in two arrays of dword. The first indicates the level (0: dominant, 1: recessive) of the generators output for each time interval. The second describes the duration for each time interval.

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

| Since Version |
|---|
