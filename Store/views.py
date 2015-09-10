from django.shortcuts import render
from Store.models import Master_Data
import pdb
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.db.models import Max

# Create your views here.

def getinfo(request):
	if request.method == 'POST':
		serial_no = int(request.POST['serial_no'])
		try:
			data_obj = Master_Data.objects.get(serial = serial_no)
		except:
			data_obj = None
		if data_obj:
			print "Data is Available"
			data = {
					'serial_no' : serial_no, 
					'IC' : data_obj.Item_category, 
					'ISC' : data_obj.Item_Sub_Category, 
					'IN': data_obj.Item_Name, 
					'quantity':data_obj.Quantity, 
					'price' : data_obj.Price
					}
			print data
			context = Context(data)
			return render_to_response('details.html', context)
		else:
			return add_info(request)
			#print "Data is not available"
			#return render_to_response("add_item.html", {'serial_no' : serial_no}, context_instance=RequestContext(request))

def  add_info(request, data = None):
	serial_no = Master_Data.objects.all().aggregate(Max('serial'))['serial__max']
	#print serial_no
	if serial_no:
		serial_no = serial_no + 1
		return render_to_response("add_item.html", {'serial_no' : serial_no}, context_instance=RequestContext(request))
	else:
		serial_no = 10001
		return render_to_response("add_item.html", {'serial_no' : serial_no}, context_instance=RequestContext(request))

def home(request):
	#pdb.set_trace()
	return render(request, "home_page.html")
def home_page(request):
	return render(request, "home_page.html")

def save(request):
	val = request.POST('item_value')
	print "Please wait data is loading"
	data_obj = Master_Data(serial = int(data['serial_no']), Item_category = data['IC'], Item_Sub_Category = data['ISC'], Item_Name = data['IN'], Quantity = data['quantity'], Price = data['price'])
	print "Data is saving........."
	data_obj.save()
	print "Data is saved successfully"
	return render(request, "add_item.html")

def add_stock(request):
	return render(request, "add_stock_item_wise.html")

def add_stock_item_wise(request):
	if request.POST["serial_info"]:
		item = request.POST['serial_info']
		print item
		dt = Master_Data.objects.get(serial = item)
	else:
		item = request.POST['item_name']
		dt = Master_Data.objects.get(Item_Name = item)
	if item:
		try:
			if dt:
				print "Show the details to the user....."
				data_dic = {"serial_no":dt.serial,"IC":dt.Item_category, "ISC":dt.Item_Sub_Category, "IN":dt.Item_Name, "quantity":dt.Quantity, "price":dt.Price}
				print data_dic
				context = Context(data_dic)
				return render_to_response("add_stock.html", context)
		except Exception as e:
			print str(e)
			pass

def add_stock_one_shot(request):
	return render(request, "")