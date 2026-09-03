from pyscript import display

display("Look at what I used!", target="div1") #literal object

#variable objects

n4m3 = "Therese" #string
_4ge = 15 #int
h31g7 = 157.48 #float
_countries = ['Japan', 'Singapore', 'South Korea'] #list
n3w_s7ud3nt = False #boolean
req_keys = {
    "color": "Lavender",
    "car_brand": "Miata",
    "shoe_size": "36",
    "best_friend": "Mikmikk"
} #dictionary
fru1ts = {"mango", "melon", "longan", "banana", "grapes"} #set
d4y5 = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") #tuple

display(type(n4m3), target="div1")
display(type(_4ge), target="div1")
display(type(h31g7), target="div1")
display(type(_countries), target="div1")
display(type(n3w_s7ud3nt), target="div1")
display(type(req_keys), target="div1")
display(type(fru1ts), target="div1")
display(type(d4y5), target="div1")

def adding_numbers(e):
    document.getElementById("numbers").innerHTML="" # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st input
    num2 = float(document.getElementById('input2').value) # get 2nd input
    result = num1 + num2 # use operator to compute
    display(result, target = "numbers") #display output in div