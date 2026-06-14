# vtsSetOutputMask

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetOutputMask (DWORD RowMask);
```

## Description

Activates the requested rows of a switch matrix module for dynamic stimulation (PWM, Bitstreams). The row selection is binary encoded into the call parameter.

## Return Values

0: Successful call

## Example

The following example demonstrates how an identical switch sequence defined in MyBitstream.txt (e.g. a bouncing contact simulation) is applied subsequently to all rows of a VT2832 channel.

```c
ToggleMatrixRows()
{
  int iRow;

  // This calls the method SetCurveType on VTS::MyMatrixChannel
  sysvar::VTS::MyMatrixChannel_1.SetCurveType(eVTSCurveTypeBitStream);

  // This calls the method LoadWFBitStream on VTS::MyMatrixChannel_2
  sysvar::VTS::MyMatrixChannel_1.LoadWFBitStream("MyBitstream.txt");

  // Configure waveform Parameters:
      // TimeIncrement (time to hold each sample)       = 20ms
      // Pause (pause between two waveform repetitions) = 0s
      // NumberOfRepeats (number of repetitions)        = 1

  sysvar::VTS::MyMatrixChannel_1.SetWFParams(0.020, 0.0, 1);

  // Start stimulation
  vtsStartStimulation("VTS::MyMatrixChannel_1");

  for (iRow = 1; iRow < 16; iRow = iRow << 1)
  {
    // This calls the method SetOutputMask on VTS::MyMatrixChannel_1
    vtsSetOutputMask("VTS::MyMatrixChannel_1", iRow);
  }

  // Stop the simulation
  vtsStopStimulation("VTS::MyMatrixChannel_1");
}
```

## Availability

| Since Version |
|---|
