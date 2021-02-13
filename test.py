"""
このファイルに解答コードを書いてください
"""

def fizz_buzz(arr: list, num: int):
    outputs = []
    for n, s in arr:
        if num % n == 0:
            outputs.append(s)
    if len(outputs) != 0:
        print("".join(outputs))
    else:
        print(num)

if __name__ == '__main__':
    # ファイルの読み込み
    with open("input.txt", mode="r") as f:
        inputs_txt = f.readlines()
    # 最終行を入力用にポップ
    num = inputs_txt.pop(-1)
    # データの前処理
    inputs = []
    for l in inputs_txt:
        l = l.replace("\n", "")
        l = l.split(":")
        inputs.append((int(l[0]), l[1]))
    # 不要なメモリの削除
    del inputs_txt
    # データのソート
    inputs = sorted(inputs)
    # 呼び出し
    fizz_buzz(inputs, int(num))
