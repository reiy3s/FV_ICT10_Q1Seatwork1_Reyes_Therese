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



display(type(n4m3), target="div2")
display(type(_4ge), target="div2")
display(type(h31g7), target="div2")
display(type(_countries), target="div2")
display(type(n3w_s7ud3nt), target="div2")
display(type(req_keys), target="div2")
display(type(fru1ts), target="div2")
display(type(d4y5), target="div2")