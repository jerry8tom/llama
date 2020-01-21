from account import Account

API_KEY = "PK6PRNSO137JXGLH1LZ0"
API_SECRET = "X1cfuvOJN/BuNYCm0BhxawkmGw640JS/NeCQt1Y/"

if __name__ == '__main__':
	personal_acc = Account(API_KEY, API_SECRET)
	print (personal_acc)
