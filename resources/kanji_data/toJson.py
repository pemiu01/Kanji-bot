import json

outputfilename = '6.json'

txt = u'亡 寸 己 干 仁 尺 片 冊 収 処 幼 庁 穴 危 后 灰 吸 存 宇 宅 机 至 否 我 系 卵 忘 孝 困 批 私 乱 垂 乳 供 並 刻 呼 宗 宙 宝 届 延 忠 拡 担 拝 枚 沿 若 看 城 奏 姿 宣 専 巻 律 映 染 段 洗 派 皇 泉 砂 紅 背 肺 革 蚕 値 俳 党 展 座 従 株 将 班 秘 純 納 胸 朗 討 射 針 降 除 陛 骨 域 密 捨 推 探 済 異 盛 視 窓 翌 脳 著 訪 訳 欲 郷 郵 閉 頂 就 善 尊 割 創 勤 裁 揮 敬 晩 棒 痛 筋 策 衆 装 補 詞 貴 裏 傷 暖 源 聖 盟 絹 署 腹 蒸 幕 誠 賃 疑 層 模 穀 磁 暮 誤 誌 認 閣 障 劇 権 潮 熟 蔵 諸 誕 論 遺 奮 憲 操 樹 激 糖 縦 鋼 厳 優 縮 覧 簡 臨 難 臓 警'

jsonArray = txt.split()

with open(outputfilename, 'w',encoding='utf8') as outfile:
	outfile.write(json.dumps(jsonArray, ensure_ascii=False))