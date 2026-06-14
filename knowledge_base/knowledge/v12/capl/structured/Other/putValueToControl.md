# putValueToControl

> Category: `Other` | Type: `function`

## Syntax

```c
notation. putValueToControl("TestPanel","ControlOutput1", "\nSignal raw\n");
putValueToControl("TestPanel","ControlOutput1", TestMsg.Signal1.phys);
paragraph. putValueToControl("TestPanel","ControlOutput1", TestMsg.Signal1.phys, 1);
```

## Description

Assigns the value val to the Panel Designer Multi Display Control or the CAPL Output View with the name control. The Multi Display Control/ CAPL Output View is located on the panel with the title panel.

Different contents are displayed with the Multi Display Control/CAPL Output View. In addition to numbers (float and integer) and texts (char[]), in particular different messages (CAN, LIN, ... and J1939 PGNs) can also be displayed.

Using a Multi Display Control/CAPL Output View, no environment variable is necessary.

## Parameters

| Name | Description |
|---|---|
| panel | Name of the panel, restricted to 128 characters. |

## Return Values

—

## Example

```c
variables
{
...message MyMessage TestMsg;
}

}on key 'c'
{
//Output of a signal (physical) without additional parameter settings.
//In this case parameters have default settings;
//they are 'no new paragraph' and display signal in 'decimal' notation.
putValueToControl("TestPanel","ControlOutput1", "\nSignal raw\n");
putValueToControl("TestPanel","ControlOutput1", TestMsg.Signal1.phys);

//Output of a signal (physical), each time in a new paragraph.
putValueToControl("TestPanel","ControlOutput1", TestMsg.Signal1.phys, 1);
}
```

## Availability

| Since Version |
|---|
