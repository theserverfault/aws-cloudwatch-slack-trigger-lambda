# Get Started: Quick Doc

```
git clone https://github.com/theserverfault/cloudwatch-slack-alarms
```

```
cd cloudwatch-slack-alarms
```

```
python3 -m venv .
```

```
source bin/activate
```

```
pip3 install -r requirements.txt
```

### Build Layer

```
chmod +x generate_layer.sh
```

```
./generate_layer.sh
```

Upload the generated `layer.zip` from `dist/` folder
