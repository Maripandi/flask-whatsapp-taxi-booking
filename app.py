from flask import Flask,render_template,request,redirect
from customfuncs.kmcalc import geopycalculator


app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def home():
    populardests = [
        'Chennai','Vellore','Kovai','Vellore','Thiruchy','Kumbakonam','Madurai','Thirunelveli','Thirupathy Tirumala'
    ]
    
    return render_template ('index.html', populardests=populardests)

@app.route('/msg',methods = ['POST'])
def msg():
    if request.method == 'POST':
        name = request.form['name']
        startlocation = request.form['startlocation']
        endlocation = request.form['endlocation']
        phnumber = request.form['phnumber']
        cartype = request.form['car']
        checkin = request.form['check_in']
        checkout = request.form['check_out']
        whatsappmsg = 'hey I am *'+name+'*\nI want a ride from *' +startlocation+'* to *'+endlocation+'* with *' +cartype+ '* type car. Date from *'+checkin+'* to *'+checkout+'*. Contact me on Phone/WhatsApp *'+phnumber+'*' 
        # print(whatsappmsg)
        return redirect( 'https://api.whatsapp.com/send?phone=+916361542457&text='+whatsappmsg+'.')

@app.route('/quickbook',methods = ['POST'])
def quickbook():
    if request.method == 'POST':
        destination = request.form['destination']
        # whatsappmsg = destination
        whatsappmsg = 'hey\n I want a ride '+destination+'*. Contact me on Phone/WhatsApp with same number' 
        print(whatsappmsg)
        return redirect( 'https://api.whatsapp.com/send?phone=+916361542457&text='+whatsappmsg+'.')

@app.route('/estimate', methods = ['POST'])
def estimate():
    if request.method == 'POST':
        type = request.form['radio']
        name = request.form['name']
        phone = request.form['phnumber']
        pickuplocation = request.form['startlocation']
        droplocation = request.form['endlocation']
        cartype = request.form['car']
        oneway = {
                'SEDAN':13,
                'SUV':18,
                'ETIOS':14,
                'INNOVA':19
        }
        roundtrip = {
                'SEDAN':11,
                'SUV':11,
                'ETIOS':15,
                'INNOVA':16
        }

        if type == 'OneWay Trip':
            km = kmph = oneway[cartype]
        elif type == 'Round Trip':
            # type = 'Round Trip (up and down)'
            km = roundtrip[cartype]
            kmph = roundtrip[cartype]*2
        distance = geopycalculator(pickuplocation,droplocation)
        # distance = geopycalculator('Madurai','Vaniyambadi')
        # printl = str(distance).replace(' km','0')
        distance = round(float(distance))
        price = distance*kmph
    return render_template('travelbox/estimateresult.html',
                        type = type,
                        name = name,
                        phone = phone,
                        pickup = pickuplocation,
                        drop = droplocation,
                        cartype = cartype,
                        km = km,
                        distance = distance,
                        price = price
    )
    
@app.route('/services',methods = ['POST','GET'])
def services():


    tndests = [
        " Ariyalur"," Chengalpattu"," Chennai"," Coimbatore"," Cuddalore"," Dharmapuri"," Dindigul"," Erode"," Kallakurichi",
        " Kanchipuram"," Kanyakumari"," Karur"," Krishnagiri"," Madurai"," Nagapattinam"," Namakkal"," Nilgiris"," Perambalur",
        " Pudukkottai"," Ramanathapuram"," Ranipet"," Salem"," Sivaganga"," Tenkasi"," Thanjavur"," Theni"," Thoothukudi",
        " Tiruchirappalli"," Tirunelveli"," Tirupathur"," Tiruppur"," Tiruvallur"," Tiruvannamalai"," Tiruvarur"," Vellore",
        " Viluppuram"," Virudhunagar"," Bangalore"," Pondicherry"," Tirupati"
    ]

    blrlocalities = [
       ' Around Railway Station','Begur Kopa Road','Doddaballapur Road','Electronic City','Hebbal','Hesaraghatta','Hoskote','Hosur',
       'Hosur Road','Indiranagar','International Airport','Jayanagar','JP Nagar','Kaggalipura','KGA Golf Course','Koramangala',
       'Krishnarajapuram','Kundana','Langford Town','Malleswaram','Marathahalli','MG Road','Minerva Circle','Mysore Road',
       'Palace Grounds','Race Course Road','Rajajinagar','Seshadripuram','Shivaji Nagar','Tumkur Road','Ulsoor Lake','Vasanth Nagar',
       'Whitefield','Yelahanka'
    ]

    bangalore = [
        'Airport', 'Electronics City', 'Marathahalli', 'Sarjapur Road', 'HAL', 'Yeswanthpur', 'Mejastics', 
        'HSR Layout', 'Manyata Tech Park', 'KR Puram', 'Whitefield'
    ]

    return render_template ('pages/services.html',tamilnadu=tndests,bangalore=bangalore)

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        # port
        debug = True
        # options
    )
