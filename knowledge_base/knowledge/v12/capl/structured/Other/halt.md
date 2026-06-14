# halt

> Category: `Other` | Type: `function`

## Syntax

```c
void halt();
```

## Description

The function stops both the debugged program as well as the simulation. The debugger window opens and the halt() command is displayed. The function thus creates a breakpoint while simultaneously interrupting the measurement in simulated mode (also for test modules). The simulation can be continued with <F9>. The halt instruction is ignored in Real mode.

## Return Values

—

## Example

```c
on key 'h'
{
  halt(); 
  // Stops execution of the simulation in Simulation mode
}
```

## Availability

| Since Version |
|---|
