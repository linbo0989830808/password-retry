pwssword = 'a123456'
i = 3 # 預設機會次數
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼： ')
	if pwd == pwssword:
		print('登錄成功')
		break
	else:
		print('密碼錯誤！ ') 
		if i > 0:
			print('還有',i , '次機會')
		else:
			print('帳號已鎖定')