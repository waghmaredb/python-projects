a = 1
b = "abc"
c = ["3", 1, "fdg"]
d = {
    "name": "Deepak",
    "surname": "Waghmare",
    "age": 10,
    "skills": ["science", "maths"]
    }

 


###List Examples
print(type(c[0]))
print(int(c[0])+2)
print(c[0]+str(c[1]))
print(c[0]+c[2])
print(c[-1])
c.append("qwer")
c[1] = "7"
print(c)

 

### Dict Examples

 

print(d["name"])
print(type(d["name"]))
d["age"] = 27
d["height"] = "1.80m"
print(d)
print(d["skills"][0])

 

output = {
  "msg": [
    {
      "aliasesA": [
        {
          "members": [
            "21:00:00:24:FF:7D:CE:1E"
          ],
          "name": "finance-esx_port1"
        }
      ],
      "zonesA": [
        {
          "members": [
            "P3000T_A_P2",
            "P3000T_B_P0",
            "finance-esx_port1"
          ],
          "name": "finance-esx_port1_PowerStore"
        }
      ]
    }
  ]
}

 

wwn = output["msg"][0]["aliasesA"][0]["members"][0]
print(wwn.lower())
print(d["name"].upper())
f = "asdf"
g = "qwer"
if f == g:
    print("ok")
else:
    print("different")

 

#exercise 1 - compare alias name with zone members. Do a for loop to iterate over zone members
print("exercise1")
alias = output["msg"][0]["aliasesA"][0]["name"]
print(alias.lower())

for x in output["msg"][0]["zonesA"][0]["members"]:
    if alias.lower() == x.lower():
        print("alias is already in the zone")
    else:
        pass

#exercise 2 - add more key-value to the output dictionary: size, model
print("exercise2")
output["msg"].append({"size": 1000, "model": "P3000T"})
output["size"]=1000
output["model"]="P3000T"

print(output["size"])

#exercise 3 - add output-size to d-age
print("exercise3")

#print(output["msg"][1]["size"]+d["age"])

print(output["size"]+d["age"])

#exercise 4 - concatenate zonesA-name in uppercase with d-surname in lowercase and hyphen in between
print("exercise4")

print(output["msg"][0]["zonesA"][0]["name"].upper() + "-" + d["surname"].lower())

