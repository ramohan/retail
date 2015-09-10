from Store.models import Master_data

Item_category = [['Grosery', 'Dal', 'Toor Dal 1Kg', 56, 75.60],
				['Grosery', 'Dal','Urud Dal 1Kg', 61, 76],
				['Grosery', 'Dal','Moong Dal 1Kg', 62, 73],
				['Grosery', 'Dal','Chenna Dal 1Kg', 63, 72],
				['Grosery', 'Dal', 'Urud Dal 5Kg', 60, 350],
				['Grosery', 'Dal', 'Toor Dal 5Kg', 50, 352],
				['Grosery', 'Dal', 'Chenna Dal 5Kg', 29, 340],
				['Grosery', 'Sugar','More Sugar 1Kg', 56, 25.60],
				['Grosery', 'Sugar','Reliance Sugar 1Kg', 26, 26],
				['Grosery', 'Sugar','Reliance Sugar 3Kg', 68, 33],
				['Grosery', 'Sugar','More Sugar 3Kg', 63, 72],
				['Grosery','Oil', 'Sunflower 1lt', 56, 75.60],
				['Grosery','Oil','Freedom 1lt', 61, 80],
				['Grosery','Oil','Rice Rich 1 lt', 62, 101],
				['Grosery','Oil','Freedom 3lt', 52, 210],
				['Cosmetics', 'Perfumes','Fogge', 25, 150.60],
				['Cosmetics', 'Perfumes','Park Avenue', 20, 162],
				['Cosmetics', 'Perfumes','Axe', 10, 180],
				['Cosmetics', 'Perfumes','Denim', 30, 100]
				['Cosmetics', 'Shampoo', 'Panteen', 50, 150],
				['Cosmetics', 'Shampoo','Head & Shoulders', 20, 120],
				['Cosmetics', 'Shampoo','Meera', 30, 100],
				['Cosmetics', 'Lip Stick', 'Lakme', 20, 160.60],
				['Cosmetics', 'Lip Stick','Revlon', 61, 170],										
				['Houseware', 'Chairs', 'NeelKamal', 20, 420],
				['Houseware', 'Chairs''Lavapola', 10, 320]
				]
con = 3
for item in Item_category:
	serial_no = Master_Data.objects.all().aggregate(Max('serial'))['serial__max']
	#print serial_no
	if serial_no:
		serial_no = serial_no + 1
	else:
		serial_no = 10001
	obj = Master_Data(serial = serial_no, Item_category = item[0], Item_Sub_Category = item[1], Item_Name = item[2], Quantity = item[3], Price = item[4])
	print  str(con) + 'rd ' + "is saving....Please wait..... "
	obj.save()
	print str(con) + 'rd ' + "is saved successfully"
	con = con + 1
print "Completed"