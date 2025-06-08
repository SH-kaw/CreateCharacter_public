import random
import numpy as np
import json
rng = np.random.default_rng()

#キャラクター作成用クラス
class create_character :
    elements = ["火","水","土","木","金"]
    gender = ["男","女"]
    katakana = list("アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ")

    def __init__(self):
        self.result = []
            
        #""を区切りにkatakanaから3つを選んでリストの要素を結合
        name = "".join(random.choices(self.katakana, k=3))
        
        #random.choice() は文字列,random.choices() はリスト
        if name.startswith("ン") :
            name = random.choice(self.katakana)+name
        
        self.result.append("name="+name)

        #elementsから属性を選択してresultに追加
        elements_result = random.choices(self.elements)
        self.result.append("element="+str(elements_result))

        #strを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        str_result = rng.normal(50,10,1)
        str_result = np.round(str_result).astype(int)
        self.result.append("STR="+(str(str_result)))
        
        #intを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        int_result = rng.normal(50,10,1)
        int_result = np.round(int_result).astype(int)
        self.result.append("INT="+(str(int_result)))

        #powを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        pow_result = rng.normal(50,10,1)
        pow_result = np.round(pow_result).astype(int)
        self.result.append("POW="+(str(pow_result)))

        #dexを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        dex_result = rng.normal(50,10,1)
        dex_result = np.round(dex_result).astype(int)
        self.result.append("DEX="+(str(dex_result)))

        #hpを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        hp_result = rng.normal(50,10,1)
        hp_result = np.round(hp_result).astype(int)
        self.result.append("HP="+(str(hp_result)))

        #mpを平均30、標準偏差30の正規分布から出力して端数を切り捨て、幅が大きく-が出るため最低値を1に設定
        mp_result = rng.normal(30,30,1)
        mp_result = np.round(mp_result).astype(int)
        mp_result = np.maximum(mp_result, 1)
        self.result.append("MP="+(str(mp_result)))

        #appを平均50、標準偏差10の正規分布から出力して端数を切り捨て
        app_result = rng.normal(50,10,1)
        app_result = np.round(app_result).astype(int)
        self.result.append("APP="+(str(app_result)))

        #homeを平均40、標準偏差30の正規分布から出力して端数を切り捨て、幅が大きく-が出るため最低値を1に設定
        home_result = rng.normal(40,30,1)
        home_result = np.round(home_result).astype(int)
        home_result = np.maximum(home_result, 1)
        self.result.append("family background="+(str(home_result)))

        #性別を男女から選択
        gender_result = random.choice(self.gender)
        self.result.append("gender="+(str(gender_result)))

        #性別に応じて身長を男=165,女=155の標準偏差10の正規分布から出力して端数を切り捨て
        if gender_result == "男":
            height_result = rng.normal(165,10,1)
            height_result = np.round(height_result).astype(int)
            self.result.append("height="+(str(height_result)))
        elif gender_result == "女":
            height_result = rng.normal(155,10,1)
            height_result = np.round(height_result).astype(int)
            self.result.append("height="+(str(height_result)))
    

#lambda用グローバル関数
def lambda_handler(event, context):
        
    A = create_character()

    return {
        'statusCode': 200,
        'body': json.dumps(A.result,ensure_ascii=False)
    }
