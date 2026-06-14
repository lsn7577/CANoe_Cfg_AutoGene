# StopStimulation

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.StopStimulation ();
```

## Description

Stops the output of a stimulation signal. This resets the stimulation mode. Therefore it is not sufficient to call StartStimulation to start the output again. You also have to restore the stimulation mode, e.g. by calling SetStimulationMode.

At the end of the execution of the command there is a short break before other commands will be executed. This means that the next functions will be executed after a short delay.With this procedure ensures that the stop command is executed effectively. The command should be called only in context of a test module setup but not in handler functions. In handler functions the correct execution of the stop command can not be ensured.

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
