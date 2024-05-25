```
tapeout41
```

```
for file in *.tapeout41; do
     echo "Hashing $file"
     sha256sum "$file"
done
```

