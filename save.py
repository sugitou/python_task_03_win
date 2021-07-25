import os
import csv
import datetime

# csvファイルの保存
def save_csv(save_dir, filename):
    # カレントディレクトリの取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    new_dir = f'{base_dir}\\{save_dir}'
    # 指定ディレクトリ作成
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print('new_dir',new_dir)
        print(os.path.isdir(new_dir))
    
    # サーチ後のcsvファイル読み込み
    # Windows環境なら以下
    with open(filename, 'r', encoding='utf_8-sig') as rf:
    # Mac環境のため今回はフルパスを指定
    # with open(f"/Users/right/python課題/project03/{filename}", 'r', encoding='utf_8-sig') as rf:
        h = next(csv.reader(rf))
        read_data = rf.readlines()
    
    # 現在時刻取得
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    new_file = now + '_' +filename
    output = new_dir + '\\' + new_file
    print('output', output)

    # データの書き込み
    with open(output, 'w', encoding='utf_8-sig') as wf:
        for line in read_data:
            wf.write(line)