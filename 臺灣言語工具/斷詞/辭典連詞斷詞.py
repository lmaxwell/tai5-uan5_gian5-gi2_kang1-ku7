# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組

class 辭典連詞斷詞:
	篩仔 = 字物件篩仔()
	分析器 = 拆文分析器()
	數字 = 阿拉伯數字()
	_連詞揀集內組 = 連詞揀集內組()

	# 字詞組集句=>句
	# 章=>章
	def 斷詞(self, 辭典, 連詞, 物件):
		if isinstance(物件, 章):
			return self.章斷詞(辭典, 連詞, 物件)
		if isinstance(物件, 字): 
			詞物件 = self.分析器.建立詞物件('')
			詞物件.內底字.append(物件)
			物件 = 詞物件
		if isinstance(物件, 詞):
			組物件 = self.分析器.建立組物件('')
			組物件.內底詞.append(物件)
			物件 = 組物件
		if isinstance(物件, 組):
			集物件 = self.分析器.建立集物件('')
			集物件.內底組.append(物件)
			物件 = 集物件
		if isinstance(物件, 集):
			句物件 = self.分析器.建立句物件('')
			句物件.內底集.append(物件)
			物件 = 句物件
		if isinstance(物件, 句):
			頂一層結果 = self.句斷詞(辭典, 連詞, 物件)
			return self._結果揣上好(連詞, 頂一層結果)
		self._掠漏.毋是字詞組集句章的毋著(物件)
	def _字陣列斷詞(self, 辭典, 連詞, 頂一个狀態, 頂一个分析, 這馬字陣列):
		if hasattr(辭典, '空'):
			這馬字陣列 = self.字陣列改數字(辭典, 這馬字陣列)
		頂一个上尾的詞, 頂一个上尾賰的字 = 頂一个狀態
		字陣列 = 頂一个上尾賰的字 + 這馬字陣列
		print('輸入', 字陣列, 這馬字陣列)
		print('輸入頂一个狀態', 頂一个狀態)
		斷詞結果 = []
		for 所在 in range(len(字陣列)):
			斷詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.上濟字數])))
# 			頂一个上尾的詞＝狀態
# 			分數 ,頂一个狀態,頂一个詞＝分析
# 			結果={狀態:分析}
		結果表 = [{頂一个上尾的詞:頂一个分析}]
		for 所在 in range(len(字陣列)):
			結果表.append({})
		for 所在 in range(len(字陣列) + 1):
			if len(結果表[所在]) == 0:
				詞物件 = 詞([字陣列[所在 - 1]])
				詞物件.屬性 = {'無佇辭典':True}
				for 上尾的詞, 分析 in 結果表[所在 - 1].items():
					分數 = 分析[0]
					這馬上尾詞 = (上尾的詞 + (詞物件,))[-連詞.上濟詞數 + 1:]
					結果表[所在][這馬上尾詞] = \
						(分數 + self._連詞揀集內組.評詞陣列分(連詞, 這馬上尾詞), 分析, 這馬上尾詞[-1])
			if 所在 < len(字陣列):
				for 斷詞集 in 斷詞結果[所在]:
					for 斷詞的候選詞 in 斷詞集:
						斷詞長度 = len(斷詞的候選詞.內底字)
						for 上尾的詞, 分析 in 結果表[所在].items():
							分數 = 分析[0]
							這馬上尾詞 = (上尾的詞 + (斷詞的候選詞,))[-連詞.上濟詞數 + 1:]
							結果表[所在 + 斷詞長度][這馬上尾詞] = \
								(分數 + self._連詞揀集內組.評詞陣列分(連詞, 這馬上尾詞), 分析, 這馬上尾詞[-1])
							print('結果表加', 結果表[所在 + 斷詞長度][這馬上尾詞])
		print('結果表', 結果表)
		結果 = {}
		for 所在 in range(min(辭典.上濟字數, len(結果表))):
			if 所在 == 0:
				賰的字 = tuple()
			else:
				賰的字 = tuple(字陣列[-所在:])
			for 上尾的詞, 分析 in 結果表[-所在 - 1].items():
				結果[(上尾的詞, 賰的字)] = 分析
		print('結果', 結果)
		return 結果
	def 字陣列改數字(self, 辭典, 字陣列):
		改字了字陣列 = []
		for 字物件 in 字陣列:
			if self.數字.是數量無(字物件.型):
				數量 = self.數字.轉數量(辭典.空, 字物件.型)
				組物件 = self.分析器.建立組物件(數量)
				改字了字陣列 += self.篩仔.篩出字物件(組物件)
			elif self.數字.是號碼無(字物件.型):
				號碼 = self.數字.轉號碼(辭典.空, 字物件.型)
				組物件 = self.分析器.建立組物件(號碼)
				改字了字陣列 += self.篩仔.篩出字物件(組物件)
			else:
				改字了字陣列.append(字物件)
		return 改字了字陣列
	def 集斷詞(self, 辭典, 連詞, 集物件, 頂一層結果):
		集物件結果 = {}
		for 狀態, 分析 in 頂一層結果.items():
			分數 , 頂一个狀態, 頂一个詞 = 分析
			for 組物件 in 集物件.內底組:
				字陣列 = self.篩仔.篩出字物件(組物件)
				結果 = self._字陣列斷詞(辭典, 連詞, 狀態, 分析, tuple(字陣列))
				for 這个狀態, 這个分析 in 結果.items():
					分數, 這个頂一个狀態 , 這个頂一个詞 = 這个分析
					if 這个狀態 not in 集物件結果 or 分數 > 集物件結果[這个狀態][0]:
						集物件結果[這个狀態] = 這个分析
				print('集物件結果', 集物件結果, 結果)
		return 集物件結果
	def 句斷詞(self, 辭典, 連詞, 句物件):
