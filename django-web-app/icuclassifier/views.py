from django.shortcuts import render
import pickle

# Create your views here.

def Home(request):
	if request.method == "POST":

		model=pickle.load(open('pickel_lgb_model.pkl', 'rb'))
		data = []

		data.append(request.POST["index0"])
		data.append(request.POST["index1"])
		data.append(request.POST["index2"])
		data.append(request.POST["index3"])
		data.append(request.POST["index4"])
		data.append(request.POST["index5"])
		data.append(request.POST["index6"])
		data.append(request.POST["index7"])
		data.append(request.POST["index8"])
		data.append(request.POST["index9"])
		data.append(request.POST["index10"])
		data.append(request.POST["index11"])
		if request.POST["index12"] == 'Floor':
			data.append(1)
			data.append(0)
		elif request.POST["index12"] == 'OR':
			data.append(0)
			data.append(1)
		else:
			data.append(0)
			data.append(0)


		prediction=model.predict([data])
		if prediction > 0:
			context = {'pred_result':'ICU SURVIVAL IS LOW'}
		else:
			context = {'pred_result':'ICU SURVIVAL IS HIGH'}
	else:
		context={}
	return render(request, 'icuclassifier/home.html', context=context )
