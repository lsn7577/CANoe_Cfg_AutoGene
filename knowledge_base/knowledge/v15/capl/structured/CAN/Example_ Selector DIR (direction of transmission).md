# Example: Selector DIR (direction of transmission)

> Category: `CAN` | Type: `selector`

### Example Selector DIR (direction of transmission)

```c
on message 0x100 {
  if (this.DIR == Rx) {
    write("message 0x100 received");
  }
  if (this.DIR == Tx) {
    write("message 0x100 sent");
  }
}
```

### Note for CANoe Users

Please note the semantics of Rx for CAPL nodes in the Simulation Setup of CANoe.
