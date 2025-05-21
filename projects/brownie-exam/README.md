# Brownie Storage Contract Example

이 프로젝트는 Brownie를 사용하여 간단한 Storage 스마트 컨트랙트를 배포하는 예제입니다.

---

## 📦 프로젝트 구조

```
brownie-exam/
├── contracts/
│   └── Storage.sol
├── scripts/
│   └── deploy.py
├── tests/
│   └── test_storage.py
├── brownie-config.yaml
├── pyproject.toml
└── README.md
```

---

## ⚙️ 환경 설정

1. Python 3.10.x
2. [Poetry](https://python-poetry.org/docs/)
3. Ganache (CLI)  
   설치:
   ```bash
   npm install -g ganache
   sudo ln -s $(which ganache) /usr/local/bin/ganache-cli
   ```

---

## 🚀 설치 및 초기화

```bash
# 프로젝트 클론
git clone https://github.com/hlibbc/python-practice.git
cd projects/brownie-exam

# 가상환경 설정
poetry env use $(pyenv which python3.10)
poetry install
```

---

## 🔧 컴파일 및 배포

### 컴파일

```bash
poetry run brownie compile
```

### 배포 실행

```bash
poetry run brownie run scripts/deploy.py
```


---

## 🧪 테스트

```bash
poetry run brownie test
```
