# InstaBot
インスタグラムの投稿をハッシュタグから取得していいねをするシステムです。

# 実行方法
1. 仮想環境を構築します。
```
python -m venv venv
```

2. 作成した仮想環境をアクティベートします。
```
source venv/bin/activate
```

3. 関連ライブラリのインストール
```
pip install -r requirements.txt
```

実行時に下記のパラメータを入れてください
- username (-u) : Your Instagram Username
- password (-p) : Your Instagram Password
- chromedriver (-c) : Your Chromedriver Path
- hashtag (-s) : HashTag
- n_likes (-n) : Number of Likes

Example:
```
python main.py -u test_user -p test_password -c ./chromedriver -s "instagood" -n 200
```

# Demo
![AnyConv com__sample2](https://user-images.githubusercontent.com/70655220/153893603-13b15910-1fa6-4fec-a271-35b430c5817b.gif)