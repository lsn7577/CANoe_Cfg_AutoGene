# Example: Selector SIMULATED (message from simulated node)

> Category: `CAN` | Type: `selector`

### Example Selector SIMULATED (message from simulated node)

```c
on message LightState {
  if (this.dir == Rx) {
    if (!this.SIMULATED) {
      write("message LightState received from real system");
    }
    putvalue(Bulb,this.OnOff);
  }
  else {
    // write("message LightState received as Tx");
  }
}
```

### Note for CANoe Users

Please note the semantics of Rx for CAPL nodes in the Simulation Setup of CANoe.
