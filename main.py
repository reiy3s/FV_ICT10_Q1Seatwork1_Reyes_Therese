from pyscript import display, document

body{
    text-align: center;
    
}

display("Look at what I used!", target="div1")

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
    document.getElementById("output1").innerHTML = ""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 + num2
    display(f'The sum is {result}!', target = "output1")

def subtracting_numbers(e):
    document.getElementById("output1").innerHTML = ""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 - num2
    display(f'The difference is {result}!', target = "output1")

def multiplying_numbers(e):
    document.getElementById("output1").innerHTML = ""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 * num2
    display(f'The product is {result}!', target = "output1")

def dividing_numbers(e):
    document.getElementById("output1").innerHTML = ""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 / num2
    display(f'The quotient is {result}!', target = "output1")