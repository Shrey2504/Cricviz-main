from django.shortcuts import render
import pandas as pd
import pickle


team_dict = {
    'KKR': 0,
    'DC': 1,
    'PBKS': 2,
    'GT': 3,
    'RR': 4,
    'RCB': 5,
    'LSG': 6,
    'SRH': 7,
    'CSK': 8,
    'MI': 9,
    'KXIP': 10,
    'RPS': 11,
    'GL': 12,
    'PWI': 13,
    'Kochi': 14
}

# Create your views here.
def prediction_view(request):
    res = 0
    if request.method == 'POST':
        # get all form data
        # get the form data
        home_team = int(request.POST.get('home_team'))
        away_team = int(request.POST.get('away_team'))
        season = int(request.POST.get('season'))
        toss_winner = int(request.POST.get('toss_won'))
        decision = int(request.POST.get('decision'))
        score = int(request.POST.get('score'))
        wickets = int(request.POST.get('wickets'))

        # load the trained model
        with open('Dashboards\modal.pickle', 'rb') as f:
            model = pickle.load(f)

        # perform prediction
        prediction = model.predict([[wickets, season,home_team, away_team, toss_winner,decision,score]])
        if(prediction==0):
            winner = list(team_dict.keys())[list(team_dict.values()).index(away_team)]
        else:
            winner = list(team_dict.keys())[list(team_dict.values()).index(home_team)]
        # return the predicted value
        return render(request, 'Dashboards/predict.html', {'prediction': winner})
    else:
        return render(request, 'Dashboards/predict.html')
    



def livescore(request):
    return render(request,'Dashboards/livescore.html')

def analysis(request):
    return render(request,'Dashboards/analysis.html')