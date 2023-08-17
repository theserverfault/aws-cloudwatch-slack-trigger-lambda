# Get Started: Quick Doc

```
git clone https://github.com/theserverfault/aws-cloudwatch-slack-trigger-lambda
```

```
cd aws-cloudwatch-slack-trigger-lambda
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
