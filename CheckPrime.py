'''
Xác định số nguyên tố
Yêu cầu
Trong bài toán này, bạn hãy xác định xem liệu một số đã cho là số nguyên tố hay hợp số.

Định dạng đầu vào
Dòng đầu tiên chứa một số nguyên T, biểu thị số lượng các trường hợp. 
Mỗi trường hợp bao gồm một dòng duy nhất chứa một số nguyên « n » (2 ≤ n ≤ 109)

Định dạng đầu ra
Đối với mỗi trường hợp, hãy in ra một dòng duy nhất chứa «YES» (không có dấu ngoặc kép và dấu cách), 
nếu số nguyên đã cho là số nguyên tố hoặc in «NO» (không có dấu ngoặc kép và dấu cách) nếu số nguyên đã cho là hợp số.
'''
import math

t = int(input())
for i in range(t):
	flag = True
	n = int(input())
	if n>1:
		# math.floor() can replace math.ceil() 
		for i in range(2,math.floor(math.sqrt(n)+1)):
			if (n%i)==0:
				flag = False
				break
	s = "YES" if flag == True else "NO"
	print(s)


