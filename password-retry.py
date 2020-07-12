pwssword = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼： ')
	if pwd == pwssword:
		print('登錄成功')
		break
	else:
		i = i - 1
		print('密碼錯誤！ 還有',i , '次機會') 
		if i == 0:
			break