from django.shortcuts import render
import pickle

# Create your views here.

x={'Ventilator support':{0: 'without', 1:'on'},
    'Pre ICU Wait Time':{},
    'APACHE III Diagnosis:':{},
    'Pulse Pressure': {1:'Normal', 0:'high', 2:'Normal'}, 
    'Heart Rate': {1:'Normal', 0:'high', 2:'Normal'},
    'Mean Aterial Pressure': {1:'Normal', 0:'high', 2:'Normal'},
    'Age':{1:'Old Adult', 0:'Adult', 2:'Young Adult'},
   	'ICU Death Prob':{},
    'Body Temprature':{},
    'Apache III Bodysystem':{0:'Cardiovascular', 1:'Gastrointestinal', 2:'Genitourinary', 3:'Gynecological', 4:'Hematological', 5:'Metabolic', 6:'Musculoskeletal',7:'Neurological', 8:'Respiratory', 9:'Sepsis', 10:'Trauma', },
    'Glassgo Coma Scale':{0:'Mild', 1:'Moderate', 2:'Normal', 3:'Sever',},
    'Admit Source':{'A&E':'Accident & Emergency', 'OR':'Operating Room', 'O_ICU'>'Other ICU' 'O_Hospital':'Other Hospital', 'Floor':'Floor'},
   	'BMI Category:':{0:'Morbidily Obesed', 1:'Normal', 2:'Obesed', 3:'Over weight', 4:'Under Weight' }}

def Home(request):
	if request.method == "POST":
		y=request.POST

		# u=f'''
		# A Patient {x["Ventilator support"][int(y["index3"][0])]} Ventilator support,
		# ICU Wait Time of {float(y["index0"][0])} hours, APACHE III Diagnosis of {float(y["index1"][0])},
		# {x["Pulse Pressure"][int(y["index9"][0])]} Pulse Pressure, {x["Heart Rate"][int(y["index10"][0])]} Heart Rate,
		# {x["Mean Aterial Pressure"][int(y["index11"][0])]} Mean Aterial Pressure, 
		# {x["Age"][int(y["index8"][0])]} Age Group, {float(y["index4"][0])} ICU Death Prob, 
		# {float(y["index2"][0])}℃ Body Temprature, {x["Apache III Bodysystem"][int(y["index5"][0])]} Apache III Bodysystem,
		# {x["Glassgo Coma Scale"][int(y["index7"][0])]} Glassgo Coma Scale, and  {x["Admit Source"] [str(y["index12"][0])]} 
		# Admit Source will have a:
		# '''

		u=f'''
		For a Patient {x["Ventilator support"][int(y["index3"][0])]} Ventilator support,
		ICU Wait Time of {float(y["index0"][0])} hours, APACHE III Diagnosis of {float(y["index1"][0])},
		{x["Pulse Pressure"][int(y["index9"][0])]} Pulse Pressure, {x["Heart Rate"][int(y["index10"][0])]} Heart Rate,
		{x["Mean Aterial Pressure"][int(y["index11"][0])]} Mean Aterial Pressure, 
		{x["Age"][int(y["index8"][0])]} Age Group, {float(y["index4"][0])} ICU Death Prob, 
		{float(y["index2"][0])}℃ Body Temprature, {x["Apache III Bodysystem"][int(y["index5"][0])]} Apache III Bodysystem, and
		{x["Glassgo Coma Scale"][int(y["index7"][0])]} Glassgo Coma Scale,
		'''
		parameters=u.strip('\n').replace('\n', ' ')
		print(parameters)

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

		prediction=model.predict_proba([data])
		if prediction[0][0] < 0.5:
			context = {'pred_result':int(round(prediction[0][0], 2)*100),
					   'parameters':parameters}
		else:
			context = {'pred_result':int(round(prediction[0][0], 2)*100),
			'parameters':parameters}
	else:
		context={}

	return render(request, 'icuclassifier/home.html', context=context )
