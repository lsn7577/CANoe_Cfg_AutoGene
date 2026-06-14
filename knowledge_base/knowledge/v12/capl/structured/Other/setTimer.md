# setTimer

> Category: `Other` | Type: `function`

## Syntax

```c
void setTimer(msTimer t, long duration); // form 1
```

## Description

Sets a timer.

## Return Values

—

## Example

```c
variables {
  msTimer t1;
  Timer t23;
}

on key F1 {
  setTimer(t1, 200); // set timer t1 to 200 ms
}

on key F2 {
  setTimer (t23, 2); // set timer t23 to 2 sec
}

on key F3 {
  setTimer (t23, 0, 1250*1000 ); // set timer t23 to 1.250 milliseconds
}

on timer t1 {
  write("F1 was pressed 200ms ago");
}

on timer t23 {
  write("F2 was pressed 2 sec ago or F3 1250000 nsec ago");
}
```

## Availability

| Since Version |
|---|
