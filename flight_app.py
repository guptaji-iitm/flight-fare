from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_pred.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("html_temp.html")
@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method =="POST":

        #Taking input for the departure
        dep_detail = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").day)

        Dep_hour = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").hour)
        Dep_minute = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").minute)

        #Taking input for the Arrival
        arr_detail = request.form["Arrival_Time"]
        Arr_hour = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").hour)
        Arr_minute = int(pd.to_datetime(dep_detail, format = "%Y-%m-%dT%H:%M").minute)

        #duration

        Duration_hours = abs(Arr_hour-Dep_hour)
        Duration_mins = abs(Arr_minute-Dep_minute)

        Total_Stops = int(request.form["stops"])

        #################################################################################

        airline = request.form['airline']
        if(airline=='Jet Airways'):
            Airline_Jet_Airways =1
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='Indigo'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='Air India'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline == 'Multiple carriers Premium economy'):

            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline == 'Jet Airways Business'):

            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0

        elif(airline=='Vistara Premium economy'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Truejet = 0

        elif(airline=='Truejet'):
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 1

        else:
            Airline_Jet_Airways = 0
            Airline_Indigo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy =0
            Airline_Truejet = 0


        Source = request.form["Source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        Destination = request.form["Source"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi= 0

        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi= 0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            Destination_New_Delhi= 0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            Destination_New_Delhi= 0

        elif (Destination == 'New Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi= 1

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi= 0

        prediction=model.predict([[
            Total_Stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_minute,
            Arr_hour,
            Arr_minute,
            Duration_hours,
            Duration_mins,
            Airline_Air_India,
            Airline_GoAir,
            Airline_Indigo,
            Airline_Jet_Airways,
            Airline_Jet_Airways_Business,
            Airline_Multiple_carriers,
            Airline_Multiple_carriers_Premium_economy,
            Airline_SpiceJet,
            Airline_Truejet,
            Airline_Vistara,
            Airline_Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi
        ]])

        output=round(prediction[0],2)

        return render_template('html_temp.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("html_temp.html")




if __name__ == "__main__":
    app.run(debug=True)
