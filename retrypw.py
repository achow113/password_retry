password = 'a123456'
n = 3 # 輸入次數機會
while n > 0:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break # stop loop
	else :
		n = n - 1
		print('密碼錯誤!還有', n , '次機會')
print(暫停輸入)
			



	