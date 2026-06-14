# SetReplayFileName

> Category: `Other` | Type: `function`

## Syntax

```c
dword setReplayFileName(char nameOfReplayBlock[], char fileName[], char fileType[]);
```

## Description

Replaces the source file of an existing Replay Block. The function call temporarily stops the replay and restarts the Replay Block with the new source file.

The function call will not modify the configuration of the Reply block in the Simulation Setup or the transmit branch. The new file will not be stored when saving the configuration.

If you change the source file during measurement in the configuration dialog of the Reply block, the new file name will be stored in the configuration.

## Example

```c
SetReplayFilename("R", "replay_test_capl1.asc", "asc");
SetReplayFilename("R", "replay_test_capl1.blf", "blf");
SetReplayFilename("R", "replay_test_capl1.mf4", "blf");
```

## Availability

| Since Version |
|---|