# 			頂一層上尾的詞,頂一層上尾賰的字＝狀態
# 			分數 ,頂一个狀態＝分析
# 			結果={狀態:分析}
		頂一層結果 = {((None,) * (連詞.上濟詞數 - 1), tuple()):(0, None, None)}
		for 集物件 in 句物件.內底集:
			頂一層結果 = self.集斷詞(辭典, 連詞, 集物件, 頂一層結果)
		return 頂一層結果
	def 章斷詞(self, 辭典, 連詞, 章物件):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
		標好章 = 章()
		用好句 = 標好章.內底句
		總分 = 0
		總詞數 = 0
		for 一句 in 章物件.內底句:
			斷好句物件, 分數, 詞數 = self.斷詞(辭典, 連詞, 一句)
			用好句.append(斷好句物件)
			總分 += 分數
			總詞數 += 詞數
		return 標好章, 總分, 總詞數
	def _結果揣上好(self, 連詞, 頂一層結果):
		上好分數 = None
		上好結果 = None
		print('上尾全部結果', 頂一層結果)
		for 上尾狀態, 一个一个結果 in 頂一層結果.items():
			if len(上尾狀態[1]) == 0:
				分數 = 一个一个結果[0] + self._連詞揀集內組.評詞陣列分(連詞, 上尾狀態[0] + (None,))
				if 上好分數 == None or 上好分數 < 分數:
					上好分數 = 分數
					上好結果 = 一个一个結果
		這馬結果 = 上好結果
		答案詞陣列 = []
		while 這馬結果 != None:
			print('這馬結果', 這馬結果)
			分數 , 頂一个結果, 這个詞 = 這馬結果
			答案詞陣列.append(這个詞)
			這馬結果 = 頂一个結果
		組物件 = self.分析器.建立組物件('')
		組物件.內底詞 = 答案詞陣列[-2::-1]
		集物件 = self.分析器.建立集物件('')
		集物件.內底組.append(組物件)
		句物件 = self.分析器.建立句物件('')
		句物件.內底集.append(集物件)
# 					print(上尾狀態, 分數 , 答案詞陣列, )
		print('結果', 句物件)
		return 句物件, 上好分數, len(答案詞陣列) - 1
		
