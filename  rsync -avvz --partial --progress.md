```
 ✘ thundermac@mac1T  ~  rsync -avvz --partial --progress --info=progress2 -e "ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -p 65081" hou_bxu_geo@eshell111.hpccube.com:/work/share/hou_admin/Agbami/benModel/A015_Drop2x2_Agbami_Down_CMP_for_Kirchoff_All.tapeout /Volumes/2TSeagate/A015_Drop2x2_Agbami_Down_CMP_for_Kirchoff_All2.tapeout
opening connection using: ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -p 65081 -l hou_bxu_geo eshell111.hpccube.com rsync --server --sender -vvlogDtprze.iLsfxCIvu . /work/share/hou_admin/Agbami/benModel/A015_Drop2x2_Agbami_Down_CMP_for_Kirchoff_All.tapeout  (16 args)
receiving incremental file list
delta-transmission enabled
A015_Drop2x2_Agbami_Down_CMP_for_Kirchoff_All.tapeout
940,127,751,465 100%    8.75MB/s   28:28:19 (xfr#1, to-chk=0/1)
total: matches=0  hash_hits=0  false_alarms=0 data=940127751465

sent 43 bytes  received 778,942,220,343 bytes  7,598,880.28 bytes/sec
total size is 940,127,751,465  speedup is 1.21
 thundermac@mac1T  ~  

```

