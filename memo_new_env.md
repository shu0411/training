# 新環境（WSL）での構築手順

## Python 環境構築

1. venv
   `python -m venv .env` 実行
2. pyenvのインストール
   <https://github.com/pyenv/pyenv>
3. `pip install -r requirements.txt`

## サクラエディタのコマンド起動

以下の内容を.bashrcに書き込み

```bash
function sakura() {
  sakura_arg=()
  for p in $@; do
      if [ -f "$p" ]; then sakura_arg+=("`wslpath -w $p`"); fi
  done
  (
    /mnt/c/Windows/System32/cmd.exe /c 'C:\path\to\sakura.exe' $sakura_arg[@] >/dev/null 2>&1 &
    sleep 2
    pid="$!"
    if [ -x "/proc/$pid" ]; then kill $pid; fi
  )
}
```

## Gitのユーザー名設定

```bash
git config --global user.name "min__96"
git config --global user.email "<mail>"
```

## Codex, Claudeインストール

```bash
curl -fsSL <https://claude.ai/install.sh> | bash
```

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```
