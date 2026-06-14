# Socket Options: SOL_VECTOR

> Category: `TCPIPAPI` | Type: `notes`

## Description

The following socket options can be set at the SOL_VECTOR option level in CAPL. They influence the behavior of the socket. For all BOOL typed options a non-zero value will be interpreted as TRUE.

See Also

| Socket Option | Set/Get | Description | Type | Stack |
|---|---|---|---|---|
| SO_VLANPRIO | set/get | Overwrite the default VLAN priority for a socket. if set to 0xFF the socket uses the default VLAN priority again. | DWORD | C |
| TCP_SSTHRESH | Set/get | Set or get the slow start threshhold. | DWORD | C |
| TCP_CWND | Set/get | Set or get the congestion window size. | DWORD | C |
| TCP_INFO_STATE | get | Get the current TCP state of this connection. Possible values are: 0: CLOSED 1: LISTEN 2: SYN_SENT 3: SYN_RECEIVED 4: ESTABLISHED 5: CLOSE_WAIT 6: FIN_WAIT_1 7: CLOSING 8: LAST_ACK 9: FIN_WAIT_2 10: TIME_WAIT | DWORD | C |
| TCP_INFO_OPTIONS | get | Options enabled on connection. | DWORD | C |
| TCP_INFO_SND_WSCALE | get | RFC1323 send shift value. | DWORD | C |
| TCP_INFO_RCV_WSCALE | get | RFC1323 recv shift value. | DWORD | C |
| TCP_INFO_RTO | get | Retransmission timeout (usec). | DWORD | C |
| TCP_INFO_SND_MSS | get | Max segment size for send. | DWORD | C |
| TCP_INFO_RCV_MSS | get | Max segment size for receive. | DWORD | C |
| TCP_INFO_LAST_DATA_RECV | get | Time since last recv data. | DWORD | C |
| TCP_INFO_RTT | get | Smoothed RTT in usecs. | DWORD | C |
| TCP_INFO_RTTVAR | get | RTT variance in usecs. | DWORD | C |
| TCP_INFO_SND_SSTHRESH | get | Slow start threshold. | DWORD | C |
| TCP_INFO_SND_CWND | get | Send congestion window. | DWORD | C |
| TCP_INFO_RCV_SPACE | get | Advertised recv window. | DWORD | C |
| TCP_INFO_SND_WND | get | Advertised send window. | DWORD | C |
| TCP_INFO_SND_BWND | get | Bandwidth send window. | DWORD | C |
| TCP_INFO_SND_NXT | get | Next egress sequence number. | DWORD | C |
| TCP_INFO_RCV_NXT | get | Next ingress sequence number. | DWORD | C |

| Version 15© Vector Informatik GmbH |
|---|
