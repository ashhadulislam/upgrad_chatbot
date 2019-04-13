import zomatopy
import json



city_dict = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer',
'Aligarh','Allahabad','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi',
'Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad',
'Durg-Bhilai Nagar','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur',
'Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool',
'Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik',
'Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri',
'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruppur','Ujjain','Vijayapura',
'Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Warangal']

city_dict = [x.lower() for x in city_dict]
def check_location(loc,city_dict =city_dict):
	print("going to check location")
	config={"user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	location_results = len(location_json['location_suggestions'])

	if location_results ==0:
		return {'location_f' : 'notfound', 'location_new' : None}
	elif loc.lower() not in city_dict:
		return {'location_f' : 'tier3', 'location_new' : None}
	else:
		return {'location_f' : 'found', 'location_new' : loc}

		
		

